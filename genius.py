import requests
from bs4 import BeautifulSoup

base_url = "https://api.genius.com"
headers = {'Authorization': 'Bearer a4nnZ7TdkUp9PKrdn1t5Ne64PJy5cyKzwZYfXXY__Ls_TMD8HwqumqdpaQCzg4BF'}

song_title = input("What song you tryna find? ")
artist_name = input("Who it be by? ")

def grab_lyrics(song_api_path):
  song_url = base_url + song_api_path
  response = requests.get(song_url, headers=headers)
  json = response.json()
  path = json["response"]["song"]["path"]
  page_url = "https://genius.com" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  [h.extract() for h in html('script')]
  lyrics = html.find("div", class_="lyrics").get_text()
  return lyrics

if __name__ == "__main__":
  search_url = base_url + "/search"
  data = {'q': song_title}
  response = requests.get(search_url, params=data, headers=headers)
  json = response.json()
  song_info = None
  for hit in json["response"]["hits"]:
    if hit["result"]["primary_artist"]["name"] == artist_name:
      song_info = hit
      break
  if song_info:
    song_api_path = song_info["result"]["api_path"]
    print(grab_lyrics(song_api_path))
