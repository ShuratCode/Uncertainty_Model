MALFUNCTION_PROBABILITY = 0.05

class Diagnoser:

    def __init__(self, system):
        """
        :param system: The system made of components
        final_diagnosis: a dictionary mapping between a possible output (key) to a dictionary mapping between possible
        faulty gates (represented as a tuple) and the probability for each one (value)
        """
        self.system = system
        self.expected_output = system.outputs  # The correct output of the system
        self.final_diagnosis = {}

    def generate_system_diagnosis(self, output_probabilities):
        """
        This function iterates through all possible outputs in the given dictionary and produces a diagnosis for each.
        Returns the most likely diagnosis.
        :param output_probabilities: A dictionary of the probability for all possible outputs.
        :return: The components most likely to be faulty.
        """
        expected_output = self.stringify_output()
        num_of_components = len(self.system.gates)
        for output, probability in output_probabilities.items():  # iterate through all possible outputs.
            self.final_diagnosis[output] = {}
            if output == expected_output:  # The probability for no
                non_failure_probability = pow((1-MALFUNCTION_PROBABILITY), num_of_components) * probability
                self.final_diagnosis[output] = {('No Faulty Gates',): non_failure_probability}
            else:
                self.diagnose(output)

        return self.final_diagnosis

    def stringify_output(self, output=None):
        expected_output = ''
        if output is None:
            output = self.expected_output
        for wire, out in output.items():
            expected_output += str(out)
        return expected_output

    def diagnose(self, output):
        """
        Receives an output and determines what could be the cause for this incorrect output and the probabilty for it.
        :param output: a faulty output of the system
        :return: the gates most likely to cause this.
        """
        num_of_components = len(self.system.gates)
        complete_diagnoses = {}
        output_dict = self.dictify_output_string(output)
        for n in range(1, num_of_components+1):
            result = self.detect_faulty_components(max_gates=n, output=output_dict, faulty_gates=None)
            if result is not None:
                complete_diagnoses.update(result)

        return complete_diagnoses

    def detect_faulty_components(self, max_gates, output, faulty_gates):
        """
        Receives the number of faulty components that might cause the incorrect output. Tries to find a combination of
        num-components. If a combination was found - return the faulty gate names and probability for this. Otherwise,
        return None
        Performs a recursive search of supersets of the given output. Returns faulty_gates if found a combination.
        :param faulty_gates: A list containing gate names that will be checked to see if they caused the output.
        :param max_gates: Number of components that might be faulty
        :param output: The observed incorrect output
        :return: All possible diagnosis and the probability for them.
        """

        #  ToDo: Verify that the equality works
        if self.system.calc_system_output(output, faulty_gates) == output:  # The correct output has been found
            return faulty_gates
        if max_gates == 0:  # We reached the max number of gates
            return None
        else:  # We continue to try and find a combination
            diagnosis = {}
            for gate_name in self.system.gates:
                if gate_name not in faulty_gates:  # this gate hasn't been checked yet
                    faulty_gates = self.detect_faulty_components(max_gates-1, output, faulty_gates + gate_name)
                    if faulty_gates is not None:
                        diagnosis[tuple(faulty_gates)] = pow(MALFUNCTION_PROBABILITY, len(faulty_gates))

        return diagnosis

    @staticmethod
    def dictify_output_string(output):
        output_dict = {}
        for i in range(0, len(output)):
            output_dict['o' + str(i + 1)] = int(output[i])
        return output_dict
