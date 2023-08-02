import torch
from langchain.agents import create_vectorstore_router_agent
from langchain.agents.agent_toolkits import VectorStoreInfo, VectorStoreRouterToolkit
from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

from readconfig.myconfig import MyConfig

config = MyConfig()
print(config.OPENAI_API_KEY)

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

llm = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY,openai_api_base= config.OPENAI_BASE_URL)

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
speak_vectordb = Chroma(persist_directory="./resource/dict/v4", embedding_function=embeddings)

# 加载VectorDB =============================================================
wiki_vectordb = Chroma(persist_directory="./resource/dict/v1", embedding_function=embeddings)

speak_vectordb_info = VectorStoreInfo(
    name="speak",
    description="All the words of the characters",
    vectorstore=speak_vectordb,
)
wiki_vectordb_info = VectorStoreInfo(
    name="wiki",
    description="the wikis about the characters",
    vectorstore=wiki_vectordb,
)

router_toolkit = VectorStoreRouterToolkit(
    vectorstores=[speak_vectordb_info, wiki_vectordb_info], llm=llm
)
agent_executor = create_vectorstore_router_agent(
    llm=llm, toolkit=router_toolkit, verbose=True
)
agent_executor.run(
    "Help me find works and speaks about '钟离'?"
)
