class BeerSong():
    def __init__(self):
        pass

    @staticmethod
    def bottles(no_of_bottle):
        if no_of_bottle > 1:
            return '{} bottles'.format(no_of_bottle)
        elif no_of_bottle == 1:
            return '1 bottle'
        else:
            return 'no more bottles'

    def at(self, level):
        if level > 0:
            base_lyrics = '{} of beer on the wall, {} of beer.\nTake one down and pass it around, {} of beer on the wall.'
            return base_lyrics.format(self.bottles(level), self.bottles(level), self.bottles(level - 1))
        else:
            base_lyrics = '{} of beer on the wall, {} of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
            no_of_bottles = self.bottles(level)
            return base_lyrics.format(no_of_bottles[0].upper() + no_of_bottles[1:], no_of_bottles)

    def main(self):
        pass

if __name__ == '__main__':
    BeerSong().main()