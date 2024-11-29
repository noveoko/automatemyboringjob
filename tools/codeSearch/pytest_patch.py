import unittest
from unittest.mock import patch

# The global variable to be mocked
global_variable = 10

def function_using_global_variable():
    return global_variable

class TestMockGlobalVariable(unittest.TestCase):

    @patch('__main__.global_variable', 20)
    def test_function_using_global_variable(self):
        # The global variable is mocked for this test case
        result = function_using_global_variable()
        self.assertEqual(result, 20)

# Run the test
if __name__ == '__main__':
    unittest.main()
