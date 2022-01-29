import requests

S = requests.Session()

URL = "https://nerf.fandom.com/api.php"
print("What category would you like to retrieve?")
category = input().strip()

PARAMS = {
    "action": "query",
    "list": "categorymembers",
    "cmtitle": f"Category:{category}",
    "cmlimit": "1000",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
data = R.json()

banned = ["(", "Category:"]

# wow closure
def validate_before_execute(func):
    func() if all(word not in x["title"] for word in banned) else 0

with open("out.txt", "w") as f:
    for x in data["query"]["categorymembers"]:
        # lambda functions allow for easy use
        validate_before_execute(lambda : f.write(f"{x['title'].replace('_', ' ')}\n"))
        validate_before_execute(lambda : print(x["title"].replace("_", " ")))