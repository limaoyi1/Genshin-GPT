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
        self.GptChain = GptChain(openai_api_key=self.config.OPENAI_API_KEY, session_id=session_id,
                                 redis_url=self.config.REDIS_URL)


# ----------------------------------------------------------------
# 生成标题
class GenAnswerOfRole(Gen):
    role_name: str = None
    material: str = None
    query: str = None
    match_answers: [] = None

    def __init__(self, session_id, role_name):
        super().__init__(session_id)
        self.role_name = role_name

    def query_to_role(self, query):
        self.query = query
        self.predict_answer_init()
        self.get_match_answer()
        return self.get_role_answer()

    def predict_answer_init(self):
        text = f"""请你作为{self.role_name}(游戏角色) 简要的回答以下问题:
        Question: {self.query}
        """
        llm1 = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY)
        self.material =llm1.predict(text)

    def get_match_answer(self):
        answer = MatchAnswer(self.role_name)
        self.match_answers = answer.match(self.material)
        print(self.match_answers)

    def get_role_answer(self):
        template = f"""Refer to the speech of this character below, I hope you answer my question using Simplified Chinese as the speaking style of this character.
        Relevant information:
        {self.match_answers}
        Question: {self.query}
        Helpful Answer:"""
        llm = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY)
        return self.GptChain.predict(template)


if __name__ == '__main__':
    # session_id = str(uuid.uuid4())
    session_id ="12345789"
    print(session_id)
    query = "下班吃什么"
    role = "雷电将军"
    title = GenAnswerOfRole(session_id, role)
    answer = title.query_to_role(query)
    print("\n\n\n")
    print("======================")
    print("你\t:" + query)
    print(role + "\t:" + answer)
    print("======================")

# 将一个问题拆分成多个子问题解决,可以大大提高AI对问题的理解,从而提高程序的速度和准确性
