from myservice.classes import poll as p
import unittest
 
class TestPoll(unittest.TestCase):
 
    def test_winners(self):
        tested_poll = p.Poll(5, "attempt", ["a", "c", "b"])  
        self.assertEqual(tested_poll.get_winners(), ["a", "c", "b"])
        tested_poll.vote('barney', 'b')
        self.assertEqual(tested_poll.get_winners(), ["b"])
        tested_poll.vote('fred', 'a')
        self.assertEqual(tested_poll.get_winners(), ["a","b"])
 
 
if __name__ == '__main__':
    unittest.main()