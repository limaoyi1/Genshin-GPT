import datetime
import json
from pathlib import Path

# 编织工具向量库

import torch.backends
from langchain.document_loaders import DirectoryLoader, PyPDFLoader, PyPDFDirectoryLoader, PyMuPDFLoader, \
    PDFMinerPDFasHTMLLoader, TextLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Chroma

from matchquery.dbtools import tools

# 使用 https://github.com/JovenChu/embedding_model_test 的经验

embedding_model_dict = {
    # "ernie-base": "models/ernie-3.0-base-zh",
    "text2vec-base": "shibing624/text2vec-base-chinese"
    # "text2vec-large": "models/text2vec-large-chinese",
    # "sentence-transformers-v2": "models/sentence-transformers-v2"
}

EMBEDDING_DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"


embeddings = HuggingFaceEmbeddings(model_name=embedding_model_dict['text2vec-base'],
                                   model_kwargs={'device': EMBEDDING_DEVICE})

ALL_TOOLS = tools
docs = [
    Document(page_content=t.description, metadata={"index": i})
    for i, t in enumerate(ALL_TOOLS)
]
for doc in docs:
    print(doc)


Chroma.from_documents(docs, embeddings, persist_directory="./../resource/dict/tools")