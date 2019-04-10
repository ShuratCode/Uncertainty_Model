from Gates.Gate import Gate


class OrGate(Gate):

    def __init__(self, inputs: dict, gate_name: str = ""):
        self.__inputs = inputs
        self.__calculate_output()
        self.__name = gate_name

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

    def get_input(self, key: str):
        return self.__inputs.get(key)

    def set_input(self, key: str, value: int):
        self.__inputs[key] = value
        self.__calculate_output()

    def get_name(self):
        return self.__name
