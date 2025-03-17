from calculator import Calculator


def test_add(self):
    calc = Calculator()
    self.assertEqual(calc.add(2, 3), 5)
    self.assertEqual(calc.add(-1, 1), 0)
    self.assertEqual(calc.add(-1, -1), -2)
    self.assertEqual(calc.add(0, 0), 0)

