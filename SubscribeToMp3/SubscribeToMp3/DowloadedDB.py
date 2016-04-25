import json
from unittest import TestCase


class SubscribeToMp3DB():
    def __init__(self, songs_path, filters_path, artists_path):
        self.songs_path = songs_path
        self.filters_path = filters_path
        self.artists_path = artists_path

    def get_songs(self):
        return self.read_all_file(self.songs_path)

    def get_artists(self):
        return self.read_all_file(self.artists_path)

    def get_filters(self):
        return self.read_all_file(self.filters_path)

    @staticmethod
    def read_all_file(path):
        with open(path, mode="r") as f:
            return json.load(f)

    @staticmethod
    def write_list_to_file(list, path):
        with open(path, mode="w") as f:
            json.dump(list, f)


class TestDB(TestCase):
    def test_get_artists_returns_json(self):
        d = SubscribeToMp3DB(songs_path=r'backup\songs.json', artists_path=r'backup\artists.json',
                             filters_path=r'backup\filters.json')
        artists = d.get_artists()
        self.assertNotEqual(d.get_artists(), [])
        self.assertEqual(d.get_filters(), [])
        self.assertNotEqual(d.get_songs(), [])
