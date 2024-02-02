class Album:
    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def addSongs(self, *args):
        counter = 0
        for song in args:
            in_it = False
            for song2 in self.__songs:
                if compare(song, song2):
                    in_it = True
            if not in_it:
                counter += 1
                self.__songs.append(song)
        return counter

    def sortBy(self, byKey, reverse):
        return sorted(self.__songs, key=byKey(), reverse=reverse)

    def sortByName(self, reverse):
        return self.sortBy(lambda song: song[0], reverse)

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getSongs(self):
        return self.__songs

    def __str__(self):
        songs = ''
        for x in range(len(self.__songs)):
            if x == len(self.__songs) - 1:
                songs += str(self.__songs[x])
            songs += str(self.__songs[x]) + "|"
        return 'Title:' + self.__title + ',' + 'Release year:' + str(
            self.__releaseYear) + ',' + 'songs:' + '{' + songs + '}'


def compare(song1, song2):
    return song1.getTitle() == song2.getTitle() and song1.getReleaseYear() == song2.getYear() and song1.getDuration() == song2.getDuration()
