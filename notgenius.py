import requests
from bs4 import BeautifulSoup

base_url = "https://api.genius.com/"
headers = {'Authorization': 'Bearer a4nnZ7TdkUp9PKrdn1t5Ne64PJy5cyKzwZYfXXY__Ls_TMD8HwqumqdpaQCzg4BF'}

song_title = "Lake Song"
artist_name = "The Decemberists"



song_url = "https://api.genius.com/songs/378195"
response = requests.get(song_url, headers=headers)
json = response.json()
path = json["response"]["song"]["path"]

page_url = "http://genius.com" + path
page = requests.get(page_url)
html = BeautifulSoup(page.text, "html.parser")

[h.extract() for h in html('script')]

lyrics = html.find("div", class_ = "lyrics").get_text()
print(lyrics)

search_url = base_url + "search"
data = {'q': song_title}
response = requests.get(search_url, params=data, headers=headers)
json = response.json()
song_info = None

print(json)
