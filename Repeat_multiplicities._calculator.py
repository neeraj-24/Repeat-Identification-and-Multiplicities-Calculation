#!/usr/bin/env python3


import os

def read_repeat_units_from_files(input_dir):
    repeat_units = {}
    
    # Iterate through all files in the input directory
    for file_name in sorted(os.listdir(input_dir)):
        if file_name.startswith('repeat_') and file_name.endswith('.txt'):
            file_path = os.path.join(input_dir, file_name)
            
            # Read the repeat from the file
            with open(file_path, 'r') as f:
                lines = f.readlines()
                sequence = lines[1].strip().split(': ')[1]  # Extract the sequence from the file
                
                # Analyze the occurrence of the repeat unit
                if sequence in repeat_units:
                    repeat_units[sequence]['count'] += 1
                    repeat_units[sequence]['files'].append(file_name)
                else:
                    repeat_units[sequence] = {
                        'count': 1,
                        'files': [file_name]
                    }
    
    return repeat_units

def write_multiplicities_to_file(repeat_units, output_dir):
    output_file = os.path.join(output_dir, 'repeat_unit_multiplicities.txt')
    
    # Write the multiplicities to the new file
    with open(output_file, 'w') as f:
        for idx, (sequence, data) in enumerate(repeat_units.items(), start=1):
            f.write(f"Repeat Unit {idx}:\n")
            f.write(f"Sequence: {sequence}\n")
            f.write(f"Multiplicity: {data['count']}\n")
            f.write(f"Found in files: {', '.join(data['files'])}\n\n")
    
    print(f"Multiplicity file written to: {output_file}")

# Main 
def main():
    input_dir = '/path/to/your/identified_repeat_output_directory'  # Defined input directory of repeats
    output_dir = '/path/to/your/multiplicity_repeat_output_directory'  # Defined output directory
    
    # Read all repeat files
    print("Reading repeat unit files and calculating multiplicities...")
    repeat_units = read_repeat_units_from_files(input_dir)
    
    # Write output to a new file
    print(f"Writing multiplicities to a file in {output_dir}...")
    write_multiplicities_to_file(repeat_units, output_dir)
    print(f"Multiplicity analysis complete.")


if __name__ == "__main__":
    main()

