from Gates.Gate import Gate


class XorGate(Gate):

    def __init__(self, inputs: dict, gate_name: str = ""):
        self.inputs = inputs
        self.name = gate_name

    def calculate_output(self):
        values = list(self.inputs.values())
        value_1 = values[0]
        value_2 = values[1]

        if value_1 == 1 and value_2 == 1:
            self.output = 0

        if value_1 == 1 and value_2 == 0:
            self.output = 1

        if value_1 == 0 and value_2 == 1:
            self.output = 1

        if value_1 == 0 and value_2 == 0:
            self.output = 0

    def get_output(self):
        return self.output

    def get_input(self, key: str):
        return self.inputs.get(key)

    def get_inputs(self):
        return self.inputs

    def set_input(self, key: str, value: int):
        self.inputs[key] = value

    def get_name(self):
        return self.name
