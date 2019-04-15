from unittest import TestCase

from Gates.BufferGate import BufferGate


class TestBufferGate(TestCase):

    def test_simple_0(self):
        buffer = BufferGate({'i1': 0})
        buffer.calculate_output()
        self.assertEqual(buffer.get_output(), 0)

    def test_simple_1(self):
        buffer = BufferGate({'i1': 1})
        buffer.calculate_output()
        self.assertEqual(buffer.get_output(), 1)

    def test_set_input(self):
        buffer = BufferGate({'i1': 0})
        buffer.calculate_output()
        buffer.set_input({'i1': 1})
        buffer.calculate_output()
        self.assertEqual(buffer.get_output(), 1)
