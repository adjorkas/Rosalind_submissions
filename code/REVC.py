# Complementing a Strand of DNA

'''
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s
'''

# Define the input and output file paths
input_path = r"C:\Users\Lucía\Documents\Cursos\Bioinformática\Rosalind\datasets\rosalind_revc.txt"
output_path = r"C:\Users\Lucía\Documents\Cursos\Bioinformática\Rosalind\outputs\revc_out.txt"

# Read input sequence
with open(input_path, "r") as file:
    strand_A = file.readline().strip()

# Create a dictionary that maps each DNA base to its complementary base
complimentary_base = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# Read strand_A bases in reverse order, find complimentary, and join into string
strand_B = "".join([complimentary_base[base] for base in strand_A[::-1]])

# Write output sequence
with open(output_path, "w") as file:
    file.write(strand_B)
    