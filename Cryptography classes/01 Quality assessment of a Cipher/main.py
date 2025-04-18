import numpy as np
import random
from Crypto.Cipher import Blowfish, AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from tkinter import ttk
import tkinter as tk

def matrix_generator(x=64):
    sac_matrix = np.zeros((x, x), dtype=int)
    return sac_matrix

def input_generator():
    return random.getrandbits(64)

def encryption(value, key, cipher_type):
    if cipher_type == "Blowfish":
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    elif cipher_type == "AES":
        cipher = AES.new(key, AES.MODE_ECB)
    elif cipher_type == "DES":
        cipher = DES.new(key, DES.MODE_ECB)
    else:
        raise ValueError("Unsupported cipher")
    
    #iv = cipher.iv
    padded_value = pad(value.to_bytes(8, 'big'), cipher.block_size)
    #ciphertext = iv + cipher.encrypt(padded_value)
    return cipher.encrypt(padded_value)

def bit_change(value, index):
    return value ^ 1 << index

def sac_analysis(input_value, key, sac_matrix, cipher_type):
    encrypted_value1 = encryption(input_value, key, cipher_type)
    for i in range(64):
        modified_value = bit_change(input_value, i)
        encrypted_value2 = encryption(modified_value, key, cipher_type)
        xor_result = bytes(a ^ b for a, b in zip(encrypted_value1, encrypted_value2))
        for j in range(64):
            bit = (xor_result[j // 8] >> (7 - (j % 8))) & 1
            if bit:
                sac_matrix[i, j] += 1    
    return sac_matrix
                
def sac_matrix_analysis(iterations = 2**20, cipher_type="Blowfish"):
    sac_matrix = matrix_generator()
    key = get_random_bytes(16 if cipher_type == "AES" else 8)
    for _ in range(iterations):
        input_value = input_generator()
        sac_analysis(input_value, key, sac_matrix, cipher_type)
    return sac_matrix

def show_results(sac_matrix):
    window = tk.Tk()
    window.title("SAC Test Results")
    
    table = ttk.Treeview(window, columns=("Bin", "Probability", "Expected number", "Counted number"), show="headings")
    table.heading("Bin", text="Bin")
    table.heading("Probability", text="Probability")
    table.heading("Expected number", text="Expected Number")
    table.heading("Counted number", text="Counted Number")
                    
    probability =[0.200224, 0.199937, 0.199677, 0.199937, 0.200224]
    Expected_number = [820, 819, 818, 819, 820]
    Counted_number = [0, 0, 0, 0, 0]
    Bin = [1, 2, 3, 4, 5]
    
    for i in range(64):
        for j in range(64):
            if sac_matrix[i, j] <= 523857:
                Counted_number[0] += 1
            elif sac_matrix[i, j] >= 523858 and sac_matrix[i, j] <= 524158:
                Counted_number[1] += 1
            elif sac_matrix[i, j] >= 524159 and sac_matrix[i, j] <= 524417:
                Counted_number[2] += 1
            elif sac_matrix[i, j] >= 524418 and sac_matrix[i, j] <= 524718:
                Counted_number[3] += 1
            else:
                Counted_number[4] += 1

    for i in range(5):
        table.insert("", tk.END, values=(Bin[i], probability[i], Expected_number[i], Counted_number[i]))
    
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=table.yview)
    table.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
            
    table.pack(fill=tk.BOTH, expand=True)
    window.mainloop()

if __name__ == "__main__":
    cipher_type = "Blowfish"
    sac_matrix = sac_matrix_analysis(iterations=2**20, cipher_type=cipher_type)
    print(sac_matrix)
    show_results(sac_matrix)
    

