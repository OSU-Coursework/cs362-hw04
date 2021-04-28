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

# ---- 2.1 generate full name with provided first and last name ----

def gen_full_name(_first, _last):
    return "{0} {1}".format((_first, "Jane/John") [len(str(_first).strip()) == 0], (_last, "Doe") [len(str(_last).strip()) == 0])

# ---- 2.2 write 3 unit tests ----

class GenFullNameTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(gen_full_name("", ""), "Jane/John Doe")
        self.assertEqual(gen_full_name(" ", ""), "Jane/John Doe")
        self.assertEqual(gen_full_name("", " "), "Jane/John Doe")
        self.assertEqual(gen_full_name(" ", " "), "Jane/John Doe")

    def test_correct_output(self):
        self.assertEqual(gen_full_name("Brock", "Samson"), "Brock Samson")

    def test_nonstandard_input(self):
        self.assertEqual(gen_full_name(1101, 1101), "1101 1101")
        self.assertEqual(gen_full_name(3564.45546, 87965.25554), "3564.45546 87965.25554")
        self.assertEqual(gen_full_name(True, False), "True False")


if __name__ == '__main__':
    unittest.main()
