import requests
from bs4 import BeautifulSoup
import time

url = "https://rhccc.ca/?p=".strip()




with open("./index.txt", "w", encoding="utf-8") as f:


    for i in range(0, 10_000):
    # for i in [734]:
        result = requests.get(url+str(i))

        if result.status_code == 404:
            f.write(f"{i}: 404 not found.")
            print(f"nothing found at p={i}")
        elif result.status_code == 200:
            src = result.content
            soup = BeautifulSoup(src, "lxml")

            title = soup.find("meta", property="og:title")
            description = soup.find("meta", property="og:description")
            site_url = soup.find("meta", property="og:url")

            pub_time = soup.find("meta", property="article:published_time")
            auth = soup.find("meta", property="twitter:data1")
    
            f.write("Searching at ?p={i}...\n\n")
            f.write(f"Found url at: {site_url['content']}\n" if site_url else "Found URL, but somehow did not!\n")
            f.write(f"Title: {title['content']}\n" if title else "No title!\n")
            f.write(f"Desc: {description['content']}\n" if description else "No desc!\n")
            f.write(f"Pub. date: {pub_time['content']}\n" if pub_time else "No pub date!\n")
            f.write(f"Author: {title['content']}\n" if auth else "No author!\n")
            f.write("\n\n")

            print(f"Found something at p={i}")
        
        time.sleep(1)
       