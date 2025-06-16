import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import Tool
from langchain.agents.react.agent import create_react_agent
from langchain.agents.agent import AgentExecutor
from langchain import hub
# from third_parties.linkedin import scrape_linkedin_profile
from tools.tools import get_profile_urul_tavily

# Load environment variables from .env file
load_dotenv()


def lookup(name: str) -> str:
    """
    Looks up a LinkedIn profile by name.
    Args:
        name (str): The name of the person to look up.
    Returns:
        str: The URL of the LinkedIn profile.
    """
    llm = ChatOllama(model="deepseek-r1:8b", temperature=0.0)

    template = """
    Given the name {name}, find the LinkedIn profile URL of the person.
    The answer should contain only the URL.
    """

    prompt_template = PromptTemplate(template=template, input_variables=["name"])

    tools_for_agent = [
        Tool(
            name="Find LinkedIn Profile URL",
            func=get_profile_urul_tavily,
            description="Useful for when you need to get the LinkedIn page URL" # Very important
        )]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        prompt=react_prompt,
        tools=tools_for_agent,
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={
            "input": prompt_template.format(name=name)
            }
    )
            
    linkedin_profile_url = result["output"]

    return linkedin_profile_url


if __name__ == "__main__":
    name = "Eden Marco"
    linkedin_profile_url = lookup(name)
    print(f"LinkedIn profile URL for {name}: {linkedin_profile_url}")
    
    # Uncomment to use the scrape function
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url, mock=True)
    # print(linkedin_data)