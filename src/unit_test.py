"""
    Simple demo de unit test case
    loriacralos@gmail.com
    I-2019
    @see https://docs.python.org/3/library/unittest.html
"""
"""
Autores:
  - Rebecca Garita Gutiérrez        117620191   Martes y Viernes, 10 AM
  - David Alberto Guevara Sánchez   402450355   Martes y Viernes, 10 AM
  - M. Fernanda Gonzáles Arias      117660980   Martes y Viernes, 10 AM
  - Luis David Villalobos Gonzáles  117540697   Martes y Viernes, 10 AM
"""
import unittest

class TestMethods(unittest.TestCase):
    def setUp(self):
        print("Setting up case\n")

    def test_one(self):
        self.assertEqual(923456 * 7895634, 7291270591104)

    def test_two(self):
        self.assertEqual(77666 * 16324, 1267819784)

    def test_three(self):
        self.assertEqual(7799 * 16324, 1267819784)
        
    def tearDown(self):
        print("\nFinishing up cases")

if __name__ == '__main__':
    unittest.main()