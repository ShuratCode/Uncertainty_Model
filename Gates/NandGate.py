from Gates.AndGate import AndGate
from Gates.Gate import Gate


class NandGate(Gate):

    def __init__(self, inputs: dict, gate_name: str = ""):
        self.__and_gate = AndGate(inputs)
        self.__calculate_output()
        self.__name = gate_name

    def __calculate_output(self):
        value = self.__and_gate.get_output()
        if value == 0:
            self.__output = 1
        if value == 1:
            self.__output = 0

    def get_output(self):
        return self.__output

    def get_inputs(self):
        return self.__and_gate.get_inputs()

    def get_input(self, key: str):
        return self.__and_gate.get_input(key)

    def set_input(self, key: str, value: int):
        self.__and_gate.set_input(key, value)
        self.__calculate_output()

    def get_name(self):
        return self.__name

