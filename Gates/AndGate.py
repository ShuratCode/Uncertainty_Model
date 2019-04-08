from Gates.Gate import Gate


class AndGate (Gate):

    def __init__(self, inputs: dict):
        self.__inputs = inputs
        self.__calculate_output()

    def __calculate_output(self):
        value = 1
        for index in range(0, len(self.__inputs)):
            input_value = self.__inputs[index]
            if input_value == 0:
                value = 0
                break
        self.__output = value

    def get_output(self):
        return self.__output

    def get_inputs(self):
        return self.__inputs

    def get_input(self, index: int):
        return self.__inputs[index]

    def set_input(self, index: int, value: int):
        self.__inputs[index] = value

