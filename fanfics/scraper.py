from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

links = []
filename = "dataset.txt"

f = open(filename, 'w+', encoding="utf-8")

main_links = ["https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87%20%D0%9F%D1%83%D1%82%D0%B8%D0%BD?p=1",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87%20%D0%9F%D1%83%D1%82%D0%B8%D0%BD?p=2",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87%20%D0%9F%D1%83%D1%82%D0%B8%D0%BD?p=3",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87%20%D0%9F%D1%83%D1%82%D0%B8%D0%BD?p=4",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87%20%D0%9F%D1%83%D1%82%D0%B8%D0%BD?p=5",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87%20%D0%9F%D1%83%D1%82%D0%B8%D0%BD?p=6",
              "https://ficbook.net/fanfiction/rpf/v_v_putin",
              "https://ficbook.net/pairings/%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%20%D0%9D%D0%B0%D0%B2%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9?p=1",
              "https://ficbook.net/pairings/%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%20%D0%9D%D0%B0%D0%B2%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9?p=2",
              "https://ficbook.net/pairings/%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%20%D0%9D%D0%B0%D0%B2%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9?p=3",
              "https://ficbook.net/fanfiction/rpf/aleksej_navaljnij",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%C2%AB%D0%92%D0%BE%D0%B2%D0%B0%D0%BD%C2%BB?p=1",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%C2%AB%D0%92%D0%BE%D0%B2%D0%B0%D0%BD%C2%BB?p=2",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%C2%AB%D0%92%D0%BE%D0%B2%D0%B0%D0%BD%C2%BB?p=3",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9?p=1",
              "https://ficbook.net/pairings/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%20%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9?p=2",
              "https://ficbook.net/pairings/%D0%94%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%B4%20%D0%94%D0%B6%D0%BE%D0%BD%20%D0%A2%D1%80%D0%B0%D0%BC%D0%BF",
              "https://ficbook.net/pairings/%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80%20%D0%93%D1%80%D0%B8%D0%B3%D0%BE%D1%80%D1%8C%D0%B5%D0%B2%D0%B8%D1%87%20%D0%9B%D1%83%D0%BA%D0%B0%D1%88%D0%B5%D0%BD%D0%BA%D0%BE%20",
              "https://ficbook.net/pairings/%D0%91%D0%B0%D1%80%D0%B0%D0%BA%20%D0%9E%D0%B1%D0%B0%D0%BC%D0%B0"]


def parse_text(main_link):

    print ('Copied: ' + main_link)

    req = Request(main_link, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    html = page.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    f.write(link + '\n\n')
    # if soup.body.main.h2 is not None:
        # f.write(soup.body.main.h2.get_text() + '\n\n')
    f.write(soup.find("div", {"id": "content"}).get_text() + '\n\n')


def find_part(main_link):

    req = Request(main_link, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    html = page.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    isParted = False
    for link in soup.find_all('a'):
        if link.get('href') is not None and link.get('href').find('part_content') > 0:
            isParted = True
            links.append('https://ficbook.net' + link.get('href'))
            print('Collected: ' + 'https://ficbook.net' + link.get('href'))
    
    if not isParted:
        links.append(main_link)
        print('Collected: ' + main_link)


def parse_search(main_link):

    req = Request(main_link, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    html = page.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a'):
        if link.get('href').find('readfic') > 0:
            find_part('https://ficbook.net' + link.get('href'))


for main_link in main_links:
    parse_search(main_link)

links_without_duplicates = list(set(links))
duplicates_number = len(links) - len (links_without_duplicates)
print("Found " + str(duplicates_number) + " duplicates")

for link in links_without_duplicates:
    parse_text(link)
