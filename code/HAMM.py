# Counting Point Mutations
# Hamming distance: minimum # of substitutions to turn one string into another

'''
Given two strings s and t of equal length, the Hamming distance between s and t,
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t)
'''

# Define the input and output file paths
input_path = r"C:\Users\Lucía\Documents\Cursos\Bioinformática\Rosalind\datasets\rosalind_hamm.txt"
output_path = r"C:\Users\Lucía\Documents\Cursos\Bioinformática\Rosalind\outputs\hamm_out.txt"

# Define variables
sequences = []
hamming = 0

# Read input sequence
with open(input_path, "r") as file:
    for line in file:
        sequences.append(line)

# Calculate hamming distance
for index, nucleotide in enumerate(sequences[0]):
    if sequences[0][index] != sequences[1][index]:
        hamming += 1

# Write output file
with open(output_path, "w") as file:
    file.write(str(hamming))