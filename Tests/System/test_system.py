from unittest import TestCase


from System.System import System


class TestSystem(TestCase):

    def test___parse_get_type_and(self):
        input = "and3"
        type, num = System.parse_get_type(input)
        self.assertEqual(type, "and")
        self.assertEqual(num, 3)

    def test_parse_gate_type_or(self):
        s = "or2"
        t, num = System.parse_get_type(s)
        self.assertEqual(t, "or")
        self.assertEqual(num, 2)

    def test_clean_line(self):
        line = '[and3,gate61,z8,i1]'
        expected = ['and3', 'gate61', 'z8', 'i1']
        self.assertEqual(expected, System.line_clean(line))

    def test_parse_gate_type_inverter(self):
        s = 'inverter'
        t, num = System.parse_get_type(s)
        self.assertEqual('inverter', t)
        self.assertEqual(None, num)
