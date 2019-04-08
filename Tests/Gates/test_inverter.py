from unittest import TestCase

from Gates.Inverter import Inverter


class TestInverter(TestCase):

    def test_inverter_input_1(self):
        inverter = Inverter(1)
        self.assertEqual(inverter.get_output(), 0)

    def test_inverter_input_0(self):
        inverter = Inverter(0)
        self.assertEqual(inverter.get_output(), 1)
