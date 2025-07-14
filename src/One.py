"""
Python program that reads at least one of the YAML files in the RISC-V Unified Database project 
(https://github.com/riscv-software-src/riscv-unified-db) under spec/std/isa/inst.
"""
import yaml

def load_yaml(filepath): 
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    return data

def main():
    yaml_path = '/home/harishankar/Downloads/Coding_challenge/data/B/clmul.yaml'  #for now taken the clmuk.yaml file (by default)

    data = load_yaml(yaml_path)
    print("YAML loaded successfully!\n")
    print(yaml.dump(data, sort_keys=False))

if __name__ == "__main__":
    main()