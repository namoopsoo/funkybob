import unittest
import funkybob

class TestBasic(unittest.TestCase):
    def test_basic(self):
        generator = funkybob.RandomNameGenerator(members=2, separator='-')
        it = iter(generator)
        blah = it.next()

    def test_known_fail_3_members(self):
        generator = funkybob.RandomNameGenerator(members=3, separator='-')
        it = iter(generator)
        blah = it.next()
        
