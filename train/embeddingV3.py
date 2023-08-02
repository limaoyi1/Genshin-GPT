import datetime
import json
from pathlib import Path

import torch.backends
from langchain.document_loaders import DirectoryLoader, PyPDFLoader, PyPDFDirectoryLoader, PyMuPDFLoader, \
    PDFMinerPDFasHTMLLoader, TextLoader
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


from opencc import OpenCC

def traditional_to_simplified(traditional_text):
    # 创建一个繁体到简体的转换器
    cc = OpenCC('t2s')  # 't2s' 表示从繁体转换为简体

    # 调用convert方法进行转换
    simplified_text = cc.convert(traditional_text)

    return simplified_text
text_loader_kwargs={'autodetect_encoding': True}
# 放弃维基百科的数据
# loader2 = DirectoryLoader('../resource/wiki', glob="**/*.md", loader_cls=TextLoader,loader_kwargs=text_loader_kwargs)
loader1 = DirectoryLoader('../resource/bilibili', glob="**/*.md", loader_cls=TextLoader,loader_kwargs=text_loader_kwargs)
docs1 = loader1.load()
# docs2 = loader2.load()
docs = docs1



from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size =200,
    chunk_overlap = 50,
    length_function = len,
)
# 拆分文本
texts = text_splitter.split_documents(docs)
for doc in texts:
    doc.page_content = traditional_to_simplified(doc.page_content.replace("\n"," "))
    simplified = traditional_to_simplified(doc.metadata.get('source'))
    doc.metadata.__setitem__('source',simplified)
    doc.metadata.__setitem__('theme', simplified.replace("..\\resource\\wiki\\","").replace("..\\resource\\bilibili\\","").replace(".md",""))
    doc.metadata.__setitem__('type', 'wiki')
    print(doc)
print(len(texts))

# 开炉炼丹 =============================================================================================================
current_time = datetime.datetime.now().time()
print("开始时间：", current_time)


vectorstore_wiki = Chroma.from_documents(texts, embeddings, persist_directory="./../resource/dict/v1")


current_time = datetime.datetime.now().time()
print("结束时间：", current_time)



print("exit")
