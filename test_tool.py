import unittest
from tool import gaps
class Tests(unittest.TestCase):
 def test_gaps(self): self.assertEqual(gaps(['2026-01-01T00:00:00','2026-01-01T00:00:10'],5),[1])
if __name__=='__main__': unittest.main()
