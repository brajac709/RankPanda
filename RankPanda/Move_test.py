#!/usr/bin/env python
import unittest

from Move import Move

class TestMove(unittest.TestCase):

    def testSetNumber(self):
        m = Move(0, 4, None, None, None)
        self.assertEquals(m._name, None)
        m.SetNumber(7)
        self.assertEquals(m._number, 7)
        self.assertEquals(m._name, 'Move 7')
    
    #(Brady) Test how it deals with nonstandard names (i.e. not 'Move' + num)
    def testSetNumberName(self):
        m = Move(0, 4, None, None, None)
        m.SetName('Lala')
        self.assertEquals(m._name, 'Lala')
        m.SetNumber(3)
        self.assertEquals(m._number, 3)
        self.assertEquals(m._name, 'Lala')
        

if __name__ == '__main__':
    unittest.main()
