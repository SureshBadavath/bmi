import unittest

from run import BMI

bmi_ = BMI()

class TestSum(unittest.TestCase):
    def test_bmi_real(self):
        bmi = bmi_.calculate_bmi(171, 96)
        self.assertEqual(bmi, 32.83)
    
    def test_category_risk(self):
        category, risk = bmi_.get_category_and_risk(26)
        self.assertEqual(category, 'Overweight')
        self.assertEqual(risk, 'Enhanced risk')

    def test_bmi_height_null(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up(None, 97, 1)
        self.assertEqual(bmi, None)

    def test_bmi_weight_null(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up(157, None, 1)
        self.assertEqual(bmi, None)

    def test_bmi_height_negitive(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up(-10, 96, 0)
        self.assertEqual(bmi, None)

    def test_bmi_weight_negitive(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up(156, -20, 0)
        self.assertEqual(bmi, None)
    
    def test_bmi_height_zero(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up(0, 100, 0)
        self.assertEqual(bmi, None)

    def test_bmi_weight_zero(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up(0, -20, 0)
        self.assertEqual(bmi, None)
        self.assertNotEqual(status, 'Calculated')

    def test_bmi_height_string(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up("187", 26, 0)
        self.assertEqual(bmi, None)

    def test_bmi_weight_string(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up(156, "87", 0)
        self.assertEqual(bmi, None)

    def test_bmi_over_weight_counter_invalid(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up(156, 98, 1)
        self.assertNotEqual(ow_counter, 2)
    
    def test_bmi_over_weight_counter_valid(self):
        bmi, ow_counter, category, risk, status =  bmi_.bmi_check_up(167, 82, 1)
        self.assertEqual(ow_counter, 2)
        self.assertEqual(status, 'Calculated')
        self.assertEqual(category, 'Overweight')
        self.assertEqual(risk, 'Enhanced risk')

if __name__ == '__main__':
    unittest.main()