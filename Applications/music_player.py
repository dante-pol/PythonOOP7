class Track:
    def __init__(self, name, artist, duration, genre):
        self.name = name
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.rating = None

    def play(self):
        print(f"Playing {self.name} by {self.artist}")

    def pause(self):
        print(f"{self.name} paused")

    def stop(self):
        print(f"{self.name} stopped")

    def rate(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
            print(f"You've rated the track {self.rating} stars")
        else:
            print("Rating should be between 1 and 5")


class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, track):
        if isinstance(track, Track):
            self.tracks.append(track)
            print(f"{track.name} added to {self.name}")

    def remove_track(self, track_name):
        for track in self.tracks:
            if track.name == track_name:
                self.tracks.remove(track)
                print(f"{track.name} removed from {self.name}")
                break

    def play(self):
        print(f"Playing {self.name} playlist:")
        for track in self.tracks:
            track.play()


class PlayerSettings:
    def __init__(self):
        self.volume = 5

    def set_volume(self, volume):
        if 0 <= volume <= 10:
            self.volume = volume
            print(f"Volume set to {self.volume}")
        else:
            print("Volume should be between 0 and 10")


if __name__ == "__main__":
    # Пример создания треков
    track1 = Track("Song A", "Artist 1", 3.30, "Pop")
    track2 = Track("Song B", "Artist 2", 4.20, "Rock")

    # Создание плейлиста и добавление треков
    playlist1 = Playlist("My Favourites")
    playlist1.add_track(track1)
    playlist1.add_track(track2)

    # Проигрывание плейлиста
    playlist1.play()

    # Настройка плеера
    settings = PlayerSettings()
    settings.set_volume(7)


