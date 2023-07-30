from langchain.document_loaders import WikipediaLoader
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

class SearchWikipedia:
    # 获取角色相关信息
    def query_role(self,role):
        wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(lang='zh', top_k_results=1))
        wikipedia.run(f"""原神 {role}""")

    docs = WikipediaLoader(query="原神 钟离", load_max_docs=2).load()
    len(docs)


if __name__ == "__main__":
    # answer = MatchAnswer("钟离")
    # matchs = answer.match("早安")
    # print(matchs)
    SearchWikipedia()
    # SearchGoogle("雷电将军","无想的一刀")
    docs = WikipediaLoader(query="钟离 (原神)", lang= 'zh',load_max_docs=2 ,doc_content_chars_max =10000).load()
    print(docs)
    len(docs)
