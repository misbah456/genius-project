import requests

CLIENT_ACCESS_TOKEN = "a4nnZ7TdkUp9PKrdn1t5Ne64PJy5cyKzwZYfXXY__Ls_TMD8HwqumqdpaQCzg4BF"

BASE_URI = "https://api.genius.com"

def _get(path, params=None, headers=None):

    url = '/'.join([BASE_URI, path])

    token = "Bearer {}".format(CLIENT_ACCESS_TOKEN)

    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    response = requests.get(url=url, params=params, headers=headers)
    response.raise_for_status()

    return response.json()

def get_artist_songs(artist_id):

    current_page = 1
    next_page = True
    songs = []

    while next_page:

        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page}
        data = _get(path=path, params=params)

        page_songs = data['response']['songs']

        if page_songs:
            songs += page_songs
            current_page += 1
        else:
            next_page = False

def scrape_lyrics(url):

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    lyrics = soup.find(name="lyrics")
    lyrics.script.decompose()

    lyrics_text = " / ".join([lyric for lyric in lyrics.stripped_strings])
    return lyrics_text

get_artist_songs("16775")
