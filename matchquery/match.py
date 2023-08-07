# init 初始化一些常数
import re

import torch
from langchain import OpenAI, LLMChain
from langchain.agents import LLMSingleActionAgent, AgentOutputParser, AgentExecutor, initialize_agent, AgentType
from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.experimental import load_chat_planner, load_agent_executor, PlanAndExecute
from langchain.prompts import StringPromptTemplate
from langchain.retrievers import SelfQueryRetriever
from langchain.schema import Document, AgentAction, AgentFinish
from langchain.vectorstores import Chroma

from matchquery.dbtools import tools
from readconfig.myconfig import MyConfig
from pympler import tracker

config = MyConfig()

# tr = tracker.SummaryTracker()
metadata_field_info = [
    AttributeInfo(
        name="language",
        description="The language used by the character",
        type="string",
    ),
    AttributeInfo(
        name="npcName",
        description="The name of the character",
        type="string",
    ),
    AttributeInfo(
        name="type",
        description="Scenes where the character speak",
        type="string",
    )
]

# llm = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY,openai_api_base= config.OPENAI_BASE_URL)

document_content_description = "All dialogues of game characters"

embedding_model_dict = {
    "text2vec-base": "shibing624/text2vec-base-chinese",
    "MiniLM": "sentence-transformers/all-MiniLM-L6-v2",
    "hinese-macbert": "hfl/chinese-macbert-base"
}

EMBEDDING_DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# 加载嵌入模型 ==============================================================
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_dict['hinese-macbert'],
                                   model_kwargs={'device': EMBEDDING_DEVICE})

# 加载VectorDB =============================================================
vectordb = Chroma(persist_directory="./resource/dict/v4", embedding_function=embeddings)

# 加载VectorDB =============================================================
vectordb_wiki = Chroma(persist_directory="./resource/dict/v1", embedding_function=embeddings)

vectordb_tools = Chroma(persist_directory="./resource/dict/tools", embedding_function=embeddings)


class MatchAnswer:
    role_name: str = None
    llm_questions: [] = []

    def __init__(self, role_name):
        self.role_name = role_name

    def match(self, raw_answer):
        # # 查看内存学习
        # print("查看内存信息")
        # print(tr.print_diff())
        # llm = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY, openai_api_base=config.OPENAI_BASE_URL)
        llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=config.OPENAI_API_KEY,
                     openai_api_base=config.OPENAI_BASE_URL)
        # 加载检索器 ================================================================
        retriever = SelfQueryRetriever.from_llm(
            llm, vectordb, document_content_description, metadata_field_info, verbose=False, enable_limit=True
        )
        # 组合 多查询检索器 和 自我检索器
        # 减少数量优化内存
        template = f"""You are an AI language model assistant. Your task is to generate three 
            different versions of the given user question to retrieve relevant documents from a vector 
            database. By generating multiple perspectives on the user question, your goal is to help
            the user overcome some of the limitations of the distance-based similarity search. 
            Provide these alternative questions seperated by newlines.
            Original question: {raw_answer}"""
        questions = llm.predict(template)
        output_list = questions.split("\n")
        contents = []
        self.llm_questions = output_list
        for i in range(len(output_list)):
            print(output_list[i])
            # 本人看法
            query = f"""whose npcName is {self.role_name} said :```{output_list[i]}```"""
            documents = retriever.get_relevant_documents(query)
            for doc in documents:
                # 去重
                if doc.page_content not in contents:
                    contents.append(doc.page_content)
            # if i == len(output_list) - 1:
            #     row_docs = retriever.get_relevant_documents(raw_answer)
            #     for row_doc in row_docs:
            #         if row_doc.page_content not in contents:
            #             contents.append(row_doc.page_content)

            # retriever.
            # vectordb.
        # print("查看内存信息2")
        # print(tr.print_diff())
        # 在wikipedia 中检索
        return contents

    metadata_wiki_info = [
        AttributeInfo(
            name="theme",
            description="theme of Wiki",
            type="string",
        ),
        AttributeInfo(
            name="source",
            description="Source of Wiki Information",
            type="string",
        ),
        AttributeInfo(
            name="type",
            description="data type",
            type="string",
        )
    ]

    def matchWiki(self, raw_answer):
        llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=config.OPENAI_API_KEY,
                     openai_api_base=config.OPENAI_BASE_URL)
        # 加载检索器 ================================================================
        retriever = SelfQueryRetriever.from_llm(
            llm, vectordb_wiki, document_contents="Some wiki text", metadata_field_info=self.metadata_wiki_info,
            verbose=True, enable_limit=True
        )
        # retriever = vectordb_wiki.as_retriever(search_type="mmr",search_kwargs={"k": 1})
        # querys = self.llm_questions
        querys = ["two wiki about" + self.llm_questions[0] + f""" which theme is {self.role_name}""",
                  "two wiki about" + self.llm_questions[0], "two wiki about " + self.role_name]
        contents = []
        for q in querys:
            documents = retriever.get_relevant_documents(q)
            for doc in documents:
                # 去重
                if doc.page_content not in contents:
                    contents.append(doc.page_content)
        return contents

    def matchTools(self, raw_answer):
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=config.OPENAI_API_KEY,
                         openai_api_base=config.OPENAI_BASE_URL)
        query = f"获取一些基础信息关于{self.role_name}的提问:{raw_answer}"
        # template = f"""You are an artificial intelligence language model assistant. Your task is to generate 3
        # different perspectives of questions in Simplified Chinese based on the information contained in the
        # questions, in order to retrieve relevant background information and answer materials from vectors. Your goal
        # is to help users obtain the background of the chat, the identity and personality of the characters,
        # and the ideas for answering. Provide these alternative questions separated by line breaks.
        # My question: {query}"""
        # questions = llm.predict(template)
        # output_list = questions.split("\n")
        # contents = []
        # ALL_TOOLS = tools
        # retriever = vectordb_tools.as_retriever()
        # def get_tools(raw_answer1):
        #     docs = retriever.get_relevant_documents(raw_answer1)
        #     return [ALL_TOOLS[d.metadata["index"]] for d in docs]

        # planner = load_chat_planner(llm)
        # executor = load_agent_executor(llm, tools, verbose=True)
        # agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)
        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,
                                 handle_parsing_errors="Check your output and make sure it conforms!")
        # agent = initialize_agent(
        #     tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True
        # )
        try:
            result = agent.run(query)
            return result
        except Exception as e:
            print(f"链式分析异常: {e}")
            return None

        # for i in range(len(output_list)):
        #     run = agent.run(output_list[i])
        #     contents.append(run)
        # return contents

        # prompt = CustomPromptTemplate(
        #     template=template,
        #     tools_getter=get_tools,
        #     # This omits the `agent_scratchpad`, `tools`, and `tool_names` variables because those are generated dynamically
        #     # This includes the `intermediate_steps` variable because that is needed
        #     input_variables=["input", "intermediate_steps"],
        # )
        # llm = OpenAI(temperature=0,openai_api_key=config.OPENAI_API_KEY,
        #              openai_api_base=config.OPENAI_BASE_URL)
        # output_parser = CustomOutputParser()
        # # LLM chain consisting of the LLM and a prompt
        # llm_chain = LLMChain(llm=llm, prompt=prompt)
        # tool_names = [tool.name for tool in tools]
        # agent = LLMSingleActionAgent(
        #     llm_chain=llm_chain,
        #     # output_parser=output_parser,
        #     stop=["\nObservation:"],
        #     allowed_tools=tool_names,
        # )
        # agent_executor = AgentExecutor.from_agent_and_tools(
        #     agent=agent, tools=tools, verbose=True
        # )
        # run = agent_executor.run(query)
        # return run


