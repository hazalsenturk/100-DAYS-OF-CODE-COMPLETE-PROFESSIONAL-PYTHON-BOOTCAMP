from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup)
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0])for score in soup.find_all(name="span", class_="score")]

index_max = article_upvotes.index(max(article_upvotes))
print(f"{article_texts[index_max]} {article_links[index_max]} {article_upvotes[index_max]}")

print(article_texts)
print(article_links)
print(article_upvotes)















# with open(file="website.html") as file:
#     content = file.read()
#
# #represents the html content
# soup = BeautifulSoup(content, 'html.parser')
# #print(soup.title.string)
# #print(soup.prettify())
# # print(soup.p) #prints the first  paragraph
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# h3_heading = soup.find(name="h3", class_="heading")
# print(h3_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)