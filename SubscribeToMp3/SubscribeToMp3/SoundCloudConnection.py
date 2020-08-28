import traceback

import soundcloud
from requests import ConnectionError

from DowloadedDB import SubscribeToMp3DB
from SoundCloudDownloader import SoundCloudDownloader


class SoundCloudConnection:
    def __init__(self):
        self.client = soundcloud.Client(
            client_id="1bcd21b153d015e1ad17a960879f1102",
            client_secret="aacf472a0963ed7c70be5d9efd8d243a",
            username="stubbs8@gmail.com",
            password="jontronEgoraptor"
        )

    def getSongsLinksOfArtist(self, artist_id):
        tracksList = self.client.get(r"users/" + artist_id + r"/tracks");
        favourites = self.client.get("users/" + artist_id + "/favorites");
        tracksList += favourites
        trackLinks = map(lambda track: track.fields()['permalink_url'], tracksList)
        return trackLinks


if __name__ == '__main__':
    import subprocess

    import pathlib
    base_path = pathlib.Path(__file__).parent.absolute()
    s = SoundCloudConnection()
    d = SubscribeToMp3DB(songs_path=f'{base_path}\\config\\songs.json', artists_path=f'{base_path}\\config\\artists.json',
                         filters_path=f'{base_path}\\config\\filters.json')
    downloader = SoundCloudDownloader()
    song_links = []
    for artist in d.get_artists():
        try:
            song_links += s.getSongsLinksOfArtist(artist['id'])
        except ConnectionError as e:
            traceback.print_exc()
    downloaded_songs_dict = d.get_songs()
    downloaded_songs_set = set(downloaded_songs_dict.keys())
    new_song_links = list(filter(lambda link: link not in downloaded_songs_set, song_links))
    print("Congrats! Found " + str(len(new_song_links)) + " new songs.")
    i = 0
    for new_song_link in new_song_links:
        try:
            print("downloading " + str(new_song_link) + " ...")
            out = downloader.download(new_song_link, '..\music')
            downloaded_songs_dict[new_song_link] = ""
            print("finished")
            i += 1
        except Exception as e:
            traceback.print_exc()
    d.write_list_to_file(downloaded_songs_dict, d.songs_path)
    print("Added " + str(i) + " new songs. Cool stuff")
