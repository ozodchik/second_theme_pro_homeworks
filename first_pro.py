import requests
from urllib.parse import urljoin

class Iterable:
   def __init__(self, url):
        get_response = requests.get(url)
        self.lines = get_response.json()
        self.cursor = 0

   def __iter__(self):
      return self

   def __next__(self):
      if self.cursor == len(self.lines):
         raise StopIteration
      number = self.lines[self.cursor]
      self.cursor += 1
      names_countrys = number["name"]["common"].replace(" ", "_")
      links = urljoin("https://en.wikipedia.org/wiki/", names_countrys)
      return f'{names_countrys} - {links}'

if __name__ == "__main__":
    with open("file.txt", "w", encoding="UTF-8") as f:
        res = Iterable("https://raw.githubusercontent.com/mledoze/countries/master/countries.json")
        for name in res:
            f.write(f'{name} \n')