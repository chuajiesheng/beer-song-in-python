class BeerSong():
    def __init__(self):
        pass

    def bottles(self, number_of_bottles):
        if number_of_bottles > 1:
            return '{} bottles'.format(number_of_bottles)
        elif number_of_bottles == 1:
            return '1 bottle'

    def at(self, level):
        base_lyrics = '{} of beer on the wall, {} of beer.\nTake one down and pass it around, {} of beer on the wall.'
        return base_lyrics.format(self.bottles(level), self.bottles(level), self.bottles(level - 1))

    def main(self):
        pass

if __name__ == '__main__':
    BeerSong().main()