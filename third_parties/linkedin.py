import os
import requests
from dotnev import load_dotenv

load_dotenv()

def scrape_linkedin_profile(profile_url: str, mock: bool =False):   
    """
    Scrapes a LinkedIn profile for the name, headline, and summary.
    
    Args:
        profile_url (str): The URL of the LinkedIn profile to scrape.
        mock (bool): If True, returns a mock response instead of scraping.

    Returns:
        dict: A dictionary containing the name, headline, and summary of the profile.
    """


    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
        response = requests.get(linkedin_profile_url, timeout=10)
        
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        # Dictionary keys need to be exactly those
        params = {"apikey" : os.getenv("SCRAPIN_API_KEY"),
                  "linkedInUrl" : linkedin_profile_url
                  }
        response = requests.get(api_endpoint, params=params, timeout=10)

    data = response.json().get("person")

    return data


if __name__ == "__main__":
    # Example usage
    profile_url = "https://www.linkedin.com/in/eden-marco/"
    profile_data = scrape_linkedin_profile(profile_url, mock=True)
    print(profile_data)
