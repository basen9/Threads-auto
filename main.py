import requests
from bs4 import BeautifulSoup
import os

AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN")
BASE_ID = os.environ.get("BASE_ID")
TABLE_NAME = os.environ.get("TABLE_NAME")
THREADS_USERNAME = os.environ.get("THREADS_USERNAME")

AIRTABLE_URL = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

HEADERS = {
    "Authorization": f"Bearer {AIRTABLE_TOKEN}",
    "Content-Type": "application/json"
}

def get_followers(username):
    url = f"https://www.threads.net/@{username}"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    try:
        text = soup.find("meta", property="og:description")["content"]
        followers = text.split(" ")[0]
        return followers
    except:
        return "Error"

def update_airtable(username, followers):
    data = {
        "fields": {
            "username": username,
            "followers": followers
        }
    }
    requests.post(AIRTABLE_URL, headers=HEADERS, json=data)

def main():
    print("Running Threads Tracker...")
    usernames = [THREADS_USERNAME]
    for username in usernames:
        followers = get_followers(username)
        print(f"{username}: {followers}")
        update_airtable(username, followers)

main()
