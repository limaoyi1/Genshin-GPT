# init 初始化一些常数
import torch
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

llm = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY)

document_content_description = "All dialogues of game characters"

embedding_model_dict = {
    "text2vec-base": "shibing624/text2vec-base-chinese",
    "MiniLM": "sentence-transformers/all-MiniLM-L6-v2"
}

EMBEDDING_DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# 加载嵌入模型 ==============================================================
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_dict['text2vec-base'],
                                   model_kwargs={'device': EMBEDDING_DEVICE})

# 加载VectorDB =============================================================
vectordb = Chroma(persist_directory="./../resource/dict/v4", embedding_function=embeddings)

# 加载检索器 ================================================================
retriever = SelfQueryRetriever.from_llm(
    llm, vectordb, document_content_description, metadata_field_info, verbose=True, enable_limit=True
)

class MatchAnswer:
    role_name: str = None

    def __init__(self, role_name):
        self.role_name = role_name

    def match(self, raw_answer):
        metadata = {
            "npcName": {self.role_name},
            # Add other key-value pairs as needed
        }
        query = f"""npc who 's name is ```{self.role_name}``` 's speak about ```{raw_answer}```"""

        documents = retriever.get_relevant_documents(query=query)
        contents = []
        for doc in documents:
            contents.append(doc.page_content + "\n")
        return contents


if __name__ == "__main__":
    answer = MatchAnswer("钟离")
    matchs = answer.match("早安")
    print(matchs)
