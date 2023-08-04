# Import things that are needed generically
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool

from matchquery.dbmatch import CharacterWrapper
from readconfig.myconfig import MyConfig

config = MyConfig("../")

llm = ChatOpenAI(temperature=0,openai_api_key=config.OPENAI_API_KEY,
                       openai_api_base=config.OPENAI_BASE_URL)

# Load the tool configs that are needed.
search = CharacterWrapper()
llm_math_chain = LLMMathChain(llm=llm, verbose=True)
tools = [
    Tool.from_function(
        func=search.run,
        name="CharacterSearch",
        description="useful for when you need  detailed information about a certain character"
    ),
]

# Construct the agent. We will use the default agent type here.
# See documentation for a full list of options.
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run(
    "纳西妲的cv是谁?"
)