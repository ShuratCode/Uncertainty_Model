from Gates.Gate import Gate


class AndGate (Gate):

    def __init__(self, inputs: dict):
        self.__inputs = inputs
        self.__calculate_output()

    def __calculate_output(self):
        value = 1
        for input_value in self.__inputs.values():
            if input_value == 0:
                value = 0
                break
        self.__output = value

    def get_output(self):
        return self.__output

    def get_inputs(self):
        return self.__inputs

    def get_input(self, key: str):
        return self.__inputs.get(key)

    def set_input(self, key: str, value: int):
        self.__inputs[key] = value
        self.__calculate_output()

