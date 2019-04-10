from Gates.Gate import Gate
from Gates.OrGate import OrGate


class NorGate(Gate):

    def __init__(self, inputs: dict, gate_name: str = ""):
        self.__or_gate = OrGate(inputs)
        self.__calculate_output()
        self.__name = gate_name

    def __calculate_output(self):
        value = self.__or_gate.get_output()
        if value == 1:
            self.__output = 0
        if value == 0:
            self.__output = 1

    def get_output(self):
        return self.__output

    def get_inputs(self):
        return self.__or_gate.get_inputs()

    def get_input(self, key: str):
        return self.__or_gate.get_input(key)

    def set_input(self, key: str, value: int):
        self.__or_gate.set_input(key, value)
        self.__calculate_output()

    def get_name(self):
        return self.__name
