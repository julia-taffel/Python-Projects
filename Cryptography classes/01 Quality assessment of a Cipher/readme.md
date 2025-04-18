Algorithm 1: 
1. Create a 64x64 SAC matrix and zero all  
2. Encrypt a random 64-bit input value with the cipher and store the cipher output 
3. In the random input value from step 2 change the bit i and calculate cipher output again then XOR this output with the output from step 2 
4. For each non-zero output bit j increment SAC table at position (i, j) by one 
5. Repeat steps 3 and 4 for all input bits 
6. Repeat the whole process (steps 2 – 5) for 220 times, each time generating a new random input

If SAC criterion is fulfilled, we should expect that each output bit will change 219 times, and the 
distribution of SAC table values will be binomial with the following probabilities of finding values from the five ranges (bins).

For input and output sizes of 64 bits, the SAC table has 64*64 = 4096 entries