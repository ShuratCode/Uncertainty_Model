from unittest import TestCase

from Gates.AndGate import AndGate


class TestAndGate(TestCase):

    def test_and_simple_input_1(self):
        inputs = {'i1': 1, 'i2': 1}
        and_gate = AndGate(inputs)
        self.assertEqual(and_gate.get_output(), 1)

    def test_and_simple_input_0(self):
        inputs = {'i1': 0, 'i2': 0}
        and_gate = AndGate(inputs)
        self.assertEqual(and_gate.get_output(), 0)

    def test_3_inputs_diff(self):
        inputs = {'i1': 0, 'i2': 1, 'i3': 0}
        and_gate = AndGate(inputs)
        self.assertEqual(and_gate.get_output(), 0)

    def test_set_input(self):
        inputs = {'il': 1, 'i2': 1}
        and_gate = AndGate(inputs)
        and_gate.set_input(0, 0)
        self.assertEqual(and_gate.get_output(), 0)
