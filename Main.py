import os
import csv
import time

from System.System import System
from System.Diagnoser import Diagnoser

if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys_name = 'c17'
    path = os.path.join(ROOT_DIR, f'Resources\\system\\{sys_name}.sys')
    system = System(path)
    obs_path = os.path.join(ROOT_DIR, f'Resources\\iscas\\{sys_name}_iscas85.obs')
    scenarios = system.parse_obs_files(obs_path)
    idx = 1
    with open(f'{sys_name}_diagnostics.csv', 'w', newline='') as diagnostic_file:
        fieldnames = ['system_name', 'input_value', 'expected_output', 'observed_output', 'diagnosis',
                      'number_of_gates', 'probability', 'time']
        csv_writer = csv.DictWriter(diagnostic_file, fieldnames)
        csv_writer.writeheader()
        for case, settings in scenarios.items():
            print(f'Case #{idx}')
            start = time.time()
            inputs = settings['inputs']
            observed_output = settings['outputs']
            output_probabilities = system.generate_output_probabilities(observed_output)
            # print(f'Expected output: {system.outputs}')
            # print(f'Observed output: {observed_output}')
            diagnoser = Diagnoser(system)
            diagnosis = diagnoser.generate_system_diagnosis(output_probabilities)
            end = time.time()
            print(diagnosis)
            expected = system.calc_system_output(inputs)
            inputs = '[' + ','.join(diagnoser.stringify_output(inputs)) + ']'
            outputs = '[' + ','.join(diagnoser.stringify_output(observed_output)) + ']'
            expected = '[' + ','.join(diagnoser.stringify_output(expected)) + ']'
            csv_writer.writerow({'system_name': sys_name,
                                 'input_value': inputs,
                                 'expected_output': expected,
                                 'observed_output': outputs,
                                 'diagnosis': ' & '.join(diagnosis['faulty gates']),
                                 'number_of_gates': str(len(diagnosis['faulty gates'])),
                                 'probability': round(diagnosis['probability'], 3),
                                 'time': str(end-start)})
            idx += 1
    print("Done")
