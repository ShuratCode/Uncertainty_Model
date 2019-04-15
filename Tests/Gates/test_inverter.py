from unittest import TestCase

from Gates.InverterGate import InverterGate


class TestInverter(TestCase):

    def test_inverter_input_1(self):
        inverter = InverterGate({'i1': 0})
        inverter.calculate_output()
        self.assertEqual(inverter.get_output(), 1)

    def test_inverter_input_0(self):
        inverter = InverterGate({'i1': 1})
        inverter.calculate_output()
        self.assertEqual(inverter.get_output(), 0)

    def test_set_input(self):
        inverter = InverterGate({'i1': 0})
        inverter.calculate_output()
        inverter.set_input({'i1': 1})
        inverter.calculate_output()
        self.assertEqual(inverter.get_output(), 0)
