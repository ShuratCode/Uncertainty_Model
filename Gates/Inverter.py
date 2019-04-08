class Inverter:

    def __init__(self, input_value):
        self.__input = input_value
        self.__calculate_output()

    def __calculate_output(self):
        if self.__input is 1:
            self.__output = 0
        else:
            self.__output = 1

    def get_input(self):
        return self.__input

    def get_output(self):
        return self.__output

    def set_input(self, input_value):
        self.__input = input_value
