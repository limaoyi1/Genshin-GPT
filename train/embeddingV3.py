import json
from pathlib import Path

import torch.backends
from langchain.document_loaders import DirectoryLoader, PyPDFLoader, PyPDFDirectoryLoader, PyMuPDFLoader, \
    PDFMinerPDFasHTMLLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Chroma

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

text_loader_kwargs={'autodetect_encoding': True}

loader1 = PyMuPDFLoader("../resource/pdf_files/八重神子.pdf")
docs1 = loader1.load()
print(docs1)
loader = PyPDFDirectoryLoader('../resource/pdf_files')
loader3 = PDFMinerPDFasHTMLLoader("../resource/pdf_files/八重神子.pdf")
docs3 = loader3.load()
print(docs3)
# loader = DirectoryLoader('../resource/pdf_files', glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True, loader_kwargs=text_loader_kwargs)
docs = loader.load()
print(len(docs))
for doc in docs:
    print(doc)

# for each in json_data:
#     if each.get('text', '') == '' or each.get('text', '') == '...':
#         continue
#     doc = Document(page_content=each.get('npcName', '') + ":\"" + each.get('text', '')+"\"",
#                    metadata={"language": each.get('language', ''), "npcName": each.get('npcName', ''),
#                              "type": each.get('type', '')})
#     docs.append(doc)
# print("start")
#
# # # pprint(data)
# vectorstore = Chroma.from_documents(docs, embeddings, persist_directory="./../resource/dict/v6")



print("exit")
