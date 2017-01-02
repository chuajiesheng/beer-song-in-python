import unittest
from beer_song import BeerSong


class TestBeerSong(unittest.TestCase):

    def test_print_first(self):
        bs = BeerSong()
        expected = '99 bottles of beer on the wall, 99 bottles of beer.' \
                   '\nTake one down and pass it around, 98 bottles of beer on the wall.'
        self.assertEqual(bs.at(99), expected, 'Level 99 lyrics different')

if __name__ == '__main__':
    unittest.main()