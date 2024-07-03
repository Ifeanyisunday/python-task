import unittest
import bike


class TestMyBike(unittest.TestCase):
    def test_if_bike_can_switch_on(self):
        output = bike.bike_switch_on()
        self.assertTrue(output)

    def test_if_bike_can_switch_off(self):
        output = bike.bike_switch_off()
        self.assertFalse(output)

    def test_if_bike_can_accelerate(self):
        output = bike.accelerate(33)
        self.assertEqual(36, output)

    def test_if_bike_can_decelerate(self):
        output = bike.decelerate(33)
        self.assertEqual(30, output)

    def test_if_bike_can_change_gear_level(self):
        output = bike.change_gear_level(19)
        self.assertEqual("Gear 1", output)



if __name__ == '__main__':
    unittest.main()
