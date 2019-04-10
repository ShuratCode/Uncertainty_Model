from Gates.Gate import Gate


class Inverter (Gate):

    def __init__(self, input_value: dict, gate_name: str = ""):
        self.inputs = input_value
        self.calculate_output()
        self.name = gate_name

    def calculate_output(self):
        value = list(self.inputs.values())[0]
        if value == 1:
            self.output = 0
        else:
            self.output = 1

    def get_input(self):
        return self.inputs

    def get_output(self):
        return self.output

    def set_input(self, input_value: dict):
        self.inputs = input_value
        self.calculate_output()

    def gat_name(self):
        return self.name
