import unittest
import sys
import os
from unittest.mock import patch


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bridge

class TestBridge(unittest.TestCase):

    def test_get_yesno_uses_prompt(self):
        with patch('builtins.input') as mock_input:
            test_prompt = "Enter yes or no:"
            bridge.get_yesno(test_prompt)
            try:
                mock_input.assert_called_once_with(test_prompt)
            except:
                args, kwargs = mock_input.call_args
                actual = str(' '.join(args))
                self.fail(f'''
nWhen I called get_yesno("{test_prompt}") I expected to see:
  {test_prompt}
but instead I saw:
  {actual}
Did you call input(prompt)??''')

    def test_get_num_uses_prompt(self):
        with patch('builtins.input') as mock_input:
            test_prompt = "Enter a number:"
            bridge.get_number(test_prompt)
            try:
                mock_input.assert_called_once_with(test_prompt)
            except:
                args, kwargs = mock_input.call_args
                actual = str(' '.join(args))
                self.fail(f'''
nWhen I called get_yesno("{test_prompt}") I expected to see:
  {test_prompt}
but instead I saw:
  {actual}
Did you call input(prompt)??''')

    def _yesno(self, inp, exp):
        with patch('builtins.input', return_value=inp):
            val = bridge.get_yesno("enter year")
            self.assertEqual(val, exp, f'\nIn get_yesno(), when I enter "{inp}" I expected {exp} but got {val}')

    def test_get_yesno_enter_no(self):
        self._yesno('no',False)
    def test_get_yesno_enter_n(self):
        self._yesno('n',False)
    def test_get_yesno_enter_nothing(self):
        self._yesno('',False)
    def test_get_yesno_enter_nonsense(self):
        self._yesno('goober',False)
    def test_get_yesno_enter_yes(self):
        self._yesno('yes',True)
    def test_get_yesno_enter_y(self):
        self._yesno('y',True)

    def _number(self, inp, exp):
        with patch('builtins.input', return_value=inp):
            val = bridge.get_number("")
            self.assertEqual(val, exp, f'\nIn get_number(), When I enter "{inp}" I expected {exp} but got {val}')
    
    def test_get_number_enter_valid(self):
        self._number('15',15)
    def test_get_number_enter_float(self):
        self._number('15.5',None)
    def test_get_number_enter_nothing(self):
        self._number('',None)
    def test_get_number_enter_nonsense(self):
        self._number('booger',None)


if __name__ == '__main__':
    unittest.main()
