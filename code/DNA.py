# Counting DNA Nucleotides

'''
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

# Define the input and output file paths
input_path = r"C:\Users\Lucía\Documents\Cursos\Bioinformática\Rosalind\datasets\rosalind_dna.txt"
output_path = r"C:\Users\Lucía\Documents\Cursos\Bioinformática\Rosalind\outputs\dna_out.txt"

# Read DNA sequence
with open(input_path, "r") as file:
    sequence = file.readline()

# Count nucleotides in sequence
counts = [sequence.count(base) for base in "ACGT"]

# Write output
with open(output_path, "w") as file:
    # map() converts into string each element in 'counts'
    # join() joins elements in an iterable into a string, with " " as separator
    file.write(" ".join(map(str, counts)))
