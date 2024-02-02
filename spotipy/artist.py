class Artist:
    def __init__(self, firstName, lastName, birthYear, albums, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles

    def mostLikedSong(self):
        maxLikes = self.__singles[0]
        for song in self.__singles:
            if song.getLikes() > maxLikes.getLikes():
                maxLikes = song
        inSingles = maxLikes

        albumSongs = []
        for album in self.__albums:
            for song in album.getSongs():
                albumSongs.append(song)

        mostLikedInAlbums = albumSongs[0]
        for song in albumSongs:
            if song.getLikes() > mostLikedInAlbums.getLikes():
                mostLikedInAlbums = song
        inAlbums = mostLikedInAlbums

        if inSingles.getLikes() > inAlbums.getLikes():
            return inSingles
        else:
            return inAlbums

    def leastLikedSong(self):
        minLikes = self.__singles[0]
        for single in self.__singles:
            if single.getLikes() < minLikes.getLikes():
                minLikes = single
        inSingles = minLikes

        albumSongs = []
        for album in self.__albums:
            for song in album.getSongs():
                albumSongs.append(song)

        leastLikedInAlbums = albumSongs[0]
        for song in albumSongs:
            if song.getLikes() < leastLikedInAlbums.getLikes():
                leastLikedInAlbums = song
        inAlbums = leastLikedInAlbums

        if inSingles.getLikes() < inAlbums.getLikes():
            return inSingles
        else:
            return inAlbums

    def totalLikes(self):
        res = 0
        for single in self.__singles:
            res += single.getLikes()
        for album in self.__albums:
            for song in album.getSongs():
                res += song.getLikes()
        return res

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getBirthYear(self):
        return self.__birthYear

    def getAlbums(self):
        return self.__albums

    def getSingles(self):
        return self.__singles

    def __str__(self):
        return 'Name:' + self.__firstName + ' ' + self.__lastName + ',' + 'Birth year:' + str(self.__birthYear) + ',' + 'Total likes:' + str(self.totalLikes())
