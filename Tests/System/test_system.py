from unittest import TestCase
from System.System import System
from System.Diagnoser import Diagnoser


class TestSystem(TestCase):

    def setUp(self):
        self.system = System('')
        self. system.inputs = {'i1': None, 'i2': None, 'i3': None}
        self. system.zeds = {'z1': None, 'z2': None, 'z3': None, 'z4': None}
        self. system.outputs = {'o1': None}
        or1 = System.build_gate('or', {'i1': None, 'i2': None})
        and2 = System.build_gate('and', {'i2': None, 'z2': None})
        nor3 = System.build_gate('nor', {'i3': None})
        and4 = System.build_gate('and', {'z1': None, 'z3': None})
        or5 = System.build_gate('or', {'z4': None, 'i3': None})

        self.  system.gates = {
            'gate1': {'gate': or1, 'output': 'z1'},
            'gate2': {'gate': and2, 'output': 'z3'},
            'gate3': {'gate': nor3, 'output': 'z2'},
            'gate4': {'gate': and4, 'output': 'z4'},
            'gate5': {'gate': or5, 'output': 'o1'},
        }

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

    def test_calc_output_000(self):
        self.system.calc_system_output({'i1': 0, 'i2': 0, 'i3': 0})
        self.assertEqual(self.system.outputs['o1'], 0)

    def test_calc_output_001(self):
        self.system.calc_system_output({'i1': 0, 'i2': 0, 'i3': 1})
        self.assertEqual(self.system.outputs['o1'], 1)

    def test_calc_output_010(self):
        self.system.calc_system_output({'i1': 0, 'i2': 1, 'i3': 0})
        self.assertEqual(self.system.outputs['o1'], 1)

    def test_calc_output_011(self):
        self.system.calc_system_output({'i1': 0, 'i2': 1, 'i3': 1})
        self.assertEqual(self.system.outputs['o1'], 1)

    def test_calc_output_100(self):
        self.system.calc_system_output({'i1': 1, 'i2': 0, 'i3': 0})
        self.assertEqual(self.system.outputs['o1'], 0)

    def test_calc_output_101(self):
        self.system.calc_system_output({'i1': 1, 'i2': 0, 'i3': 1})
        self.assertEqual(self.system.outputs['o1'], 1)

    def test_calc_output_110(self):
        self.system.calc_system_output({'i1': 1, 'i2': 1, 'i3': 0})
        self.assertEqual(self.system.outputs['o1'], 1)

    def test_calc_output_111(self):
        self.system.calc_system_output({'i1': 1, 'i2': 1, 'i3': 1})
        self.assertEqual(self.system.outputs['o1'], 1)

    def test_diagnoser_simple(self):
        self.system.calc_system_output({'i1': 0, 'i2': 0, 'i3': 0})
        diag = Diagnoser(self.system)
        outputs = self.system.generate_output_probabilities(self.system.outputs)
        results = diag.generate_system_diagnosis(outputs)

        print('wasdasd')
