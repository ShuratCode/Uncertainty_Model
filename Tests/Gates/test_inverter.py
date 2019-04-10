from unittest import TestCase

from Gates.InverterGate import Inverter


class TestInverter(TestCase):

    def test_inverter_input_1(self):
        inverter = Inverter({'i1': 0})
        self.assertEqual(inverter.get_output(), 1)

    def test_inverter_input_0(self):
        inverter = Inverter({'i1': 1})
        self.assertEqual(inverter.get_output(), 0)

    def test_set_input(self):
        inverter = Inverter({'i1': 0})
        inverter.set_input({'i1': 1})
        self.assertEqual(inverter.get_output(), 0)
