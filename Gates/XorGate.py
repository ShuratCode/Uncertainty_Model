from Gates.Gate import Gate


class XorGate(Gate):

    def __init__(self, inputs: dict, gate_name: str = ""):
        self.__inputs = inputs
        self.__calculate_output()
        self.__name = gate_name

    def __calculate_output(self):
        values = list(self.__inputs.values())
        value_1 = values[0]
        value_2 = values[1]

        if value_1 == 1 and value_2 == 1:
            self.__output = 0

        if value_1 == 1 and value_2 == 0:
            self.__output = 1

        if value_1 == 0 and value_2 == 1:
            self.__output = 1

        if value_1 == 0 and value_2 == 0:
            self.__output = 0

    def get_output(self):
        return self.__output

    def get_input(self, key: str):
        return self.__inputs.get(key)

    def get_inputs(self):
        return self.__inputs

    def set_input(self, key: str, value: int):
        self.__inputs[key] = value
        self.__calculate_output()

    def get_name(self):
        return self.__name
