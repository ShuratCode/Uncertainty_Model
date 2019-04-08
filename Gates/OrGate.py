from Gates.Gate import Gate


class OrGate(Gate):

    def __init__(self, inputs: dict):
        self.__inputs = inputs
        self.__calculate_output()

    def __calculate_output(self):
        value = 0
        for input_value in self.__inputs.values():
            if input_value == 1:
                value = 1
                break
        self.__output = value

    def get_output(self):
        return self.__output

    def get_inputs(self):
        return self.__inputs

    def get_input(self, index: str):
        return self.__inputs.get(index)

    def set_input(self, index: str, value: int):
        self.__inputs[index] = value
        self.__calculate_output()
