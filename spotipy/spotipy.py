class SpotiPy:
    def __init__(self):
        self.__artists = []

    @classmethod
    def loadFromFile(cls, path):
        pass

    def getArtists(self):
        return self.__artists

    def addArtists(self, *args):
        for newArtist in args:
            in_it = False
            for artist in self.__artists:
                if newArtist.getFirstName() == artist.getFirstName() and newArtist.getLastName() == artist.getLastName() and newArtist.getBirthYear() == artist.getBirthYear():
                    in_it = True
            if not in_it:
                self.__artists.append(newArtist)

    def getTopTrendingArtist(self):
        topArtist = self.__artists[0]
        for x in self.__artists:
            if x.totalLikes() > topArtist.totalLikes():
                topArtist = x
        return topArtist.getFirstName(), topArtist.getLastName()

    def getTopTrendingAlbum(self):
        albums = {}
        for artist in self.__artists:
            for album in artist.getAlbums():
                albums[album] = albumLikes(album)
        return max(albums, key=albums.get)

    def getTopTrendingSong(self):
        topSong = self.__artists[0].mostLikedSong()
        for artist in self.__artists:
            if artist.mostLikedSong().getLikes() > topSong.getLikes():
                topSong = artist.mostLikedSong()
        return topSong


def albumLikes(album):
    likes = 0
    for song in album.getSongs():
        likes += song.getLikes()
    return likes
