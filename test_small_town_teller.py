"""
Testing file for non-persistent small town teller
"""

from unittest import TestCase
# TestCase is the class unit test uses to detect tests
import small_town_teller
from small_town_teller import Person, Account, Bank


class TestTeller(TestCase):

    def test_Person(self):
        # given
        expected = []  # the answer
        test_case = [1, 'bob', 'jenkins']  # push through to testing file
        # when
        # this is where to add the actual = test value
        actual = small_town_teller.Person(test_case)
        if actual is not None:
            pass  # i know this is bad, but i am unsure how t
        else:
            self.assertEquals(expected, actual)

    def test_Account(self):
        expected = []  # the answer
        actual = []  # push through to testing file

        self.assertEquals(expected, actual)

    def test_Bank(self):
        expected = []  # the answer
        actual = []  # push through to testing file

        self.assertEquals(expected, actual)
