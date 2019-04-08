from unittest import TestCase

from Gates.BufferGate import BufferGate


class TestBufferGate(TestCase):

    def test_simple_0(self):
        buffer = BufferGate(0)
        self.assertEqual(buffer.get_output(), 0)

    def test_simple_1(self):
        buffer = BufferGate(1)
        self.assertEqual(buffer.get_output(), 1)

    def test_set_input(self):
        buffer = BufferGate(1)
        buffer.set_input(0)
        self.assertEqual(buffer.get_output(), 0)
