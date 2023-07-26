import torch
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from readconfig.myconfig import MyConfig

# 全局的常量初始化
config = MyConfig()
EMBEDDING_DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# 加载嵌入模型 ==============================================================
embedding_model_dict = {
    "text2vec-base": "shibing624/text2vec-base-chinese",
    "MiniLM": "sentence-transformers/all-MiniLM-L6-v2"
}

embeddings = HuggingFaceEmbeddings(model_name=embedding_model_dict['text2vec-base'],
                                   model_kwargs={'device': EMBEDDING_DEVICE})

# 加载VectorDB =============================================================
vectordb = Chroma(persist_directory="./resource/dict/v4", embedding_function=embeddings)

print("扫描到我了？")