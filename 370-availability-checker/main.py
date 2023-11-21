import requests
from bs4 import BeautifulSoup
import smtplib
import os
import time
from dotenv import load_dotenv

load_dotenv()

print("Starting the script with email", os.getenv("EMAIL"), "and destination email", os.getenv("DEST_EMAIL"))

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
  
    server.login(os.getenv("EMAIL"), os.getenv("EMAIL_PASSWORD"))
  
    subject = "370 JUST OPENED A CLASS!"
    body = "GO GO GO https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL."
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(os.getenv("EMAIL"), os.getenv("DEST_EMAIL"), message)
  
    server.quit()

def main():
    shouldRun = True
    url = "https://classes.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1239&subject=CS&cournum=370"

    while shouldRun:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
        
                # Find the specific row with time "02:30-03:50"
                rows = soup.find_all('tr')
                for row in rows:
                    if "02:30-03:50" in str(row):
                        # Count occurrences of "81" in this row
                        count = str(row).count("81")
                        if count < 2:
                            print("IT WAS FOUND IT WAS FOUND IT WAS FOUND")
                            shouldRun = False
                            send_email()
                        else:
                            print("nothing out of the ordinary...")
                        break

            else:
                print(f"Failed to get data: {response.status_code}")

        except requests.RequestException as e:
            print(f"An error occurred: {e}")

        time.sleep(60)  # Wait for 60 seconds before the next request

if __name__ == "__main__":
    main()
