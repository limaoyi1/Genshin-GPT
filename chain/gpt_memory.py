from langchain import PromptTemplate, OpenAI, LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.memory import RedisChatMessageHistory, ConversationBufferMemory

from chain.custom_redis_messagehistory import MyRedisChatMessageHistory


class GptChain:
    template: str = """You play a role-playing game with a person named Traveler.
This is your Conversation with Traveler:
{chat_history}

{human_input}"""
    openai_api_key: str = None
    openai_base_url: str = None
    session_id: str = None
    redis_url: str = None
    llm_chain: LLMChain = None
    message_history: RedisChatMessageHistory = None
    npcName: str = None

    def __init__(self, openai_api_key, session_id, redis_url, openai_base_url="https://api.openai.com/v1", npc_name ="AI"):
        self.openai_api_key = openai_api_key
        self.session_id = session_id
        self.redis_url = redis_url
        self.openai_base_url = openai_base_url
        self.npcName = npc_name
        self.redis_llm_chain_factory()

    def redis_llm_chain_factory(self):
        """
        已经封装外部尽量不要调用此方法
        Returns:
        """
        message_history = MyRedisChatMessageHistory(
            url=self.redis_url, ttl=600, session_id=self.session_id
        )
        self.message_history = message_history
        memory = ConversationBufferMemory(
            memory_key="chat_history", chat_memory=message_history, ai_prefix=self.npcName, human_prefix="Traveler"
        )
        prompt = PromptTemplate(
            input_variables=["chat_history", "human_input"], template=self.template)
        llm_chain = LLMChain(
            llm=OpenAI(model_name="gpt-3.5-turbo-16k", openai_api_key=self.openai_api_key,
                       openai_api_base=self.openai_base_url, streaming=True,
                       callbacks=[StreamingStdOutCallbackHandler()]),
            prompt=prompt,
            verbose=True,
            memory=memory,
        )
        self.llm_chain = llm_chain

    def predict(self, question):
        return self.llm_chain.predict(human_input=question)

    # def clean(self):
    #     self.llm_chain.

    def clear_redis(self):
        self.message_history.clear()


if __name__ == "__main__":
    chain = GptChain("you key", "1234", "you redis url")
    song = chain.predict(question="Write me a song about sparkling water.")
    # print(song)
