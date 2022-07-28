"""
Testing file for non-persistent small town teller
"""

from unittest import TestCase
# TestCase is the class unit test uses to detect tests
from small_town_teller import Person, Account, Bank


class TestTeller(TestCase):

    def setUp(self) -> None:
        # this is used to stage or set up test data
        #
        self.test_data = ['Bob', 1001, 'Smith']

    def test_Person(self):
        expected = []  # the answer
        actual = []  # push through to testing file

        self.assertEquals(expected, actual)

    def test_Account(self):
        expected = []  # the answer
        actual = Person('jj')  # push through to testing file

        self.assertEquals(expected, actual)

    def test_Bank(self):
        expected = []  # the answer
        actual = []  # push through to testing file

        self.assertEquals(expected, actual)

    def test_Persistence(self):
        expected = []
        actual = []

        self.assertEquals(expected, actual)
