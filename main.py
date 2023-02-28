#################################################
#                                               #
#   ItsBlueTiger2's Anime Characters Scraper    #
#                                               #
#################################################

import re
import requests
from time import perf_counter, sleep


# this script scrapes https://www.anime-planet.com/characters/all using requests and re module
prefix = 'class="name">'
suffix = "</a><div"
urls_to_scrape = []
urls_to_scrape.append("https://www.anime-planet.com/characters/all")
last_page = eval(input("Up to which page (included) do you want to scrape? \n"
                 "Please note that the first page number is 0. \n"
                 "Expected answer: integer number \n"))

for number in range(1, last_page+1):
    urls_to_scrape.append(f"https://www.anime-planet.com/characters/all?page={number}")

def main():
    with open('Characters.txt', 'w', encoding="utf-8") as u:
        for index, page in enumerate(urls_to_scrape):
            print(f"Proceeding page {index}...")
            r = requests.get(page)
            h = r.text
            lines = h.split("\n")
            for line in lines:
                res = re.findall(prefix
                                 + "(.*)"
                                 + suffix, line)
                if res:
                    sleep(0)
                    character = res[0]
                    character = character.replace('&#039;', "'")
                    u.write(character + "\n")

tic = perf_counter() #Program timer start
if __name__ == "__main__":
    main()
toc = perf_counter() #Program timer stop
print(f"It took {toc - tic:0.1f} seconds to finish.")

