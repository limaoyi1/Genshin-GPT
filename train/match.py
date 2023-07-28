# init 初始化一些常数
import torch
from langchain import OpenAI
from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.retrievers import SelfQueryRetriever
from langchain.vectorstores import Chroma

from readconfig.myconfig import MyConfig

config = MyConfig()

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
    "MiniLM": "sentence-transformers/all-MiniLM-L6-v2"
}

EMBEDDING_DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# 加载嵌入模型 ==============================================================
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_dict['text2vec-base'],
                                   model_kwargs={'device': EMBEDDING_DEVICE})


class MatchAnswer:
    role_name: str = None

    def __init__(self, role_name):
        self.role_name = role_name

    def match(self, raw_answer):
        # 加载VectorDB =============================================================
        vectordb = Chroma(persist_directory="./resource/dict/v4", embedding_function=embeddings)

        print("初始化了vectordb")
        # llm = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY, openai_api_base=config.OPENAI_BASE_URL)
        llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=config.OPENAI_API_KEY,
                     openai_api_base=config.OPENAI_BASE_URL)
        # 加载检索器 ================================================================
        retriever = SelfQueryRetriever.from_llm(
            llm, vectordb, document_content_description, metadata_field_info, verbose=True, enable_limit=True
        )
        metadata = {
            "npcName": {self.role_name},
            # Add other key-value pairs as needed
        }
        query = f"""npc who 's name is ```{self.role_name}``` 's speak about ```{raw_answer}```"""
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
        for i in range(len(output_list)):
            print(output_list[i])
            # 本人看法
            query = f"""whose npcName is {self.role_name} said :```{output_list[i]}```"""
            documents = retriever.get_relevant_documents(query)
            for doc in documents:
                # 去重
                if doc.page_content not in contents:
                    contents.append(doc.page_content)
        return contents


if __name__ == "__main__":
    answer = MatchAnswer("钟离")
    matchs = answer.match("早安")
    print(matchs)
