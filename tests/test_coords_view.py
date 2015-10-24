import unittest
from mock import Mock
from pycoords_lib import ScaledCoords, CoordsView


class Test_Coords(unittest.TestCase):

    def test_scale_of_view_when_the_range_is_tall(self):
        coords = ScaledCoords([(-100, -50), (100, 50)], 100, 100)
        self.assertAlmostEqual(0.38, coords.scale)
        self.assertAlmostEqual(0, coords.center_x)

    def test_scale_of_view_when_the_range_is_wide(self):
        coords = ScaledCoords([(-100, -200), (100, 200)], 100, 100)
        self.assertAlmostEqual(0.19, coords.scale)


class Test_Coords_View(unittest.TestCase):

    def setUp(self):
        self.canvas = Mock()
        self.canvas.get_width.return_value = 100
        self.canvas.get_height.return_value = 100
        self.coords = ScaledCoords([[-100, -200], [100, 200]], 100, 100)
        self.view = CoordsView(self.canvas, self.coords)

    def test_show(self):
        self.view.show()
        self.canvas.create_circle.assert_called_with(
            69.0, 88.0, 12, fill='blue')

    def test_move_canvas(self):
        self.view.move(50, 50, 60, 60)
        self.assertAlmostEqual(-315.7894736842105, self.coords.center_x)

    def test_move_point(self):
        self.view.move(69, 88, 60, 60)
        self.assertAlmostEqual(0, self.coords.center_x)

    def test_add(self):
        self.view.put = Mock()
        self.view.add(50, 50)
        self.assertAlmostEqual(3, len(self.coords.coords))
        self.assertEqual([0, 0], self.coords.coords[-1])
        self.view.put.assert_called_with(2)

    def test_remove_no_exist(self):
        self.view.show = Mock()
        self.view.remove(50, 50)
        self.assertEqual(2, len(self.coords.coords))
        self.assertEqual(0, self.view.show.call_count)

    def test_remove(self):
        self.view.show = Mock()
        self.view.remove(*self.coords.scaled(0))
        self.assertEqual(1, len(self.coords.coords))
        self.view.show.assert_called_with()
