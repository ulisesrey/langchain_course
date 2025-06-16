
from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_urul_tavily(name: str) -> str:
    """
    Looks up a LinkedIn profile by name using Tavily search.
    
    Args:
        name (str): The name of the person to look up.
        
    Returns:
        str: The URL of the LinkedIn profile.
    """
    tavily_search = TavilySearchResults()
    results = tavily_search.invoke(input=name)
    
    # Assuming the first result is the most relevant
    if results and "url" in results[0]:
        return results[0]["url"]
    
    return "Profile not found"