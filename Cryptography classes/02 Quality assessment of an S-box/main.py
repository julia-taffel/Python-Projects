from itertools import product
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

def read_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    no_zeros = data[0::2]
    if len(no_zeros) != 256:
        raise ValueError("Expected 256 non-zero bytes")
    return no_zeros

def extract_functions(sbox_data):
    functions = [[] for _ in range(8)]
    for i in sbox_data:
        bit = format(i, '08b')
        for j in range(8):
            functions[j].append(int(bit[j]))
    return functions

def check_balance(functions):
    for i in functions:
        a = 0
        for j in i:
            if j == 1:
                a += 1
        #print("Number of 1 in a function:", a)

def generate_affine_functions(n=8):
    affine_functions = []
    for coeffs in product([0, 1], repeat=n+1):  # a_0 to a_n
        func = []
        for x in range(2**n):
            x_bits = [(x >> i) & 1 for i in reversed(range(n))]
            val = coeffs[0]  # a_0
            for j in range(n):
                val ^= coeffs[j+1] & x_bits[j]
            func.append(val)
        affine_functions.append(func)
    return affine_functions

def hamming_distance(f, g):
    return sum([bit_f != bit_g for bit_f, bit_g in zip(f, g)])

def compute_nonlinearity(functions):
    affine_functions = generate_affine_functions(n=8)
    nonlinearities = []
    for f in functions:
        min_distance = min(hamming_distance(f, aff) for aff in affine_functions)
        nonlinearities.append(min_distance)
    return nonlinearities

def check_sac(functions, n=8):
    results = []
    for f_index, f in enumerate(functions):
        sac_total = 0
        total_checks = 0
        for i in range(n):  # flip each bit
            changes = 0
            for x in range(2**n):
                flipped_x = x ^ (1 << (n - 1 - i))  # flip i-th bit
                changes += f[x] ^ f[flipped_x]
            total_checks += 2**n
            sac_total += changes
        sac_ratio = sac_total / total_checks
        results.append(sac_ratio)
    return results

def xor_profile(sbox_data):
    matrix = np.zeros((256, 256), dtype=int)
    
    for i in range(256):
        for j in range(256):
            
            values1 = sbox_data[i]
            values2 = sbox_data[j]
            
            result = values1 ^ values2
            val = i ^ j
            matrix[result][val] += 1
    
    flat_matrix = matrix.flatten()
    maximum = np.max(flat_matrix[1:])
    #print("XOR profile is equal to:", maximum)
    return maximum
    
def cycles(sbox_data):
    visited = [False] * 256
    cycle_count = 0

    for i in range(256):
        if not visited[i]:
            cycle_count += 1
            current = i
            while not visited[current]:
                visited[current] = True
                current = sbox_data[current]
    
    #print(f"Number of cycles in S-box: {cycle_count}")
    return cycle_count

def comparison(n_sboxes=5, reference=None):
    results = []
    
    def analysis(sbox, name=""):    
        functions = extract_functions(sbox)
        balance = [f.count(1) for f in functions]
        nonlinearity = compute_nonlinearity(functions)
        sac = check_sac(functions)
        maximum = xor_profile(sbox)
        cycle = cycles(sbox)
        
        return {
            "S-box": name,
            "Avg Balance": sum(balance)/8,
            "Min Nonlinearity": min(nonlinearity),
            "Avg Nonlinearity": sum(nonlinearity)/8,
            "Avg SAC": sum(sac)/8,
            "XOR Profile Max": maximum,
            "Cycle Count": cycle
        }
        
    if reference is not None:
        results.append(analysis(reference, name="Original"))
        
    for i in range(n_sboxes):
        sbox = list(range(256))
        random.shuffle(sbox)
        results.append(analysis(sbox, name=f"Random_{i+1}"))
        
    df = pd.DataFrame(results)
    print(df)
    return df 

def plot_sbox_comparison(df):
    plt.style.use('seaborn-v0_8-colorblind')
    x_labels = df["S-box"]

    # Min Nonlinearity
    plt.figure(figsize=(10, 5))
    plt.bar(x_labels, df["Min Nonlinearity"], color="cornflowerblue")
    plt.title("Minimalna nieliniowość S-boxów")
    plt.xlabel("S-box")
    plt.ylabel("Min Nonlinearity")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Avg SAC
    plt.figure(figsize=(10, 5))
    plt.bar(x_labels, df["Avg SAC"], color="lightseagreen")
    plt.axhline(0.5, color="red", linestyle="--", label="Ideal SAC = 0.5")
    plt.title("Średnie SAC (Strict Avalanche Criterion)")
    plt.xlabel("S-box")
    plt.ylabel("Avg SAC")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

filename = "02 Quality assessment of an S-box/sbox.SBX"
sbox_no_zeros = read_file(filename)
functions = extract_functions(sbox_no_zeros)
check_balance(functions)

nonlinearities = compute_nonlinearity(functions)
#print("Nonlinearities:", nonlinearities)

sac_scores = check_sac(functions)
for i, score in enumerate(sac_scores):
    print(f"Function {i}: SAC = {score:.3f}")

xor_profile(sbox_no_zeros)
cycles(sbox_no_zeros)

#comparison(100, sbox_no_zeros)
plot_sbox_comparison(comparison(100, sbox_no_zeros))