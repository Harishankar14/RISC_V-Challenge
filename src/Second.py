"""
Same Python program then emits the data in the YAML file as a C header file, format of your choosing.
"""
import yaml
import os

def load_yaml(filepath):
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    return data

def resolve_inherited_opcode(yaml_data, base_path):
    opcode_ref = yaml_data.get('format', {}).get('opcodes', {}).get('opcode', {}).get('$inherits')
    if opcode_ref:

        inherited_file = os.path.join(base_path, *opcode_ref.split('#')[0].split('/')[1:])
        try:
            with open(inherited_file, 'r') as f:
                inherited_data = yaml.safe_load(f)
            return inherited_data.get('data', {}).get('value', 0x33) 
        except FileNotFoundError:
            print(f"Warning: Could not find {inherited_file}, defaulting opcode to 0x33")
            return 0x33
    return 0x33  # Default for OP if no inheritance, if not found, just to distinguish.

def generate_c_header(data, output_file, base_path):
    with open(output_file, 'w') as f:
        f.write('#ifndef RISCV_INSTRUCTION_H\n')
        f.write('#define RISCV_INSTRUCTION_H\n\n')
        f.write('// Auto-generated C header from RISC-V YAML\n\n')
        f.write('typedef struct {\n')
        f.write('    const char *name;\n')
        f.write('    unsigned int opcode;\n')
        f.write('    unsigned int funct3;\n')
        f.write('    unsigned int funct7;\n')
        f.write('} riscv_instruction_t;\n\n')
        
        f.write('static const riscv_instruction_t instructions[] = {\n')
        
        name = data.get('name', 'unknown')
        opcode = resolve_inherited_opcode(data, base_path)
        funct3 = data.get('format', {}).get('opcodes', {}).get('funct3', {}).get('value', 0)
        funct7 = data.get('format', {}).get('opcodes', {}).get('funct7', {}).get('value', 0)
        f.write(f'    {{ "{name}", 0x{opcode:x}, 0x{funct3:x}, 0x{funct7:x} }},\n')
        
        f.write('};\n\n')
        f.write('#endif // RISCV_INSTRUCTION_H\n')

def main():
    yaml_path = '/home/harishankar/Downloads/Coding_challenge/data/B/clmul.yaml'
    output_header = 'riscv_instruction.h'
    base_path = os.path.dirname(yaml_path)
    
    data = load_yaml(yaml_path)
    print("Loading the YAML.\n")
    print(yaml.dump(data, sort_keys=False))
    
    generate_c_header(data, output_header, base_path)
    print(f" C header file '{output_header}' generated successfully!")

if __name__ == "__main__":
    main()
