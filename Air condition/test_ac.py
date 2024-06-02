import unittest
import ac


class TestAirCondition(unittest.TestCase):
    def test_on(self):
        output = ac.on(switch=False)
        self.assertTrue(output)

    def test_off(self):
        output = ac.off(switch=False)
        self.assertFalse(output)

    def test_temperature_increase_but_not_beyond_30(self):
        output = ac.temperature_increase_but_not_beyond_30(temperature_value=28)
        self.assertEqual(29, output)

    def test_temperature_decrease_but_not_below_16(self):
        output = ac.temperature_decrease_but_not_below_16(temperature_value=20)
        self.assertEqual(19, output)


if __name__ == '__main__':
    unittest.main()
