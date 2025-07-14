# RISC_V-Challenge

![Untitled Diagram(1)](https://github.com/user-attachments/assets/236be8c3-ee92-40db-941d-8a41222856aa)

This project demonstrates a complete round-trip pipeline between YAML instruction data (from the RISC-V Unified Database) and C code. It includes steps for parsing, transforming, generating C headers, and verifying output symmetry via YAML emission.

### DIRECTORY STRUCTURE 

RISC_V-Challenge/
├── data/
│   └── B/                          # Contains multiple .yaml instruction files (e.g., andn.yaml)
├── src/                           # Source directory for Python and C implementations
│   ├── One.py                     # Step 1: Reads a YAML file
│   ├── Second.py                  # Step 2: Emits a C header file from YAML
│   ├── Third.c                    # Step 3: C program that includes the header and prints data
│   ├── Fourth.c                   # Step 4: Emits YAML from the C struct
│   ├── Test1_with_newly_generated_yaml.py
│   ├── Test2_with_newly_generated_yaml.py
│   ├── Test3_with_newly_generated_yaml.c
└── output/                        # Contains generated header, output YAML, and verification data

🔁 Workflow Breakdown
 Step 1: Parse YAML (One.py)

    Reads one .yaml instruction file from data/B/

    Parses it using PyYAML and prints the content

 Step 2: Generate C Header (Second.py)

    Takes the parsed YAML

    Emits a C header file (instruction_<mnemonic>.h)

    Header defines a typedef struct for the instruction and a static instance

Step 3: Use Header in C (Third.c)

    Includes the generated .h file

    Prints the contents of the instruction to stdout

Step 4: Emit YAML from C (Fourth.c)

    C program that reconstructs the YAML structure from the Instruction struct

    Useful for checking correctness of the round-trip conversion


Step 5: Looping steps 1-4.
a) Test1_with_newly_generated_yaml.py

    Acts like One.py but uses the YAML emitted from Step 4 as input

b) Test2_with_newly_generated_yaml.py

    Like Second.py, generates a new C header from the new YAML

c) Test3_with_newly_generated_yaml.c

    C program that uses the regenerated header

    Ensures output YAML matches the one from Step 4

### OUTPUT
All intermediate and final outputs, including:

    Generated .h headers

    C output logs

    Final YAML files

...are saved in the output/ folder for easy comparison and verification.

