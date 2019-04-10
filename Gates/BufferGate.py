from Gates.Gate import Gate


class BufferGate(Gate):

    def __init__(self, input_value: dict, gate_name: str = ""):
        self.inputs = input_value
        self.calculate_output()
        self.name = gate_name

    def calculate_output(self):
        value = list(self.inputs.values())[0]
        if value == 0:
            self.output = 0
        if value == 1:
            self.output = 1

    def set_input(self, input_value: dict):
        self.inputs = input_value
        self.calculate_output()

    def get_output(self):
        return self.output

    def get_name(self):
        return self.name
