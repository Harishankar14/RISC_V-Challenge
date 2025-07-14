// C program that includes the C header file generated in step 2.//
#include <stdio.h>
#include "riscv_instruction.h"  // header file generated via program 2 (file name :Second.py)

int main() {
    printf("RISC-V Instructions:\n");
    printf("--------------------\n");
    
    // Iterate through the instructions array
    for (size_t i = 0; i < sizeof(instructions) / sizeof(instructions[0]); i++) {
        printf("Instruction: %s\n", instructions[i].name);
        printf("Opcode: 0x%02x\n", instructions[i].opcode);
        printf("Funct3: 0x%01x\n", instructions[i].funct3);
        printf("Funct7: 0x%02x\n", instructions[i].funct7);
        printf("--------------------\n");
    }
    
    return 0;
}
//-------------------------------------------------------------------------------------//
/*
    The output Received 
    RISC-V Instructions:
    --------------------
    Instruction: clmul
    Opcode: 0x33
    Funct3: 0x1
    Funct7: 0x05
    --------------------


*/
