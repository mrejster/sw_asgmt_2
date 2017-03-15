import unittest
import piglatin as pl

class TestParseCommandLine(unittest.TestCase):

    #Test in empty input returns nothing.
    def test_noinput(self):
       self.assertEqual(pl.parseCommandLine([]),'')
       self.assertEqual(pl.parseCommandLine(['filename']),'')

    #Test if an inputstring is returned unchanged.
    def test_returnInputString(self):
        self.assertEqual(pl.parseCommandLine(['', 'inputString']),'inputString')

    def test_oneWordTranslate(self):
        self.assertEqual(pl.translateToPig('pig'),'igpay')
        
    def test_onlyConsonantsTranslate(self):
        with self.assertRaises(SystemExit):
           pl.translateWordToPig('bbb')
        
    #Test if Capitalized words remain capitalized efter translation.
    def test_capWordTranslate(self):
        self.assertEqual(pl.translateToPig('Victor'),'Ictorvay')

    def test_oneWordStartsVowelTranslate(self):
        self.assertEqual(pl.translateToPig('eat'),'eatway')
        self.assertEqual(pl.translateToPig('omelet'),'omeletway')
        self.assertEqual(pl.translateToPig('are'),'areway')
        self.assertEqual(pl.translateToPig('egg'),'eggway')
        self.assertEqual(pl.translateToPig('Egg'),'Eggway')
        self.assertEqual(pl.translateToPig('Erik'),'Erikway')

    def test_multipleWordsTranslate(self):
        self.assertEqual(pl.translateToPig('eat omelet'),'eatway omeletway')
        self.assertEqual(pl.translateToPig('Eat egg\neat pig'),'Eatway eggway\neatway igpay')

    def test_punctuation(self):
        self.assertEqual(pl.translateToPig('Test cases: one, two, three.'),'Esttay asescay: oneway, otway, eethray.')
        self.assertEqual(pl.translateToPig('Hello! How is it going?'),'Ellohay! Owhay isway itway oinggay?')

"""
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
"""

#if __name__ == '__main__':
#    unittest.main()
