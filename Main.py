import os

from System.System import System
from System.Diagnoser import Diagnoser

if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(ROOT_DIR, 'Resources\\system\\74182.sys')
    system = System(path)
    obs_path = os.path.join(ROOT_DIR, 'Resources\\iscas\\74182_iscas85.obs')
    scenarios = system.parse_obs_files(obs_path)
    for case, settings in scenarios.items():
        inputs = settings['inputs']
        observed_output = settings['outputs']
        output_probabilities = system.generate_output_probabilities(observed_output)
        system.calc_system_output(inputs)
        diagnoser = Diagnoser(system)
        diagnosis = diagnoser.generate_system_diagnosis(output_probabilities)
        print(system.outputs)
        print(observed_output)
    print("Done")
