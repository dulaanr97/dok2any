import os
import argparse
from openbabel import openbabel

def dok2xyz(dok_content):
    remarks = []
    current_structure = []
    
    for line in dok_content.splitlines():
        if line.startswith('REMARK Cluster'):
            remarks.append(line.strip())
        elif line.startswith('ATOM'):
            current_structure.append(line.strip())

    if not current_structure:
        return None

    # Use REMARK line as the comment
    comment = 'REMARK from dok file => ' + remarks[0] if remarks else ''
    # Prepare XYZ format content
    num_atoms = len(current_structure)
    xyz_content = f"{num_atoms}\n{comment}\n"
    
    for atom_line in current_structure:
        parts = atom_line.split()
        atom_type = parts[2]
        # Correct the atom_type format: capitalize first letter, lowercase second letter
        corrected_atom_type = atom_type[0] + atom_type[1].lower() if len(atom_type) > 1 else atom_type
        
        x, y, z = parts[5], parts[6], parts[7]
        xyz_content += f"{corrected_atom_type} {x} {y} {z}\n"

    return xyz_content

def xyz_converter(input_xyz_content, output_format):
    # Create an Open Babel conversion object
    obConversion = openbabel.OBConversion()
    obConversion.SetInAndOutFormats("xyz", output_format)

    # Create a molecule object
    mol = openbabel.OBMol()

    # Read the .xyz content
    obConversion.ReadString(mol, input_xyz_content)

    # Convert the molecule to the desired output format
    output_content = obConversion.WriteString(mol)
    
    return output_content

def process_dok_file(dok_file_path, output_format, output_file_path):
    # Read the content of the .dok file
    with open(dok_file_path, 'r') as file:
        data = file.readlines()

    structures = []
    current_structure = []

    for line in data:
        if line.startswith('ATOM') or line.startswith('REMARK Cluster'):
            current_structure.append(line.strip())
        elif line.startswith('END'):
            if current_structure:
                # Join current structure lines into a single string
                dok_content = '\n'.join(current_structure)
                # Convert DOK to XYZ
                xyz_content = dok2xyz(dok_content)
                if xyz_content:
                    # Convert XYZ to the specified output format
                    output_content = xyz_converter(xyz_content, output_format)
                    # Append the output content
                    structures.append(output_content)
                current_structure = []

    # Write all structures to a single output file
    with open(output_file_path, 'w') as f:
        for structure in structures:
            f.write(structure)
            f.write("\n")

    print(f"Converted {dok_file_path} to {output_file_path} successfully!")

def main():
    parser = argparse.ArgumentParser(description='Convert DOK files to specified output format using Open Babel.')
    parser.add_argument('-idok', metavar='input_dok_folder', type=str, required=True,
                        help='Path to the folder containing DOK files')
    parser.add_argument('-oformat', metavar='output_format', type=str, required=True,
                        help='Output format for conversion (e.g., mol2, pdb, sdf)')
    parser.add_argument('-odir', metavar='output_dir', type=str, required=True,
                        help='Path to the output directory')
    
    args = parser.parse_args()
    
    input_folder = args.idok
    output_format = args.oformat.lower()  # Ensure the output format is lowercase
    output_dir = args.odir

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each DOK file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.dok'):
            dok_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_dir, filename.replace('.dok', f'.{output_format}'))
            process_dok_file(dok_file_path, output_format, output_file_path)

if __name__ == "__main__":
    main()
