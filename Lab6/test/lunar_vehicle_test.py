import math
import unittest
from Lab6.src.LunarVehicle import LunarVehicle


class LunarVehicleTest(unittest.TestCase):
    def setUp(self):
        self.vehicle = LunarVehicle()

    def tearDown(self):
        self.vehicle = None

    def test_initial_position(self):
        self.assertEqual(self.vehicle.get_position(), (0,0,0))

    def test_start_position(self):
        x = 10
        y = 20
        angle = 90

        self.vehicle.start_position(x,y,angle)
        self.assertEqual(self.vehicle.get_position(), (x,y,angle))

    def test_go_forward(self):
        distance = 10

        self.vehicle.go_forward(distance)
        self.assertEqual(self.vehicle.get_position(), (distance,0,0))

    def test_go_backward(self):
        distance = 20

        self.vehicle.go_back(distance)
        self.assertEqual(self.vehicle.get_position(), (-distance,0,0))

    def test_rotation(self):
        self.vehicle.rotation(90)
        self.assertEqual(self.vehicle.get_position(), (0,0,90))

        self.vehicle.rotation(270)
        self.assertEqual(self.vehicle.get_position(), (0,0,0))

        self.vehicle.rotation(-90)
        self.assertEqual(self.vehicle.get_position(), (0,0,270))

    def test_movement_at_angle(self):
        self.vehicle.start_position(0,0,45)
        self.vehicle.go_forward(math.sqrt(2))
        self.assertAlmostEqual(self.vehicle.x, 1, places=5)
        self.assertAlmostEqual(self.vehicle.y, 1, places=5)

        self.vehicle.go_back(math.sqrt(2))
        self.assertAlmostEqual(self.vehicle.x, 0, places=5)
        self.assertAlmostEqual(self.vehicle.y, 0, places=5)

if __name__ == "__main__":
    unittest.main()