from unittest import TestCase
from ResultEntrance import ResultEntrance


class TestResultEntrance(TestCase):

    # TESTY   GenerateAsText(self)

    def test_GenerateAsText_mix_not(self):
        tmp = [['A', '-B', 'C1', '-D'], ['-A', 'B2', 'C'], ['-B', '-C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsText()
        expect = "Y = A·(B)'·C1·(D)' + (A)'·B2·C + (B)'·(C)'"

        self.assertEqual(expect, actual)

    def test_GenerateAsText_only_not(self):
        tmp = [['-A', '-x12', '-x22', '-y'], ['-A', '-x22', '-C'], ['-x', '-C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsText()
        expect = "Y = (A)'·(x12)'·(x22)'·(y)' + (A)'·(x22)'·(C)' + (x)'·(C)'"

        self.assertEqual(expect, actual)

    def test_GenerateAsText_without_not(self):
        tmp = [['x2', 'x3', 'y1', 'y2'], ['A', 'B', 'C']]

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsText()
        expect = "Y = x2·x3·y1·y2 + A·B·C"

        self.assertEqual(expect, actual)

    def test_GenerateAsText_empty(self):
        tmp = []

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsText()
        expect = None

        self.assertEqual(expect, actual)


    # TESTY   GenerateAsMath(self)

    def test_GenerateAsMath_mix_not(self):

        trial1 = [['A', '-B', 'C', 'D'], ['A', '-B', 'C']]
        act_trial1 = ResultEntrance(trial1).GenerateAsMath()
        exp_trial1 = "$Y = A\\,\\overline{B}\\,C\\,D\\, + A\\,\\overline{B}\\,C\\,$"

        trial2 = [['A', '-A1', 'A3', 'A4'], ['A1', '-A2', 'A4']]
        act_trial2 = ResultEntrance(trial2).GenerateAsMath()
        exp_trial2 = "$Y = A\\,\\overline{A}\\,_{1}\\,A_{3}\\,A_{4} + A_{1}\\,\\overline{A}_{2}\\,A_{4}$"

        trial3 = [['-x1', '-x2', 'x3'], ['x2', 'x3', '-x4']]
        act_trial3 = ResultEntrance(trial3).GenerateAsMath()
        exp_trial3 = "$Y = \\overline{x}_{1}\\overline{x}_{2}x_{3} + x_{2}x_{3}\\bar{x}_{4}$"

        self.assertEqual(exp_trial1, act_trial1)
        self.assertEqual(exp_trial2, act_trial2)
        self.assertEqual(exp_trial3, act_trial3)


    def test_GenerateAsMath_only_not(self):

        trial1 = [['-A', '-B', '-C'], ['-A', '-C']]
        act_trial1 = ResultEntrance(trial1).GenerateAsMath()
        exp_trial1 = "$Y = \\overline{A}\\overline{B}\\overline{C} + \\overline{A}\\overline{C}$"

        trial2 = [['-A1', '-B2', '-C3'], ['-A1', '-C3']]
        act_trial2 = ResultEntrance(trial2).GenerateAsMath()
        exp_trial2 = "$Y = \\overline{A}_{1}\\overline{B}_{2}\\overline{C}_{3} + \\overline{A}_{1}\\overline{C}_{3}$"

        trial3 = [['-x11', '-x12', '-x13'], ['-x12', '-x13']]
        act_trial3 = ResultEntrance(trial3).GenerateAsMath()
        exp_trial3 = "$Y = \\overline{x}_{11}\\overline{x}_{12}\\overline{x}_{13} + \\overline{x}_{12}\\overline{x}_{13}$"

        self.assertEqual(exp_trial1, act_trial1)
        self.assertEqual(exp_trial2, act_trial2)
        self.assertEqual(exp_trial3, act_trial3)


    def test_GenerateAsMath_without_not(self):

        trial1 = [['A', 'B', 'C', 'D'], ['A', 'B', 'C']]
        act_trial1 = ResultEntrance(trial1).GenerateAsMath()
        exp_trial1 = "$Y = ABCD + ABC$"


        trial2 = [['A1', 'B2'], ['D3']]
        act_trial2 = ResultEntrance(trial2).GenerateAsMath()
        exp_trial2 = "$Y = A_{1}B_{2} + D_{3}$"

        trial3 = [['x1', 'x2', 'x3'], ['x', 'x1']]
        act_trial3 = ResultEntrance(trial3).GenerateAsMath()
        exp_trial3 = "$Y = x_{1}x_{2}x_{3} + xx_{1}$"

        self.assertEqual(exp_trial1, act_trial1)
        self.assertEqual(exp_trial2, act_trial2)
        self.assertEqual(exp_trial3, act_trial3)


    def test_GenerateAsMath_empty(self):
        tmp = []

        testObj = ResultEntrance(tmp)
        actual = testObj.GenerateAsMath()
        expect = ''

        self.assertEqual(expect, actual)