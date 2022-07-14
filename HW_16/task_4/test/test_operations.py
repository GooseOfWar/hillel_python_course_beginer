"""
Test cases
"""
# --max-line-length=120


from unittest import TestCase, main

from HW_16.task_4 import exchanger, utils  # pylint: disable=import-error

user_input = exchanger.i_o_operator
operator = utils.Operator


class UtilsTest(TestCase):
    """Utils module tests"""

    def test_wrong_path(self):
        """Test case: wrong path"""
        utils.PATH = 'A'
        case = operator()
        result = case.status('rate')
        self.assertEqual(result, 'File Not Found')


class IOTests(TestCase):
    """Input/output tests"""

    def test_course_1(self):
        """Test case: one arg"""
        command: str = 'COURSE'
        result = user_input(command)
        self.assertEqual(result, 'INVALID COMMAND COURSE')

    def test_course_2(self):
        """Test case: one wrong arg"""
        command: str = 'wrong'
        result = user_input(command)
        self.assertEqual(result, 'INVALID COMMAND wrong')

    def test_course_3(self):
        """Test case: 3 arg"""
        command: str = 'COURSE UAH 500'
        result = user_input(command)
        self.assertEqual(result, 'INVALID COMMAND COURSE UAH 500')

    def test_course_4(self):
        """Test case: wrong currency"""
        command: str = 'COURSE ZLT'
        result = user_input(command)
        self.assertEqual(result, 'INVALID CURRENCY ZLT')

    def test_exchange_1(self):
        """Test case: unavailable sum"""
        utils.PATH = r'C:\Users\Capibara\Documents\GitHub\hillel_python_course_beginer\HW_16\task_4\db.json'
        command: str = 'EXCHANGE USD 5000000000000'
        result = user_input(command)
        self.assertIn('UNAVAILABLE', result)

    def test_exchange_2(self):
        """Test case: wrong data"""
        utils.PATH = r'C:\Users\Capibara\Documents\GitHub\hillel_python_course_beginer\HW_16\task_4\db.json'
        command: str = 'EXCHANGE CMD 15'
        result = user_input(command)
        self.assertEqual(result, 'INVALID CURRENCY CMD')

    def test_exchange_3(self):
        """Test case: zero case"""
        utils.PATH = r'C:\Users\Capibara\Documents\GitHub\hillel_python_course_beginer\HW_16\task_4\db.json'
        command: str = 'EXCHANGE USD 0'
        result = user_input(command)
        self.assertEqual(result, 'USD 0.0, RATE 27.5')

    def test_exchange_4(self):
        """Test case: empty command"""
        command: str = 'EXCHANGE'
        result = user_input(command)
        self.assertEqual(result, 'INVALID COMMAND EXCHANGE')

    def test_exchange_5(self):
        """Test case: not a number"""
        command: str = 'EXCHANGE USD dkkdkd'
        result = user_input(command)
        self.assertEqual(result, 'INVALID AMOUNT dkkdkd')

    def test_exchange_6(self):
        """Test case: not a number"""
        utils.PATH = r'C:\Users\Capibara\Documents\GitHub\hillel_python_course_beginer\HW_16\task_4\db.json'
        command: str = 'EXCHANGE UAH 100'
        result = user_input(command)
        self.assertIn('UAH', result)


if __name__ == '__main__':
    main()