# Set up the base template
template = """Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin! Remember to speak as a pirate when giving your final answer. Use lots of "Arg"s

Question: {input}
{agent_scratchpad}"""

from typing import Callable, Union


# Set up a prompt template
class CustomPromptTemplate(StringPromptTemplate):
    # The template to use
    template: str
    ############## NEW ######################
    # The list of tools available
    tools_getter: Callable

    def format(self, **kwargs) -> str:
        # Get the intermediate steps (AgentAction, Observation tuples)
        # Format them in a particular way
        intermediate_steps = kwargs.pop("intermediate_steps")
        thoughts = ""
        for action, observation in intermediate_steps:
            thoughts += action.log
            thoughts += f"\nObservation: {observation}\nThought: "
        # Set the agent_scratchpad variable to that value
        kwargs["agent_scratchpad"] = thoughts
        ############## NEW ######################
        tools = self.tools_getter(kwargs["input"])
        # Create a tools variable from the list of tools provided
        kwargs["tools"] = "\n".join(
            [f"{tool.name}: {tool.description}" for tool in tools]
        )
        # Create a list of tool names for the tools provided
        kwargs["tool_names"] = ", ".join([tool.name for tool in tools])
        return self.template.format(**kwargs)


class CustomOutputParser(AgentOutputParser):
    def parse(self, llm_output: str) -> Union[AgentAction, AgentFinish]:
        # Check if agent should finish
        if "Final Answer:" in llm_output:
            return AgentFinish(
                # Return values is generally always a dictionary with a single `output` key
                # It is not recommended to try anything else at the moment :)
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output,
            )
        # Parse out the action and action input
        regex = r"Action\s*\d*\s*:(.*?)\nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
        match = re.search(regex, llm_output, re.DOTALL)
        if not match:
            raise ValueError(f"Could not parse LLM output: `{llm_output}`")
        action = match.group(1).strip()
        action_input = match.group(2)
        # Return the action and action input
        return AgentAction(
            tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output
        )


if __name__ == "__main__":
    answer = MatchAnswer("钟离")
    matchs = answer.match("早安")
    print(matchs)

# 你是一个人工智能语言模型助理。你的任务是用简体中文针对提问中包含出的信息生成5个不同角度的提问，以从向量中检索相关背景信息和回答素材，您的目标是帮助用户获取聊天的背景,角色的身份和性格,回答的思路。提供这些用换行符分隔的备选问题。
# 我的问题：
# You are an artificial intelligence language model assistant. Your task is to generate 5 different perspectives of questions in Simplified Chinese based on the information contained in the questions, in order to retrieve relevant background information and answer materials from vectors. Your goal is to help users obtain the background of the chat, the identity and personality of the characters, and the ideas for answering. Provide these alternative questions separated by line breaks.
# My question:
