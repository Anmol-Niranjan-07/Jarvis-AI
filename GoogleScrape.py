import aiohttp
import asyncio
from bs4 import BeautifulSoup
from googlesearch import search
import time

async def fetch(session, url):
    try:
        async with session.get(url, timeout=0.5) as response:  # Reduced timeout to 0.5 seconds
            result = await response.text()
    except Exception as e:
        result = ""
    return result

async def scrape_content(session, url):
    try:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'lxml')  # Changed parser to lxml for better performance
        
        # Extract and process the desired content from the HTML using BeautifulSoup
        
        # Example: Extract all the text from the <p> tags
        paragraphs = soup.find_all('p')
        content = [p.get_text() for p in paragraphs]
    except Exception as e:
        content = []
    return content

async def search_and_scrape(query, num_results):
    try:
        search_results = search(query, num_results=num_results)
    except Exception as e:
        search_results = []
    
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_content(session, url) for url in search_results]  # Using list comprehension for better performance
        
        try:
            scraped_content = await asyncio.gather(*tasks)
        except Exception as e:
            scraped_content = []
    return scraped_content

async def main(query):
    
    try:
        scraped_content = await search_and_scrape(query, 2)  # Increased number of results to scrape for better data
    except Exception as e:
        scraped_content = []
    
    # Put all content in a variable
    all_content = '\n'.join(['\n'.join(content) for content in scraped_content])
    # Shorten the all_content to 2000 tokens
    all_content = ' '.join(all_content.split()[:1500])  # Increased token limit for better data
    
    return all_content
    
def scrape(prompt):
    try:
        result = asyncio.run(main(prompt))
    except Exception as e:
        result = ""
    return result
