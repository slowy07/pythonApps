import requests
import webbrowser


pageCount = 10
url = (
    "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit="
    + str(pageCount)
    + "&format=json"
)


def load():
    response = requests.get(url)
    if response.ok:
        jsonData = response.json()["query"]["random"]
        print("10 random generate wiki pages")
        for idx, j in enumerate(jsonData):
            print(str(idx) + ": ", j["title"])

        i = input("wich page want to see[R :retry / n: exit]: ")
        if i == "r" and i == "R":
            print("generate random page wiki ")
        elif i == "n" and i == "N":
            print("exiting program ")
        else:
            try:
                jsonData[int(i)]["id"]
            except Exception:
                raise Exception("wrong input")
            print("taking to the browser")
            webbrowser.get().open(
                "https://en.wikipedia.org/wiki?curid=" + str(jsonData[int(i)]["id"])
            )
        load()
    else:
        response.raise_for_status()


if __name__ == "__main__":
    load()
