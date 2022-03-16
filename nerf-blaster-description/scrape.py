import requests

S = requests.Session()

URL = "https://nerf.fandom.com/api.php"
print("What nerf gun would you like to see details of?")
gun = input().strip()

PARAMS = {
    "action": "query'",
    "prop": "revisions",
    "titles": gun,
    "rvslots": "*",
    "rvprop": "content",
}

R = S.get(url=URL, params=PARAMS)
print(R.content)

data = R.json()
print(data)


# wow closure
# def validate_before_execute(func):
#     func() if all(word not in x["title"] for word in banned) else 0

# with open("out.txt", "w") as f:
#     f.write(data[])