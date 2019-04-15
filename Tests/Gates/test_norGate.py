from unittest import TestCase

from Gates.NorGate import NorGate


class TestNorGate(TestCase):

    def test_or_simple_1(self):
        inputs = {'i1': 1, 'i2': 1}
        nor_gate = NorGate(inputs)
        nor_gate.calculate_output()
        self.assertEqual(nor_gate.get_output(), 0)

    def test_or_simple_0(self):
        inputs = {'i1': 0, 'i2': 0}
        nor_gate = NorGate(inputs)
        nor_gate.calculate_output()
        self.assertEqual(nor_gate.get_output(), 1)

    def test_3_inputs_diff(self):
        inputs = {'i1': 0, 'i2': 1, 'i3': 0}
        nor_gate = NorGate(inputs)
        nor_gate.calculate_output()
        self.assertEqual(nor_gate.get_output(), 0)

    def test_set_input(self):
        inputs = {'il': 0, 'i2': 1}
        nor_gate = NorGate(inputs)
        nor_gate.calculate_output()
        nor_gate.set_input('i2', 0)
        nor_gate.calculate_output()
        self.assertEqual(nor_gate.get_output(), 1)

    def test_get_input(self):
        inputs = {'il': 0, 'i2': 1}
        nor_gate = NorGate(inputs)
        self.assertEqual(nor_gate.get_input('il'), 0)
