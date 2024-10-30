import re

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence

def parse_yass_output(file_path, seq1, seq2, min_length):
    alignments = []
    with open(file_path, 'r') as file:
        content = file.read()

        # Find all alignment blocks
        alignment_blocks = re.findall(r"\*\((\d+)-(\d+)\)\((\d+)-(\d+)\)", content)

        for block in alignment_blocks:
            start1, end1, start2, end2 = map(int, block)
            length = min(end1 - start1, end2 - start2)
            
            if length >= min_length:
                aligned_seq1 = seq1[start1-1:end1]  # -1 to adjust for 0-based index
                aligned_seq2 = seq2[start2-1:end2]
                alignments.append((aligned_seq1, start1, end1, aligned_seq2, start2, end2))
    
    return alignments

def print_alignments(alignments):
    for alignment in alignments:
        print(f"Alignment: Seq1({alignment[1]}, {alignment[2]}): {alignment[0]}")
        print(f"           Seq2({alignment[4]}, {alignment[5]}): {alignment[3]}")
        print()

# User-defined file paths and minimum length
fasta1_path = "/path/to/your/file.fasta"
fasta2_path = "/path/to/your/file.fasta"
yass_output_path = "/path/to/your/yass_output.txt"
min_length = 3  # Set your desired minimum alignment length

# Read the sequences from FASTA files
seq1 = read_fasta(fasta1_path)
seq2 = read_fasta(fasta2_path)

# Parse the YASS output and get the alignments
alignments = parse_yass_output(yass_output_path, seq1, seq2, min_length)

# Print the results
print_alignments(alignments)

