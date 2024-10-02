# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testCase1(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a right triangle')

    def testCase2(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a right triangle')
        
    def testCase3(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testCase4(self): 
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput','-1,-1,-1 should be invalid')

    def testCase5(self): 
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 should be invalid')

    def testCase6(self): 
        self.assertEqual(classifyTriangle(3,4,0),'InvalidInput','3,4,0 should be invalid')

    def testCase7(self): 
        self.assertEqual(classifyTriangle(3,4,-1),'InvalidInput','3,4,-1 should be invalid')
    
    def testCase8(self): 
        self.assertEqual(classifyTriangle(0,3,4),'InvalidInput','0,3,4 should be invalid')

    def testCase9(self): 
        self.assertEqual(classifyTriangle(-1,3,4),'InvalidInput','-1,3,4 should be invalid')

    def testCase10(self): 
        self.assertEqual(classifyTriangle(3,0,4),'InvalidInput','3,0,4 should be invalid')

    def testCase11(self): 
        self.assertEqual(classifyTriangle(3,-1,4),'InvalidInput','1,1,1 should be invalid')

    def testCase12(self): 
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral','10,10,10 should be equilateral')
    
    def testCase13(self): 
        self.assertEqual(classifyTriangle(5,5,3),'Isosceles','1,1,1 should be isosceles')
    
    def testCase14(self): 
        self.assertEqual(classifyTriangle(10,11,12),'Scalene','1,1,1 should be scalene')

    def testCase15(self): 
        self.assertEqual(classifyTriangle(10,10,150),'NotATriangle','10,10,150 should be invalid')

    def testCase16(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','1,1,1 should be equilateral')

    def testCase17(self): 
        self.assertEqual(classifyTriangle(10,10,15),'Isosceles','1,1,1 should be isosceles')

    def testCase18(self): 
        self.assertEqual(classifyTriangle(10,12,14),'Scalene','1,1,1 should be scalene')

    def testCase19(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Right','1,1,1 should be right')

    def testCase20(self): 
        self.assertEqual(classifyTriangle(1,1,199),'NotATriangle','1,1,201 should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    

