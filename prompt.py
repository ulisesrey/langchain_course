from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_loookup_agent import lookup
from parsers.output_parsers import summary_parser, Summary
from typing import Tuple

# Load environment variables from .env file
load_dotenv()


# def ice_break_with(name: str) -> str:
#     linkedin_username = linkedin_lookup_agent(name=name)
#     linkedin_data =scrape_linkedin_profile(linkedin_profile_url=linkedin_username)


def ice_break_with(name: str) -> Tuple[Summary, str]:
    
    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A short summary
    2. two interesting facts about the person
    
    Use information from Linkedin.
    \n{format_instructions}
    """
    
    
    summary_prompt_template = PromptTemplate(
        input_variables="information",
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()},
    )

    llm = ChatOllama(model="mistral", temperature=0.0) 

    # Create a chain that combines the prompt template with the LLM and an output parser
    chain = summary_prompt_template | llm | summary_parser


    name = "Eden Marco"
    linkedin_url = lookup(name=name)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_url,
        mock=True,  # Set to True to use mock data for testing
    )

    # This "":Summary" is just a type hint    
    response: Summary = chain.invoke(input={"information": linkedin_data})

    return response, linkedin_data.get("photo_url", "")


if __name__ == "__main__":
    print("Hello LangChain.")

    name = "Eden Marco"
    summary, photo_url = ice_break_with(name=name)
    print(summary)
    print(f"Photo URL: {photo_url}")