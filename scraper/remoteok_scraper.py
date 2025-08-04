import requests
from bs4 import BeautifulSoup

def get_remote_jobs(keyword="python"):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = []

    for div in soup.find_all("tr", class_="job"):
        try:
            title = div.find("h2").text.strip()
            company = div.find("h3").text.strip()
            location = div.find("div", class_="location").text.strip() if div.find("div", class_="location") else "Remote"
            jobs.append({
                "title": title,
                "company": company,
                "location": location
            })
        except:
            continue

    return jobs

if __name__ == "__main__":
    results = get_remote_jobs("python")
    for job in results[:5]:
        print(job)
