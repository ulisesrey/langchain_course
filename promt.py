from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    print("Hello LangChain.")

    information = """
Artur Mas i Gavarró (Catalan pronunciation: [əɾˈtuɾ ˈmas]; born 31 January 1956) is a Catalan politician from Spain. He was president of the Government of Catalonia from 2010 to 2015[2] and acting president from September 2015 to 12 January 2016.
Mas is a long time member of Democratic Convergence of Catalonia (CDC by its Catalan acronym) which used to be the bigger of the two component members –along with Unió Democràtica de Catalunya– of what at the time was a long-standing electoral coalition, Convergència i Unió (CiU), a liberal nationalist coalition which had dominated Catalan regional politics since the 1980s.[3] In 2001 Mas was named general secretary of CDC, then, in 2012 he was named president of the party[4] until the party was refounded in July 2016 as PDeCAT, which he presided between July 2016 and January 2018.
From 2003 to 2015, Mas has run five times for the Catalan presidency, four heading the –nowadays defunct– CiU ticket and one running for the novel Junts pel Sí coalition. He attained the presidency in two elections, 2010 and 2012 (both running for CiU) but neither with an absolute majority. In the absence of single party majorities, both tenures were marked by political instability and ended with Mas calling a snap election.
Mas is an economist who obtained his degree from the University of Barcelona, and is fluent in English and French, in addition to Catalan and Spanish.
His ideology tends to be considered liberal from the economic point of view and supportive of Catalan independence. From the social point of view, he has mostly supported a moderate agenda in numerous issues, such as gay rights, but not same-sex marriage[5] and free debate on his party concerning abortion.[6]
In 2010,[citation needed] for the first time, Mas indicated he would vote "Yes" on a hypothetical referendum to secede from Spain. Since then, sovereignty and Catalan independence have become the central part of his political agenda,[7][8] with Mas being instrumental in CDC's novel turn towards separatism. """

    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A short summary
    2. two interesting facts about the person"""

    summary_prompt_template = PromptTemplate(
        input_variables="information",
        template=summary_template,
    )

    llm = ChatOllama(model="llama3.2:latest", temperature=0.0) 

    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})

    print(response)
