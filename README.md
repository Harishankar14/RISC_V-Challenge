# RISC_V-Challenge

![Untitled Diagram(1)](https://github.com/user-attachments/assets/236be8c3-ee92-40db-941d-8a41222856aa)

This Repo Majorly Contains the Files 

1. Data
   Under Data I have extracted the folder B which accompanies more than one .yaml files. Source taken: (https://github.com/riscv-software-src/riscv-unified-db)

2. Second Most Important file directory is nothing but the '''src'''
   This folder is divided into different Files both python and c files.


### Jumping into the src files in detail.

1. One.py
   This file has python code which majorly reads at least one of the YAML files in the RISC-V Unified Database project.

2.Second.py 

  In this file, Same Python program then emits the data in the YAML file as a C header file, format of your choosing. 


3. Third.c

   One of the important files, so this file is nothing but a C implementation  that includes the C header file generated in step 2 or from Second.py

4.Fourth.c 

  Another C Implementation, where  program should emit the contents of the C header file in YAML. The YAML file does NOT need to match the original YAML file.


### 5TH STEP IN DETAIL...

5th Step was nothing but to repeat the first four steps, inorder to do so the files have been named in a unique way. 

a) '''Test1_with_newly_generated_yaml.py''': (same as One.py) but the yaml file used is taken from the input of step 4 (for testing on new .yaml file)

b) '''Test2_with_newly_generated_yaml.py''': (same as Second.py) but with a new_generated_instruction.h file. (from  the new .yaml file)

c ''' Test3_with_newly_generated_yaml.c''': ( here again we obtain the header file) verifying for the correction and making sure it is the same as that. 


### output 

Output file, basically consist of all the expected output of each files, majorly, inorder to verify the following.



Thank You :) 

