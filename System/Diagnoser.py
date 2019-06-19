MALFUNCTION_PROBABILITY = 0.2


class Diagnoser:

    def __init__(self, system):
        """
        :param system: The system made of components
        final_diagnosis: a dictionary mapping between a possible output (key) to a dictionary mapping between possible
        faulty gates (represented as a tuple) and the probability for each one (value)
        """
        self.system = system
        self.expected_output = system.outputs  # The correct output of the system
        self.final_diagnosis = None
        self.output_probabilities = None
        self.faulty_combinations = {}
        self.curr_max_probability = 0

    def generate_system_diagnosis(self, output_probabilities):
        """
        This function iterates through all possible outputs in the given dictionary and produces a diagnosis for each.
        Returns the most likely diagnosis.
        :param output_probabilities: A dictionary of the probability for all possible outputs.
        :return: The components most likely to be faulty.
        """
        self.output_probabilities = output_probabilities
        sorted_outputs = [(combo, prob) for combo, prob in self.output_probabilities.items()]
        sorted_outputs.sort(key=lambda k: k[1], reverse=True)

        for output in sorted_outputs:  # iterate through all possible outputs.
            self.faulty_combinations[output[0]] = set()
            self.diagnose(output[0])

        return self.final_diagnosis

    def sorted_diagnosis(self):

        sorted_diag = [(combo, v['probability'], v['output']) for combo, v in self.final_diagnosis.items()]

        sorted_diag.sort(key=lambda k: k[1], reverse=True)

        top = 3
        print("*** System Diagnosis: ***")
        print(f"Top {top} most probable faults:")
        for i in range(top):
            print(f'1) {sorted_diag[i][0]} , with a probability of {round(sorted_diag[i][1], 3)} and with an output of'
                  f' {self.stringify_output(sorted_diag[i][2])}')

        return sorted_diag

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
        output_dict = self.dictify_output_string(output)
        for n in range(0, num_of_components + 1):
            if self.should_continue(output, n):
                #print(f'n = {n}')
                self.detect_faulty_gates(max_gates=n, faulty_output=output_dict, faulty_gates=[])
            else:
                break

    def detect_faulty_gates(self, max_gates, faulty_output, faulty_gates):
        """
        Receives the number of faulty components that might cause the incorrect output. Tries to find a combination of
        num-components. If a combination was found - return the faulty gate names and probability for this. Otherwise,
        return None
        Performs a recursive search of supersets of the given output. Returns faulty_gates if found a combination.
        :param faulty_gates: A list containing gate names that will be checked to see if they caused the output.
        :param max_gates: Number of components that might be faulty
        :param faulty_output: The observed incorrect output
        :return: All possible diagnosis and the probability for them.
        """

        self.system.clean_system()
        calculated_output = self.system.calc_system_output(self.system.inputs, faulty_gates)

        if not self.is_superset(faulty_gates, faulty_output):  # If it's a superset of an existing combo, skip it
            if self.stringify_output(calculated_output) == self.stringify_output(faulty_output):
                self.update_diagnosis(faulty_gates, faulty_output)  # The correct output has been found
            elif max_gates > 0:  # We continue to try and find a combination
                for gate_name in self.system.gates:
                    if gate_name not in faulty_gates:  # this gate hasn't been checked yet
                        self.detect_faulty_gates(max_gates - 1, faulty_output, faulty_gates + [gate_name])

    def update_diagnosis(self, new_faulty_gates, faulty_output):
        try:
            new_faulty_gates.sort()
            output_string = self.stringify_output(faulty_output)
            probability = self.prob_of_n_faulty_gates(len(new_faulty_gates)) * self.output_probabilities[output_string]
            if probability > self.curr_max_probability:
                self.curr_max_probability = probability
                faulty = self.faulty_gates_to_tuple(new_faulty_gates)
                self.final_diagnosis = \
                    {'faulty gates': faulty, 'probability': probability, 'With an output of ': faulty_output}
            self.faulty_combinations[output_string].add(frozenset(new_faulty_gates))
        except AttributeError:
            print(new_faulty_gates)

    def prob_of_n_faulty_gates(self, faulty_gates_num):
        return pow(MALFUNCTION_PROBABILITY, faulty_gates_num) * \
               pow(1 - MALFUNCTION_PROBABILITY, len(self.system.gates) - faulty_gates_num)

    @staticmethod
    def faulty_gates_to_tuple(new_faulty_gates):
        if len(new_faulty_gates) > 0:
            return tuple(new_faulty_gates)
        else:
            return 'No faulty components',

    @staticmethod
    def dictify_output_string(output):
        output_dict = {}
        for i in range(0, len(output)):
            output_dict['o' + str(i + 1)] = int(output[i])
        return output_dict

    def is_superset(self, faulty_gates, output):
        faulty_gates.sort()
        faulty_set = frozenset(faulty_gates)
        for combo in self.faulty_combinations[self.stringify_output(output)]:
            if combo.issubset(faulty_set) and len(combo) > 0 and len(faulty_gates) > 0:
                return True

        return False

    def should_continue(self, output, n):
        """
        Tests if it's worth trying to find a combination of faulty components. Basically calculates if the probability
        is already too low to be worth trying.
        :param output: The output being checked
        :param n: Current number of faulty components that will be in the faulty set
        :return: True if it's worth trying, otherwise false.
        """
        output_prob = self.output_probabilities[output]
        faulty_prob = self.prob_of_n_faulty_gates(n)
        if self.curr_max_probability > output_prob * faulty_prob:
            return False
        return True
