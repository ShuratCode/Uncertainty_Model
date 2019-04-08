from Gates.Gate import Gate


class BufferGate (Gate):

    def __init__(self, input_value: int):
        self.__input = input_value
        self.__calculate_output()

    def __calculate_output(self):
        if self.__input == 0:
            self.__output = 0
        if self.__input == 1:
            self.__output = 1

    def set_input(self, input_value: int):
        self.__input = input_value
        self.__calculate_output()

    def get_output(self):
        return self.__output
