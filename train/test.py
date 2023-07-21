# Build a sample vectorDB
# from langchain.document_loaders import WebBaseLoader

import torch.backends
from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.retrievers import SelfQueryRetriever
from langchain.vectorstores import Chroma

from readconfig.myconfig import MyConfig

config = MyConfig()
embedding_model_dict = {
    # "ernie-base": "models/ernie-3.0-base-zh",
    "text2vec-base": "shibing624/text2vec-base-chinese"
    # "text2vec-large": "models/text2vec-large-chinese",
    # "sentence-transformers-v2": "models/sentence-transformers-v2"
}
EMBEDDING_DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# 加载嵌入模型 ==============================================================
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_dict['text2vec-base'],
                                   model_kwargs={'device': EMBEDDING_DEVICE})
# 加载VectorDB =============================================================
vectordb = Chroma(persist_directory="./../resource/dict/v1", embedding_function=embeddings)

# 多查询检索 =================================================================

from langchain.chat_models import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever

question = "关于璃月的信息"
llm = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY)
retriever_from_llm = MultiQueryRetriever.from_llm(retriever=vectordb.as_retriever(), llm=llm)

# Set logging for the queries
import logging

logging.basicConfig()
logging.getLogger('langchain.retrievers.multi_query').setLevel(logging.INFO)

unique_docs = retriever_from_llm.get_relevant_documents(query=question)
print(unique_docs)
len(unique_docs)

# 自我查询 =====================================================================
# metadata_field_info = [
#     AttributeInfo(
#         name="language",
#         description="The language used by the character",
#         type="string",
#     ),
#     AttributeInfo(
#         name="npcName",
#         description="The name of the character",
#         type="string",
#     ),
#     AttributeInfo(
#         name="type",
#         description="Scenes where the character speak",
#         type="string",
#     )
# ]
# document_content_description="All dialogues of game characters"
#
# retriever = SelfQueryRetriever.from_llm(
#     llm, vectordb, document_content_description, metadata_field_info, verbose=True
# )
#
# documents = retriever.get_relevant_documents("npcName是神里凌华的角色说过什么?")
# for doc in documents:
#     print(doc)
