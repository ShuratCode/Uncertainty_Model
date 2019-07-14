
import os
import csv

res_folder = 'D:\\project'

for root, dirs, files in os.walk(res_folder):
    output_fieldnames = ['system', 'num_of_gates', 'bit_diff', 'time']
    input_fieldnames = ['system_name', 'input_value', 'expected_output', 'observed_output', 'diagnosis',
                  'number_of_gates', 'probability', 'bit_difference', 'time']
    if len(files) > 0:
        type = files[0].split(' - ')[1].rstrip('.csv')
        output = f'D:\\{type} results.csv'
        with open(output, 'w', newline='') as out_file:
            csv_writer = csv.DictWriter(out_file, output_fieldnames)
            csv_writer.writeheader()
            for file in files:
                print(file)
                path = os.path.join(res_folder, root, file)
                with open(path, 'r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        name = row['system_name']
                        gates = row['number_of_gates']
                        bit_diff = row['bit_difference']
                        time = row['time']
                        csv_writer.writerow({
                            'system': name,
                            'num_of_gates': gates,
                            'bit_diff': bit_diff,
                            'time': time
                        })



