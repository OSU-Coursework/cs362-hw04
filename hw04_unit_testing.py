# cs362 - hw04
# casey nord
# spring 2021

import unittest


# ---- question 1 ------------------------------------------------------------

# ---- 1.1 calculate volume of a cube ----

def cube_volume(_length):
    return abs(pow(_length, 3))

# ---- 1.2 write 3 unit tests ----

class CubeVolumeTests(unittest.TestCase):

    def test_correct_values(self):
        self.assertEqual(cube_volume(1), 1)
        self.assertEqual(cube_volume(3), 27)
        self.assertEqual(cube_volume(256), 16777216)

    def test_value_always_positive(self):
        self.assertTrue(cube_volume(-1), 1)
        self.assertTrue(cube_volume(-3), 27)
        self.assertTrue(cube_volume(-256), 1777216)

    def test_type(self):
        with self.assertRaises(TypeError):
            cube_volume("42")


# ---- question 2 ------------------------------------------------------------

# ---- 2.1 calculate average of elements in a list ----

def avg_elems_in_list(_list):
    return sum(_list) / (len(_list), 1) [len(_list) == 0] 

# ---- 2.2 write 3 unit tests ----

class AvgElemsInListTest(unittest.TestCase):
    
    def test_list_empty(self):
        self.assertEqual(avg_elems_in_list([]), 0)

    def test_correct_values(self):
        self.assertEqual(avg_elems_in_list([1, 1, 1, 1]), 1)
        self.assertEqual(avg_elems_in_list([6, 10, 42, 1]), 14.75)
        self.assertEqual(avg_elems_in_list([6, 10, 42, True]), 14.75)

    def test_type(self):
        with self.assertRaises(TypeError):
            avg_elems_in_list([6, "10", 42, True])
        with self.assertRaises(TypeError):
            avg_elems_in_list(42)
        with self.assertRaises(TypeError):
            avg_elems_in_list("hello")
        with self.assertRaises(TypeError):
            avg_elems_in_list(False)


# ---- question 3 ------------------------------------------------------------

# ---- 2.1 TODO: generates full name with provided first and last name ----

# ---- 2.2 TODO: write 3 unit tests ----

# TODO: explain tests in word doc


if __name__ == '__main__':
    unittest.main()
