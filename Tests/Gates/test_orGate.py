from unittest import TestCase

from Gates.OrGate import OrGate


class TestOrGate(TestCase):

    def test_or_simple_1(self):
        inputs = {'i1': 1, 'i2': 1}
        or_gate = OrGate(inputs)
        or_gate.calculate_output()
        self.assertEqual(or_gate.get_output(), 1)

    def test_or_simple_0(self):
        inputs = {'i1': 0, 'i2': 0}
        or_gate = OrGate(inputs)
        or_gate.calculate_output()
        self.assertEqual(or_gate.get_output(), 0)

    def test_3_inputs_diff(self):
        inputs = {'i1': 0, 'i2': 1, 'i3': 0}
        or_gate = OrGate(inputs)
        or_gate.calculate_output()
        self.assertEqual(or_gate.get_output(), 1)

    def test_set_input(self):
        inputs = {'il': 0, 'i2': 1}
        or_gate = OrGate(inputs)
        or_gate.calculate_output()
        or_gate.set_input('i2', 0)
        or_gate.calculate_output()
        self.assertEqual(or_gate.get_output(), 0)

    def test_get_input(self):
        inputs = {'il': 0, 'i2': 1}
        or_gate = OrGate(inputs)
        or_gate.calculate_output()
        self.assertEqual(or_gate.get_input('il'), 0)
