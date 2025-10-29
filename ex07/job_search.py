from operator import indexOf
import sys
import bs4
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python job_search.py <technology>")
        sys.exit(1)

    # Read technology and build URL
    technology = sys.argv[1]
    url = f"https://www.juniors.ro/jobs?q={technology}"

    # GET request and extract job listings
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        sys.exit(1)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    job_listings = soup.find_all('div', class_='job_header_title', limit=7)
    if not job_listings:
        print("No job listings found.")
        sys.exit(0)

    companies = soup.find_all('ul', class_='job_requirements', limit=21)
    company_names = companies[::3] # Extract every third element -> company names

    for job, company in zip(job_listings, company_names):

        job_title = job.find('h3')
        job_title = job_title.get_text(strip=True) if job_title else "N/A"
        print(f"Job Title: {job_title}")

        date_added = job.find('strong')
        date_added = date_added.get_text(strip=True).split('|')[1].strip() if date_added else "N/A"
        print(f"Date Added: {date_added}")

        location = job.find('strong')
        location = location.get_text(strip=True).split('|')[0].strip() if location else "N/A"
        print(f"Location: {location}")

        tech_stack = job.find('ul', class_='job_tags')
        tech_stack = tech_stack.get_text(separator=' ', strip=True) if tech_stack else "N/A"
        print(f"Tech Stack: {tech_stack}")

        company_name = company.get_text(separator=' ', strip=True).split(' ') if company else []
        if "Companie:" in company_name:
            # Make sure to print the entire company name if more words
            company_name = ' '.join(company_name[(indexOf(company_name, "Companie:") + 1) : indexOf(company_name, "Sursa:")])
            print(f"Company: {company_name}")

        print("-" * 40)