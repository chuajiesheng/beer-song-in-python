import unittest
from beer_song import BeerSong


class TestBeerSong(unittest.TestCase):

    def test_print_first(self):
        bs = BeerSong()
        expected = '99 bottles of beer on the wall, 99 bottles of beer.' \
                   '\nTake one down and pass it around, 98 bottles of beer on the wall.'
        self.assertEqual(bs.at(99), expected, 'Level 99 lyrics different')

    def test_print_level_3(self):
        bs = BeerSong()
        expected = '3 bottles of beer on the wall, 3 bottles of beer.' \
                   '\nTake one down and pass it around, 2 bottles of beer on the wall.'
        self.assertEqual(bs.at(3), expected, 'Level 3 lyrics different')

    def test_print_level_2(self):
        bs = BeerSong()
        expected = '2 bottles of beer on the wall, 2 bottles of beer.' \
                   '\nTake one down and pass it around, 1 bottle of beer on the wall.'
        self.assertEqual(bs.at(2), expected, 'Level 2 lyrics different')

    def test_print_level_1(self):
        bs = BeerSong()
        expected = '1 bottle of beer on the wall, 1 bottle of beer.' \
                   '\nTake one down and pass it around, no more bottles of beer on the wall.'
        self.assertEqual(bs.at(1), expected, 'Level 1 lyrics different')

    def test_print_level_0(self):
        bs = BeerSong()
        expected = 'No more bottles of beer on the wall, no more bottles of beer.' \
                   '\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        self.assertEqual(bs.at(0), expected, 'Level 0 lyrics different')

if __name__ == '__main__':
    unittest.main()