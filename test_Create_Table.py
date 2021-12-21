from unittest import TestCase
import pandas as pd

from Create_Table import CreateTable


class TestCreateTable(TestCase):

    def setUp(self):
        self.table = CreateTable()

    def test_correct_value(self):
        var1 = '1,2,3'
        var2 = '4,9,11'
        df = CreateTable(var1, var2).get_df()
        actual = df['Liczba Dziesiętna'].tolist()
        actual.sort()
        expect = [1, 2, 3, 4, 9, 11]
        self.assertEqual(expect, actual)

    def test_few_value(self):
        var1 = '1,2,3'
        df = CreateTable(var1).get_df()
        actual = df['Liczba Binarna'].tolist()
        print(actual)
        actual.sort()
        expect = ['0001', '0010', '0011']
        self.assertEqual(expect, actual)


    def test_with_incorrect_value(self):
        var1 = '1,d,3'
        var2 = '4,e,11'
        df = CreateTable(var1, var2).get_df()
        actual = df['Liczba Dziesiętna'].tolist()
        actual.sort()
        expect = [1, 3, 4, 11]
        self.assertEqual(expect, actual)


    def test_white_value(self):
        var1 = '1 2 3 5 7'
        var2 = '4 9 12'
        df = CreateTable(var1, var2).get_df()
        actual = df['Liczba Dziesiętna'].tolist()
        actual.sort()
        expect = [1, 2, 3, 4, 5, 7, 9, 12]
        self.assertEqual(expect, actual)


    def test_duplicate_value(self):
        var1 = '1 2 4 5 9'
        var2 = '1 9 12 3'
        df = CreateTable(var1, var2).get_df()
        actual = df['Liczba Dziesiętna'].tolist()
        actual.sort()
        expect = [1, 2, 3, 4, 5, 9, 12]
        self.assertEqual(expect, actual)

    def test_onlyMinterm_value(self):
        var1 = '1 2 4 5 9'
        var2 = ''
        df = CreateTable(var1, var2).get_df()
        actual = df['Liczba Dziesiętna'].tolist()
        actual.sort()
        expect = [1, 2, 4, 5, 9]
        self.assertEqual(expect, actual)

    def test_onlyDontCare_value(self):
        var1 = ''
        var2 = '1, 2, 3, 4'
        df = CreateTable(var1, var2).get_df()
        actual = df['Liczba Dziesiętna'].tolist()
        actual.sort()
        expect = [1, 2, 3, 4]
        self.assertEqual(expect, actual)

    def test_mix_value(self):
        var1 = '1-2-4-5-9-12-x'
        var2 = 'y-4-7-0'
        df = CreateTable(var1, var2).get_df()
        actual = df['Liczba Dziesiętna'].tolist()
        actual.sort()
        expect = [0, 1, 2, 4, 5, 7, 9, 12]
        self.assertEqual(expect, actual)

    def test_wrong_value(self):
        var1 = 'xds'
        var2 = 'asd'
        df = CreateTable(var1, var2).get_df()
        print(df)
        actual = df['Liczba Dziesiętna'].tolist()
        actual.sort()
        expect = []
        self.assertEqual(expect, actual)
