import unittest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import calcagain


class TestCalculator(unittest.TestCase):

    def _float(self, inp, exp_ret, exp_out = None):
        with patch('builtins.input', return_value=inp):
            out_stream = StringIO()
            with redirect_stdout(out_stream):
                val = calcagain.get_float("")
                self.assertEqual(val, exp_ret,
                    f'\nIn get_float(), when I enter "{inp}" I expected {exp_ret} but got {val}')
                if exp_out:
                    out = out_stream.getvalue()
                    self.assertTrue(exp_out.lower() in out.lower(),
                        f'\nIn get_float(), when I enter "{inp}" I expected you to print:\n  "{exp_out}\nbut I saw\n  {out}')

    def test_get_float_enter_float(self):
        self._float('12.34',12.34)
    def test_get_float_enter_int(self):
        self._float('16',16.0)
    def test_get_float_enter_nothing(self):
        self._float('',None,'is not a number')
    def test_get_float_enter_nonsense(self):
        self._float('boom-boom',None,'boom-boom is not a number')

    def _operator(self, inp, exp_ret, exp_out = None):
        with patch('builtins.input', return_value=inp):
            out_stream = StringIO()
            with redirect_stdout(out_stream):
                val = calcagain.get_operator("")
                self.assertEqual(val, exp_ret,
                    f'\nIn get_operator(), when I enter "{inp}" I expected {exp_ret} but got {val}')
                if exp_out:
                    out = out_stream.getvalue()
                    self.assertTrue(exp_out.lower() in out.lower(),
                        f'\nIn get_operator(), when I enter "{inp}" I expected you to print:\n  "{exp_out}\nbut I saw\n  {out}')

    def test_get_operator_enter_plus(self):
        self._operator('+','+')
    def test_get_operator_enter_minus(self):
        self._operator('-','-')
    def test_get_operator_enter_times(self):
        self._operator('x','x')
    def test_get_operator_enter_divide(self):
        self._operator('/','/')
    def test_get_operator_enter_pow(self):
        self._operator('^','^')
    def test_get_operator_enter_nothing(self):
        self._operator('',None,'is not a valid operator')
    def test_get_operator_enter_asterisk(self):
        self._operator('*',None,'* is not a valid operator')
    def test_get_operator_enter_nonsense(self):
        self._operator('jabberwocky',None,'jabberwocky is not a valid operator')

    def _result(self, num1, num2, op, exp_ret):
        val = calcagain.get_result(num1,num2,op)
        self.assertEqual(val, exp_ret,
            f'\nIn get_result(), when I enter pass "{num1}", "{num2}" and "{op}" I expected {exp_ret} but got {val}')

    def test_get_result_addition(self):
        self._result(5,10,'+',15)
    def test_get_result_subtraction(self):
        self._result(5,10,'-',-5)
    def test_get_result_multiplication(self):
        self._result(5,10,'x',50)
    def test_get_result_multiplication_very_big(self):
        self._result(sys.float_info.max,1,'x',sys.float_info.max)
    def test_get_result_division(self):
        self._result(5,10,'/',0.5)
    def test_get_result_division_by_zero(self):
        self._result(5,0,'/',None)
    def test_get_result_pow(self):
        self._result(5,2,'^',25)
    def test_get_result_pow_negative(self):
        self._result(5,-2,'^',1/25)
    def test_get_result_pow_fraction(self):
        self._result(16,1/2,'^',4)
    def test_get_result_pow_too_big(self):
        self._result(12345.0,10000,'^',None)


if __name__ == '__main__':
    unittest.main()
