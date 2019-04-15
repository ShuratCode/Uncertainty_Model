from Gates.AndGate import AndGate
from Gates.Gate import Gate


class NandGate(Gate):

    def __init__(self, inputs: dict, gate_name: str = ""):
        self.__and_gate = AndGate(inputs)
        self.name = gate_name

    def calculate_output(self):
        self.__and_gate.calculate_output()
        value = self.__and_gate.get_output()
        if value == 0:
            self.output = 1
        if value == 1:
            self.output = 0

    def get_output(self):
        return self.output

    def get_inputs(self):
        return self.__and_gate.get_inputs()

    def get_input(self, key: str):
        return self.__and_gate.get_input(key)

    def set_input(self, key: str, value: int):
        self.__and_gate.set_input(key, value)

    def get_name(self):
        return self.name

