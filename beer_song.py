class BeerSong():
    FIRST_SENTENCE = '{} of beer on the wall, {} of beer.'
    SECOND_SENTENCE = 'Take one down and pass it around, {} of beer on the wall.'
    BUY_MORE_BEER = 'Go to the store and buy some more, 99 bottles of beer on the wall.'

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

    @staticmethod
    def cap(s):
        return s[0].upper() + s[1:]

    def at(self, level):
        first_sentence = self.FIRST_SENTENCE.format(self.cap(self.bottles(level)), self.bottles(level))
        second_sentence = self.SECOND_SENTENCE.format(self.bottles(level - 1)) if level > 0 else self.BUY_MORE_BEER
        return '\n'.join([first_sentence, second_sentence])

    def main(self):
        pass

if __name__ == '__main__':
    BeerSong().main()