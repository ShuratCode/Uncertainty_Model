from Gates.Gate import Gate
from Gates.OrGate import OrGate


class NorGate(Gate):

    def __init__(self, inputs: dict):
        self.__or_gate = OrGate(inputs)
        self.__calculate_output()

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

    def get_input(self, index: str):
        return self.__or_gate.get_input(index)

    def set_input(self, index: str, value: int):
        self.__or_gate.set_input(index, value)
        self.__calculate_output()
