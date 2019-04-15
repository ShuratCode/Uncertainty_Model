from unittest import TestCase

from Gates.NandGate import NandGate


class TestNandGate(TestCase):

    def test_nand_two_input_1(self):
        inputs = {'i1': 1, 'i2': 1}
        nand_gate = NandGate(inputs)
        nand_gate.calculate_output()
        self.assertEqual(nand_gate.get_output(), 0)

    def test_and_simple_input_0(self):
        inputs = {'i1': 0, 'i2': 0}
        nand_gate = NandGate(inputs)
        nand_gate.calculate_output()
        self.assertEqual(nand_gate.get_output(), 1)

    def test_3_inputs_diff(self):
        inputs = {'i1': 0, 'i2': 1, 'i3': 0}
        nand_gate = NandGate(inputs)
        nand_gate.calculate_output()
        self.assertEqual(nand_gate.get_output(), 1)

    def test_set_input(self):
        inputs = {'i1': 1, 'i2': 1}
        nand_gate = NandGate(inputs)
        nand_gate.calculate_output()
        nand_gate.set_input('i1', 0)
        nand_gate.calculate_output()
        self.assertEqual(1, nand_gate.get_output())

    def test_get_input(self):
        inputs = {'il': 0, 'i2': 1}
        nand_gate = NandGate(inputs)
        self.assertEqual(nand_gate.get_input('il'), 0)
