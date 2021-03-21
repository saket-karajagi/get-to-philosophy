import requests
import bs4
from bs4 import BeautifulSoup
import urllib
import time
from re import search

class WikipediaTrace:
    def __init__(self, types, number_of_random_links):
        types = types
        self.last_seen = {}
        number_of_random_links = number_of_random_links
        self.max_path = 0

    def get_next_first_url(self, url):
        response = requests.get(url)
        response_text = response.text
        next_first_page = None
        soup = BeautifulSoup(response_text, features='lxml')
        main_text = soup.find(
            id='mw-content-text').find(class_='mw-parser-output')

        for element in main_text.find_all("p", recursive=False):
            d = element.contents
            count = 0
            for ele in range(0, len(d)):
                if '(' in d[ele]:
                    count += 1
                elif ')' in d[ele] and count > 0:
                    count -= 1
                elif '/wiki/' in str(d[ele]) and count == 0:
                    next_first_page = d[ele].get('href')
                    break
                else:
                    continue

            if not next_first_page:
                continue
            else:
                break

        if not next_first_page:
            return

        next_first_url = urllib.parse.urljoin(
            'https://en.wikipedia.org/', next_first_page)

        return next_first_url

    def trace_types(self):
        for _ in range(0, number_of_random_links):
            first_url = 'https://en.wikipedia.org/wiki/Special:Random'
            last_url = 'https://en.wikipedia.org/wiki/Philosophy'

            reached = False
            wiki_tree = [first_url]
            wiki_seen = set()
            step_count = 0

            while not reached:
                next_first_url = self.get_next_first_url(wiki_tree[-1])
                print(next_first_url)
                step_count += 1
                if not next_first_url:
                    self.last_seen[next_first_url] = self.last_seen.get(next_first_url, 0) + 1
                    types['reached dead end'] += 1
                    reached = True
                elif next_first_url == last_url:
                    types['target reached'] += 1
                    if step_count > self.max_path:
                    	self.max_path = step_count
                    reached = True
                elif step_count >= 100:
                    self.last_seen[next_first_url] = self.last_seen.get(next_first_url, 0) + 1
                    types['max steps reached'] += 1
                    reached = True
                elif next_first_url in wiki_seen:
                    self.last_seen[next_first_url] = self.last_seen.get(next_first_url, 0) + 1
                    types['loop'] += 1
                    reached = True
                else:
                    wiki_tree.append(next_first_url)
                    wiki_seen.add(next_first_url)

        return types, self.last_seen, self.max_path

types = {'reached dead end': 0, 
         'target reached': 0, 
         'max steps reached': 0, 
         'loop': 0,}
number_of_random_links = 100
wiki_trace = WikipediaTrace(types, number_of_random_links)
print(wiki_trace.trace_types())