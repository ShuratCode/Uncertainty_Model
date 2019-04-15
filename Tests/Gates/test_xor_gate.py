from unittest import TestCase

from Gates.XorGate import XorGate


class TestXorGate(TestCase):

    def test_xor_two_1(self):
        inputs = {'i1': 1, 'i2': 1}
        xor = XorGate(inputs)
        xor.calculate_output()
        self.assertEqual(xor.get_output(), 0)

    def test_xor_two_0(self):
        inputs = {'i1': 0, 'i2': 0}
        xor = XorGate(inputs)
        xor.calculate_output()
        self.assertEqual(xor.get_output(), 0)

    def test_xor_1_and_0(self):
        inputs = {'i1': 1, 'i2': 0}
        xor = XorGate(inputs)
        xor.calculate_output()
        self.assertEqual(xor.get_output(), 1)

    def test_set_input(self):
        inputs = {'i1': 1, 'i2': 0}
        xor = XorGate(inputs)
        xor.calculate_output()
        xor.set_input('i1', 0)
        xor.calculate_output()
        self.assertEqual(xor.get_output(), 0)

    def test_get_input(self):
        inputs = {'i1': 1, 'i2': 0}
        xor = XorGate(inputs)
        xor.calculate_output()
        self.assertEqual(xor.get_input('i1'), 1)
