import unittest

import common.boats
import day12

class TestBoat(unittest.TestCase):
    def test_boat_init(self):
        boat = common.boats.Boat()
        self.assertEqual(90, boat.heading)
        self.assertEqual(0, boat.pos_north)
        self.assertEqual(0, boat.pos_east)

    def test_move(self):
        boat = common.boats.Boat()
        boat.move('N10')
        boat.move('E10')
        self.assertEqual(90, boat.heading)
        self.assertEqual(10, boat.pos_north)
        self.assertEqual(10, boat.pos_east)
        boat.move('S8')
        boat.move('W5')
        self.assertEqual(90, boat.heading)
        self.assertEqual(2, boat.pos_north)
        self.assertEqual(5, boat.pos_east)

    def test_move_forward(self):
        boat = common.boats.Boat()
        boat.move('F10')
        self.assertEqual(90, boat.heading)
        self.assertEqual(0, boat.pos_north)
        self.assertEqual(10, boat.pos_east)

    def test_turn(self):
        boat = common.boats.Boat()
        boat.move('L90')
        self.assertEqual(0, boat.heading)
        self.assertEqual(0, boat.pos_north)
        self.assertEqual(0, boat.pos_east)

        boat.move('R180')
        self.assertEqual(180, boat.heading)
        self.assertEqual(0, boat.pos_north)
        self.assertEqual(0, boat.pos_east)

        boat.move('R180')
        self.assertEqual(0, boat.heading)
        self.assertEqual(0, boat.pos_north)
        self.assertEqual(0, boat.pos_east)


if __name__ == '__main__':
    unittest.main()
