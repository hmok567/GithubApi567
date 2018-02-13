from HW04 import numCommits, repoList
import unittest

class TestHW04(unittest.TestCase):
    def test_repoList(self):
        self.assertEqual(len(repoList('hmokingbird')), 8, 'Wrong number')
    
    def test_numCommits(self):
        self.assertEqual(numCommits('hmokingbird', 'GoMusicBot'), 26, 'Not correct number of commits')

if __name__ == "__main__":
    print('Running unit tests...')
    unittest.main()