#include <stdio.h>
#include "riscv_instruction.h"

int main() {
    // Open the output file
    FILE *file = fopen("/home/harishankar/Downloads/Coding_challenge/data/B/output.yaml", "w");
    if (file == NULL) {
        fprintf(stderr, "Error: Could not open output.yaml for writing\n");
        return 1;
    }
    
    // Write YAML to file
    fprintf(file, "instructions:\n");
    
    // Iterate through the instructions array
    for (size_t i = 0; i < sizeof(instructions) / sizeof(instructions[0]); i++) {
        fprintf(file, "  - name: %s\n", instructions[i].name);
        fprintf(file, "    opcode: 0x%02x\n", instructions[i].opcode);
        fprintf(file, "    funct3: 0x%01x\n", instructions[i].funct3);
        fprintf(file, "    funct7: 0x%02x\n", instructions[i].funct7);
    }
    
    // Close the file
    fclose(file);
    printf("YAML file written to /home/harishankar/Downloads/Coding_challenge/data/B/output.yaml\n");
    
    return 0;
}