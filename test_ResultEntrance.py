from unittest import TestCase
from ResultEntrance import ResultEntrance


class TestResultEntrance(TestCase):

    def test_GenerateAsText_mix_not(self):
        tmp = [['A', '-B', 'C', '-D'], ['-A', 'B', 'C'], ['-B', '-C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsText()
        expect = "Y = AB'CD' + A'BC + B'C'"

        self.assertEqual(expect, actual)

    def test_GenerateAsText_only_not(self):
        tmp = [['-A', '-B', '-C', '-D'], ['-A', '-B', '-C'], ['-B', '-C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsText()
        expect = "Y = A'B'C'D' + A'B'C' + B'C'"

        self.assertEqual(expect, actual)

    def test_GenerateAsText_without_not(self):
        tmp = [['A', 'B', 'C', 'D'], ['A', 'B', 'C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsText()
        expect = "Y = ABCD + ABC"

        self.assertEqual(expect, actual)

    def test_GenerateAsText_empty(self):
        tmp = []

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsText()
        expect = None

        self.assertEqual(expect, actual)

    def test_GenerateAsMath_mix_not(self):
        tmp = [['A', '-B', 'C', 'D'], ['A', '-B', 'C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsMath()
        expect = "$Y = A\\bar{B}CD + A\\bar{B}C$"

        self.assertEqual(expect, actual)

    def test_GenerateAsMath_only_not(self):
        tmp = [['-A', '-B', '-C'], ['-A', '-C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsMath()
        expect = "$Y = \\bar{A}\\bar{B}\\bar{C} + \\bar{A}\\bar{C}$"

        self.assertEqual(expect, actual)

    def test_GenerateAsMath_without_not(self):
        trial1 = [['A', 'B', 'C', 'D'], ['A', 'B', 'C']]
        trial2 = [['A', 'B'], ['D']]
        trial3 = [['A', 'B', 'D'], ['D', 'E']]

        act_trial1 = ResultEntrance(trial1).GenerateAsMath()
        act_trial2 = ResultEntrance(trial2).GenerateAsMath()
        act_trial3 = ResultEntrance(trial3).GenerateAsMath()

        exp_trial1 = "$Y = ABCD + ABC$"
        exp_trial2 = "$Y = AB + D$"
        exp_trial3 = "$Y = ABD + DE$"

        self.assertEqual(exp_trial1, act_trial1)
        self.assertEqual(exp_trial2, act_trial2)
        self.assertEqual(exp_trial3, act_trial3)

    def test_GenerateAsMath_empty(self):
        tmp = []

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsMath()
        expect = None

        self.assertEqual(expect, actual)