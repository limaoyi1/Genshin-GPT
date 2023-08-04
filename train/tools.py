from langchain.document_loaders import WikipediaLoader
from langchain.retrievers import WikipediaRetriever
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.document_loaders import WikipediaLoader
# 维基百科和 谷歌的速度,合法性,价格不能被接受,所以放弃了这种思路
class SearchWikipedia:
    # 获取角色相关信息
    def query_role(self,role):
        wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(lang='zh', top_k_results=1))
        wikipedia.run(f"""原神 {role}""")

    docs = WikipediaLoader(query="原神 钟离", load_max_docs=2).load()
    len(docs)

    def docs_get(self,query):
        retriever = WikipediaRetriever(lang = "zh" , top_k_results=1,load_all_available_meta = True, doc_content_chars_max =100000)
        docs = retriever.get_relevant_documents(query)
        print(docs)  # meta-information of the Document

    def docs_loader(self,query):
        docs = WikipediaLoader(query=query, load_max_docs=1,lang = "zh",load_all_available_meta = True,doc_content_chars_max =100000).load()
        print(docs)


if __name__ == "__main__":
    # answer = MatchAnswer("钟离")
    # matchs = answer.match("早安")
    # print(matchs)
    wikipedia = SearchWikipedia()
    # SearchGoogle("雷电将军","无想的一刀")
    # docs = WikipediaLoader(query="钟离 (原神)", lang= 'zh',load_max_docs=2 ,doc_content_chars_max =10000).load()
    # wikipedia.docs_get("原神")
    wikipedia.docs_loader("原神")
    # print(docs)
    # len(docs)
