#!/usr/bin/env python
import unittest
import CubicHermiteSpline as CHS

"""Tests for the CubicHermiteSpline module """

class TestSpline(unittest.TestCase):
    
    def testGetLength(self):
        fnlist1 = [[20, 2, -30, (39-2*31/3)], [10, -1, 20, 7]]
        fnlist2 = [[8, -3, 20, 1], [80, 4, 2, 1]]
        self.assertEquals(CHS.GetLengthHelper(fnlist1, 0, 1, 0.001), CHS._GetLengthHelper(fnlist1, 0, 1, 0.001))
        self.assertEquals(CHS.GetLengthHelper(fnlist2, 0, 1, 0.001), CHS._GetLengthHelper(fnlist2, 0, 1, 0.001))
    
	def testGetTVal(self):
	    pass
if __name__ == '__main__':
    unittest.main()