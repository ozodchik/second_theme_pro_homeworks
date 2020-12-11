import requests
from urllib.parse import urljoin


class Iterable:

    def __init__(self, url):
        self.get_response = requests.get(url)
        self.response_json = self.get_response.json()

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration



if __name__ == "__main__":
    with open("file.txt", "w", encoding="UTF-8") as f:
        a = Iterable("https://raw.githubusercontent.com/mledoze/countries/master/countries.json")
        for names in a.response_json:
            country = names["name"]["common"].replace(" ", "_")
            urls = urljoin("https://en.wikipedia.org/wiki/", country)
            f.write(f'{country}-{urls} \n')