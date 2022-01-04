from unittest import TestCase

from Schema import Schema

class TestSchema(TestCase):

    def test_set_list_implicantFourVariable(self):
        variable = ['a', 'b', 'c', 'd']
        trial1 = ['0--0', '010-', '11--']
        trial2 = ['01-0', '-10-', '1---']
        trial3 = ['---1', '11--', '--00']

        act_trial1 = Schema.SetListImplicantStatic(variable, trial1)
        act_trial2 = Schema.SetListImplicantStatic(variable, trial2)
        act_trial3 = Schema.SetListImplicantStatic(variable, trial3)
        exp_trial1 = [['-a', '-d'], ['-a', 'b', '-c'], ['a', 'b']]
        exp_trial2 = [['-a', 'b', '-d'], ['b', '-c'], ['a']]
        exp_trial3 = [['d'], ['a', 'b'], ['-c', '-d']]

        self.assertEqual(exp_trial1, act_trial1)
        self.assertEqual(exp_trial2, act_trial2)
        self.assertEqual(exp_trial3, act_trial3)

    def test_set_list_implicantFiveVariable(self):
        variable = ['a', 'b', 'c', 'd', 'e']
        trial1 = ['0-1-0', '1010-', '-11--']
        trial2 = ['11111', '00000', '0-1-0']
        trial3 = ['----1', '1----', '0----']

        act_trial1 = Schema.SetListImplicantStatic(variable, trial1)
        act_trial2 = Schema.SetListImplicantStatic(variable, trial2)
        act_trial3 = Schema.SetListImplicantStatic(variable, trial3)
        exp_trial1 = [['-a', 'c', '-e'], ['a', '-b', 'c', '-d'], ['b', 'c']]
        exp_trial2 = [['a', 'b', 'c', 'd', 'e'], ['-a', '-b', '-c', '-d', '-e'], ['-a', 'c', '-e']]
        exp_trial3 = [['e'], ['a'], ['-a']]

        self.assertEqual(exp_trial1, act_trial1)
        self.assertEqual(exp_trial2, act_trial2)
        self.assertEqual(exp_trial3, act_trial3)


    def test_set_list_implicantWrongData(self):
        variable1 = ['a', 'b', 'c', 'd', 'e']
        variable2 = ['a', 'b', 'c', 'd']
        trial1 = ['0-1-', '1010', '-11-']
        trial2 = ['0-1--', '1-010', '--11-']
        trial3 = ['1----', '----1', '000-0']

        act_trial1 = Schema.SetListImplicantStatic(variable1, trial1)
        act_trial2 = Schema.SetListImplicantStatic(variable1, trial2)
        act_trial3 = Schema.SetListImplicantStatic(variable1, trial3)

        act_trial4 = Schema.SetListImplicantStatic(variable2, trial1)
        act_trial5 = Schema.SetListImplicantStatic(variable2, trial2)
        act_trial6 = Schema.SetListImplicantStatic(variable2, trial3)

        exp_trial1 = []
        exp_trial2 = [['-a', 'c'], ['a', '-c', 'd', '-e'], ['c', 'd']]
        exp_trial3 = [['a'], ['e'], ['-a', '-b', '-c', '-e']]
        exp_trial4 = [['-a', 'c'], ['a', '-b', 'c', '-d'], ['b', 'c']]
        exp_trial5 = []
        exp_trial6 = []

        self.assertEqual(exp_trial1, act_trial1)
        self.assertEqual(exp_trial2, act_trial2)
        self.assertEqual(exp_trial3, act_trial3)
        self.assertEqual(exp_trial4, act_trial4)
        self.assertEqual(exp_trial5, act_trial5)
        self.assertEqual(exp_trial6, act_trial6)

