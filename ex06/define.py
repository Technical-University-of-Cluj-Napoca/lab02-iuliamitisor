import sys
import bs4 
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python define.py <word>")
        sys.exit(1)

    # Read word and build URL
    word = sys.argv[1]
    url = f"https://dexonline.ro/definitie/{word}"

    # GET request and extract definition by class name
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    definition = soup.find('span', class_='tree-def html').get_text(strip=True)    
    print(definition)
