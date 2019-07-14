import os
import csv
import time

from System.System import System
from System.Diagnoser import Diagnoser


def calc_bit_disparity(output_1, output_2):
    diff = 0
    for index in range(len(output_1)):
        if output_1[index] != output_2[index]:
            diff += 1

    return diff


if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys_name = '74181'
    path = os.path.join(ROOT_DIR, f'Resources\\system\\{sys_name}.sys')
    system = System(path)
    obs_path = os.path.join(ROOT_DIR, f'Resources\\iscas\\{sys_name}_iscas85.obs')
    scenarios = system.parse_obs_files(obs_path)
    idx = 1
    with open(f'{sys_name}_diagnostics.csv', 'w', newline='') as diagnostic_file:
        fieldnames = ['system_name', 'input_value', 'expected_output', 'observed_output', 'diagnosis',
                      'number_of_gates', 'probability', 'bit_difference', 'time']
        csv_writer = csv.DictWriter(diagnostic_file, fieldnames)
        csv_writer.writeheader()
        for case, settings in scenarios.items():
            print(f'Case #{idx}')
            start = time.time()
            inputs = settings['inputs']
            observed_output = settings['outputs']
            output_probabilities = system.generate_output_probabilities(observed_output)
            system.inputs = inputs
            diagnoser = Diagnoser(system)
            diagnosis = diagnoser.generate_system_diagnosis(output_probabilities)
            end = time.time()
            expected = system.calc_system_output(inputs)
            expected = diagnoser.stringify_output(output=expected)
            observed_output = diagnoser.stringify_output(observed_output)
            bit_disparity = calc_bit_disparity(observed_output, expected)
            #print(f'Observed Output: {observed_output}')
            #print(f'Expected Output: {expected}')
            #print(diagnosis)
            inputs = '[' + ','.join(diagnoser.stringify_output(inputs)) + ']'
            outputs = '[' + ','.join(observed_output) + ']'
            expected = '[' + ','.join(expected) + ']'
            csv_writer.writerow({'system_name': sys_name,
                                 'input_value': inputs,
                                 'expected_output': expected,
                                 'observed_output': outputs,
                                 'diagnosis': ' & '.join(diagnosis['faulty gates']),
                                 'number_of_gates': str(len(diagnosis['faulty gates'])),
                                 'probability': round(diagnosis['probability'], 3),
                                 'bit_difference': str(bit_disparity),
                                 'time': str(end-start)})
            idx += 1
    print("Done")
