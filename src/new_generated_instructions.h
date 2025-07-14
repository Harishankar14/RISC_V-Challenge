#ifndef RISCV_INSTRUCTION_H
#define RISCV_INSTRUCTION_H

// Auto-generated C header from RISC-V YAML

typedef struct {
    const char *name;
    unsigned int opcode;
    unsigned int funct3;
    unsigned int funct7;
} riscv_instruction_t;

static const riscv_instruction_t instructions[] = {
    { "clmul", 0x33, 0x0, 0x0 },
};

#endif // RISCV_INSTRUCTION_H
