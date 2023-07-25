import uuid

from langchain.chat_models import ChatOpenAI

from readconfig.myconfig import MyConfig
from chain.gpt_memory import GptChain
from train.match import MatchAnswer

config = MyConfig()


# 抽象父类
class Gen:
    config: MyConfig = None
    GptChain: GptChain = None

    def __init__(self, session_id):
        self.config = MyConfig()
        print(f"open ai key:{self.config.OPENAI_API_KEY}")
        self.GptChain = GptChain(openai_api_key=self.config.OPENAI_API_KEY, openai_base_url= self.config.OPENAI_BASE_URL,session_id=session_id,
                                 redis_url=self.config.REDIS_URL)


# ----------------------------------------------------------------
# 生成标题
class GenAnswerOfRole(Gen):
    role_name: str = None
    material: str = None
    query: str = None
    match_answers: [] = None
    match_query: [] = None

    def __init__(self, session_id, role_name):
        super().__init__(session_id)
        self.match_query = None
        self.role_name = role_name

    def query_to_role(self, query):
        self.query = query
        self.predict_answer_init()
        self.get_match_answer()
        return self.get_role_answer()

    def predict_answer_init(self):
        # 真的有必要在问一遍LLM吗？
        # text = f"""请你作为{self.role_name}(游戏角色) 简要的回答以下问题:
        # Question: {self.query}
        # """
        # llm1 = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY)
        # self.material =llm1.predict(text)
        pass

    def get_match_answer(self):
        answer = MatchAnswer(self.role_name)
        # self.match_answers = answer.match(self.material)
        self.match_answers = answer.match(self.query)
        print(self.match_answers)

    def get_role_answer(self):
        text = ""
        for answer1 in self.match_answers:
            text = text + answer1 + "\n"+"        "
        template = f"""Please refer to records, Answer my questions in the first person as {self.role_name}.
        Try to mimic the character's language style.Don't repeat your answer to the record I gave you.Please answer briefly
        These are some historical records retrieved in the database via vectors:
        {text}
        Question: {self.query}
        {self.role_name}:"""
        llm = ChatOpenAI(temperature=0.4, openai_api_key=config.OPENAI_API_KEY,openai_api_base= config.OPENAI_BASE_URL)
        return self.GptChain.predict(template)


if __name__ == '__main__':
    # session_id = str(uuid.uuid4())
    session_id ="1234578913161"
    print(session_id)
    query = "如何看待剑术"
    role = "神里绫华"
    title = GenAnswerOfRole(session_id, role)
    answer = title.query_to_role(query)
    print("\n\n\n")
    print("======================")
    print("你\t:" + query)
    print(role + "\t:" + answer)
    print("======================")

# 将一个问题拆分成多个子问题解决,可以大大提高AI对问题的理解,从而提高程序的速度和准确性