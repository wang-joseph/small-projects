import requests
from bs4 import BeautifulSoup

# getting all the links from the whitehouse statements
# fun learning


def main():
    result = requests.get("https://www.whitehouse.gov/briefings-statements/")
    src = result.content
    soup = BeautifulSoup(src, "lxml")

    urls = []

    for h2Tag in soup.find_all("h2"):
        aTag = h2Tag.find("a")
        urls.append(aTag.attrs["href"])

    print(urls, "\n")

    # print(soup.prettify())
    # print(soup.b)
    # print(soup.find("b")) #same thing as above
    # print(soup.find_all("b")) #returns a list of beautiful soup objects
    # print(soup.b.name)  # print the name

    tag = soup.b
    # tag.name = "blockquote"  # altering the bold content into blockquote
    # print(tag)
    # print(tag["class"]) # get the attribute
    # print(tag.attrs) # all the attributes
    # print(tag.string) # get the string element of the specified element
    # you can also use tag.string.replace_with(replacement) to replace the string with specified replacement

    # You can also delete tags using the 'del' keyword


if __name__ == "__main__":
    main()
