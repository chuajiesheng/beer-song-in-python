class BeerSong():
    def __init__(self):
        pass

    def at(self, level):
        base_lyrics = '{} bottles of beer on the wall, {} bottles of beer.' \
                      '\nTake one down and pass it around, {} bottles of beer on the wall.'

        return base_lyrics.format(level, level, level - 1)

    def main(self):
        pass

if __name__ == '__main__':
    BeerSong().main()