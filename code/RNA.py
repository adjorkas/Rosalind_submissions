# Transcribing DNA into RNA

'''
Given a DNA string t corresponding to a coding strand, its transcribed RNA
string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
'''

# Define the input and output file paths
input_path = r"C:\Users\Lucía\Documents\Cursos\Bioinformática\Rosalind\datasets\rosalind_rna.txt"
output_path = r"C:\Users\Lucía\Documents\Cursos\Bioinformática\Rosalind\outputs\rna_out.txt"

# Read DNA sequence
with open(input_path, "r") as file:
    DNA_seq = file.readline()

# Replace 'T' with 'U' to transcribe DNA to RNA
RNA_seq = DNA_seq.replace("T", "U")

# Write RNA sequence
with open(output_path, "w") as file:
    file.write(RNA_seq)