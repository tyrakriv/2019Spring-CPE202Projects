# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):

    #Tests a normal input with two operands and one operator
    def test_postfix_eval_01(self):
##        self.assertEqual(infix_to_postfix("( 3 + 2 ) + 8 / 3 * 17 - ( 12 / 4.2 / 1.2 - 8 * 6 ) "),0)
        self.assertAlmostEqual(postfix_eval("3 5 + "), 8)

    #Tests for an invalid token error with letters
    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    #Tests for insufficient operands
    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    #Tests for too many operands
    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    #Tests with subtraction
    def test_postfix_eval_05(self):
        self.assertAlmostEqual(postfix_eval("5 3 - "), 2)

    #Tests for multiplication
    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval("3 5 * "), 15)

    #Tests for exponential
    def test_postfix_eval_07(self):
        self.assertAlmostEqual(postfix_eval("5 3 ** "), 125)

    #Tests for division of zero
    def test_postfix_eval_08(self):
        self.assertAlmostEqual(postfix_eval("0 5 / "), 0)

    #Tests for value error when a value is divided by zero
    def test_postfix_eval_09(self):
        with self.assertRaises(ValueError):
            postfix_eval("3 0 / ") 

    #Tests for illegal shift operator with integers
    def test_postfix_eval_10(self):
        try:
            postfix_eval("3 3 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    #Tests for illegal shift operator with floats
    def test_postfix_eval_11(self):
        try:
            postfix_eval("3 0.2 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    #Tests for bit shifts
    def test_postfix_eval_12(self):
        self.assertEqual(postfix_eval("20 4 >>"),1)
        
    def test_postfix_eval_13(self):
        self.assertEqual(postfix_eval('-2 5 <<'), -64)

    #Tests infix to postfix function with subtraction and extra spaces
    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 -      3"), "6 3 -")

    #Tests with one number
    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("6"), "6")

    #Tests with large input string
    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix("2 ** ( 3 / 5 )"), "2 3 5 / **")

    #Tests with large input string
    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix(" 3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    #Tests subtraction and exponential
    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix("2 - 3  ** 5"), "2 3 5 ** -")

    #Tests bit shift operand
    def test_infix_to_postfix_06(self):
        self.assertEqual(infix_to_postfix("20 >> 4 **"), "20 4 >> **")
        

    #Tests all coverage of prefix to postfix function
    def test_prefix_to_postfix_01(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    #Tests all coverage of prefix to postfix function
    def test_prefix_to_postfix_02(self):
        self.assertEqual(prefix_to_postfix("- + 4 5 * 1 8"), "4 5 + 1 8 * -")


if __name__ == "__main__":
    unittest.main()
