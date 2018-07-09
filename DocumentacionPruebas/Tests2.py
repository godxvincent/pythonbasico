# Unit Tests
import unittest


def doblar(a): return a*2


def suma(a, b): return a+b


def esPar(a): return True if a % 2 == 0 else False
# Siempre devuelve True or False si pasan o no el test.


class Prueba(unittest.TestCase):

    def test_doblar(self):
        self.assertEqual(doblar(5), 10)
        self.assertEqual(doblar(-5), -10)

        # Las unittest devuelve tres respuestas OK, F (Exception Asertiva), E (Error)
        # pass
        # raise AssertionError()
        # 1/0

    def test_suma(self):
        self.assertEqual(suma(4, 4), 8)
        self.assertEqual(suma(4, -2), 2)
        self.assertEqual(suma('Ab', 'cd'), 'Abcd')
        self.assertEqual(suma('Ab', 0), 'Ab0')

    def test_esPar(self):
        self.assertEqual(esPar(2), True)
        self.assertEqual(esPar(3), False)
        self.assertEqual(esPar(3), True)


if __name__ == "__main__":
    unittest.main()
