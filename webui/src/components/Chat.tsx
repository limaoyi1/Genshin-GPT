import {useMemo, useCallback, useEffect} from "react";

import {
    MainContainer,
    Sidebar,
    ConversationList,
    Conversation,
    Avatar,
    ChatContainer,
    ConversationHeader,
    MessageGroup,
    Message,
    MessageList,
    MessageInput,
    TypingIndicator
} from "@chatscope/chat-ui-kit-react";

import {
    useChat,
    ChatMessage,
    MessageContentType,
    MessageDirection,
    MessageStatus
} from "@chatscope/use-chat";
import {MessageContent, TextContent, User} from "@chatscope/use-chat";

let uniqueId = localStorage.getItem('uniqueId');

function generateUniqueIdentifier() {
    if (!uniqueId) {
        // Generate a new unique identifier if it doesn't exist in localStorage
        uniqueId = Date.now().toString(36) + Math.random().toString(36).substr(2);
        localStorage.setItem('uniqueId', uniqueId);
    }

    return uniqueId;
}

export const Chat = ({user}: { user: User }) => {


    // Get all chat related values and methods from useChat hook 
    const {
        currentMessages,
        conversations,
        activeConversation,
        setActiveConversation,
        sendMessage,
        getUser,
        currentMessage,
        setCurrentMessage,
        sendTyping,
        setCurrentUser
    } = useChat();

    useEffect(() => {
        setCurrentUser(user);
    }, [user, setCurrentUser]);

    // Get current user data
    const [currentUserAvatar, currentUserName] = useMemo(() => {

        if (activeConversation) {
            const participant = activeConversation.participants.length > 0 ? activeConversation.participants[0] : undefined;

            if (participant) {
                const user = getUser(participant.id);
                if (user) {
                    return [<Avatar src={user.avatar}/>, user.username]
                }
            }
        }

        return [undefined, undefined];

    }, [activeConversation, getUser]);

    const handleChange = (value: string) => {
        // Send typing indicator to the active conversation
        // You can call this method on each onChange event
        // because sendTyping method can throttle sending this event
        // So typing event will not be send to often to the server
        setCurrentMessage(value);
        if (activeConversation) {
            sendTyping({
                conversationId: activeConversation?.id,
                isTyping: true,
                userId: user.id,
                content: value, // Note! Most often you don't want to send what the user types, as this can violate his privacy!
                throttle: true
            });
        }

    }

    const handleSend = (text: string) => {
        const message = new ChatMessage({
            id: "", // Id将由存储生成器生成，因此在这里可以传递空字符串
            content: text as unknown as MessageContent<TextContent>,
            contentType: MessageContentType.TextHtml,
            senderId: user.id,
            direction: MessageDirection.Outgoing,
            status: MessageStatus.Sent,
        });

        if (activeConversation) {
            sendMessage({
                message,
                conversationId: activeConversation.id,
                senderId: user.id,
            });

            // 假设'role'和'uuid'在此处可用，将它们替换为适当的值
            const requestData = {
                role: currentUserName, // 将聊天对象的名称替换为实际的值
                uuid: generateUniqueIdentifier() + "-" + currentUserName, // 将对话生成的唯一ID替换为实际的值
                query: text, // 用户输入的文本
            };

            // 发送POST请求到服务器
            fetch("http://www.limaoyi.top:4396/generate_answer", { //http://www.limaoyi.top:4396/generate_answer //http://127.0.0.1:5000/generate_answer
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(requestData),
            })
                .then((response) => response.text())
                .then((data) => {
                    // 在收到服务器响应后，将其作为新的聊天消息添加到 currentMessages 数组中
                    const responseMessage = new ChatMessage({
                        id: "", // Id将由存储生成器生成，因此在这里可以传递空字符串
                        content: data as unknown as MessageContent<TextContent>, // 将服务器响应的数据作为聊天消息的内容
                        contentType: MessageContentType.TextHtml,
                        senderId: "server", // 假设服务器的senderId为"server"
                        direction: MessageDirection.Incoming, // 将方向设置为Incoming表示是收到的消息
                        status: MessageStatus.Sent,
                    });

                    if (activeConversation) {
                        // 添加被聊天者的回答到当前会话中
                        sendMessage({
                            message: responseMessage,
                            conversationId: activeConversation.id,
                            senderId: "server", // 将服务器的senderId设置为"server"
                        });
                    }
                })
                .catch((error) => {
                    // 处理请求期间出现的任何错误
                    console.error("发送请求时出错:", error);
                });
        }
    };

    const getTypingIndicator = useCallback(
        () => {

            if (activeConversation) {

                const typingUsers = activeConversation.typingUsers;

                if (typingUsers.length > 0) {

                    const typingUserId = typingUsers.items[0].userId;

                    // Check if typing user participates in the conversation
                    if (activeConversation.participantExists(typingUserId)) {

                        const typingUser = getUser(typingUserId);

                        if (typingUser) {
                            return <TypingIndicator content={`${typingUser.username} is typing`}/>
                        }

                    }

                }

            }


            return undefined;

        }, [activeConversation, getUser],
    );

    return (<MainContainer responsive>
        <Sidebar position="left" scrollable>
            <ConversationHeader style={{backgroundColor: "#fff"}}>
                <Avatar src={user.avatar}/>
                <ConversationHeader.Content>
                    {user.username}
                </ConversationHeader.Content>
            </ConversationHeader>
            <ConversationList>
                {conversations.map(c => {
                    // Helper for getting the data of the first participant
                    const [avatar, name] = (() => {

                        const participant = c.participants.length > 0 ? c.participants[0] : undefined;

                        if (participant) {
                            const user = getUser(participant.id);
                            if (user) {

                                return [<Avatar src={user.avatar}/>, user.username]

                            }
                        }

                        return [undefined, undefined]
                    })();

                    return <Conversation key={c.id}
                                         name={name}
                                         info={c.draft ? `Draft: ${c.draft.replace(/<br>/g, "\n").replace(/&nbsp;/g, " ")}` : ``}
                                         active={activeConversation?.id === c.id}
                                         unreadCnt={c.unreadCounter}
                                         onClick={() => setActiveConversation(c.id)}>
                        {avatar}
                    </Conversation>
                })}
            </ConversationList>
        </Sidebar>

        <ChatContainer>
            {activeConversation && <ConversationHeader>
                {currentUserAvatar}
                <ConversationHeader.Content userName={currentUserName}/>
            </ConversationHeader>}
            <MessageList typingIndicator={getTypingIndicator()}>
                {activeConversation && currentMessages.map((g) => <MessageGroup key={g.id} direction={g.direction}>
                    <MessageGroup.Messages>
                        {g.messages.map((m: ChatMessage<MessageContentType>) => <Message key={m.id} model={{
                            type: "html",
                            payload: m.content,
                            direction: m.direction,
                            position: "normal"
                        }}/>)}
                    </MessageGroup.Messages>
                </MessageGroup>)}
            </MessageList>
            <MessageInput value={currentMessage} onChange={handleChange} onSend={handleSend}
                          disabled={!activeConversation} attachButton={false} placeholder="Type here..."/>
        </ChatContainer>

    </MainContainer>);

}