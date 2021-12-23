from unittest import TestCase
from ResultEntrance import ResultEntrance


class TestResultEntrance(TestCase):

    def test_PrintAsText1(self):
        tmp = [['A', '-B', 'C', '-D'], ['-A', 'B', 'C'], ['-B', '-C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.printAsText()
        expect = "Y = AB'CD' + A'BC + B'C'"

        self.assertEqual(expect, actual)

    def test_PrintAsText2(self):
        tmp = [['-A', '-B', '-C', '-D'], ['-A', '-B', '-C'], ['-B', '-C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.printAsText()
        expect = "Y = A'B'C'D' + A'B'C' + B'C'"

        self.assertEqual(expect, actual)