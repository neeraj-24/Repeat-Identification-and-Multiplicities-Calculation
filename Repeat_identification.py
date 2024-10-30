#!/usr/bin/env python3

import re
import os

def parse_alignment_file(file_path):
    alignments = []
    
    # Extraction of coordinates and sequences
    pattern = re.compile(r"Alignment: Seq1\((\d+), (\d+)\): (\w+)\s+Seq2\((\d+), (\d+)\): (\w+)")
    
    with open(file_path, 'r') as file:
        content = file.read()
        matches = pattern.findall(content)
        
        for match in matches:
            seq1_start, seq1_end, seq1_seq, seq2_start, seq2_end, seq2_seq = match
            alignments.append({
                'Seq1': {'start': int(seq1_start), 'end': int(seq1_end), 'sequence': seq1_seq},
                'Seq2': {'start': int(seq2_start), 'end': int(seq2_end), 'sequence': seq2_seq}
            })
    
    return alignments

def match_query_to_templates(query_alignment, templates, min_length):
    matched_sequences = []
    
    query_seq1 = query_alignment['Seq1']['sequence']
    query_seq2 = query_alignment['Seq2']['sequence']
    
    query_seq1_len = len(query_seq1)
    query_seq2_len = len(query_seq2)
    
    # Query sequence analysis
    if query_seq1_len < min_length or query_seq2_len < min_length:
        return matched_sequences
    
    # Iteration overh all template alignments and compare both Seq1 and Seq2 from query to Seq1 and Seq2 in the template
    for template_alignment in templates:
        template_seq1 = template_alignment['Seq1']['sequence']
        template_seq2 = template_alignment['Seq2']['sequence']
        
        # Checking for matches by comparing lengths and characters between Seq1/Seq2 from query to Seq1/Seq2 in template
        if len(template_seq1) == query_seq1_len and template_seq1 == query_seq1:
            matched_sequences.append({
                'sequence': template_seq1,
                'coordinates': (template_alignment['Seq1']['start'], template_alignment['Seq1']['end']),
                'seq_type': 'Seq1'
            })
        if len(template_seq2) == query_seq1_len and template_seq2 == query_seq1:
            matched_sequences.append({
                'sequence': template_seq2,
                'coordinates': (template_alignment['Seq2']['start'], template_alignment['Seq2']['end']),
                'seq_type': 'Seq2'
            })
        if len(template_seq1) == query_seq2_len and template_seq1 == query_seq2:
            matched_sequences.append({
                'sequence': template_seq1,
                'coordinates': (template_alignment['Seq1']['start'], template_alignment['Seq1']['end']),
                'seq_type': 'Seq1'
            })
        if len(template_seq2) == query_seq2_len and template_seq2 == query_seq2:
            matched_sequences.append({
                'sequence': template_seq2,
                'coordinates': (template_alignment['Seq2']['start'], template_alignment['Seq2']['end']),
                'seq_type': 'Seq2'
            })
    
    return matched_sequences

def write_repeats_to_files(repeats, output_dir):
    # Output directory creation and saving the repeats
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for idx, repeat in enumerate(repeats, start=1):
        file_name = f"{output_dir}/repeat_{idx}.txt"
        with open(file_name, 'w') as f:
            f.write(f">Repeat {idx}\n")
            f.write(f"Sequence: {repeat['sequence']}\n")
            f.write(f"Coordinates: {repeat['coordinates']}\n")
            f.write(f"Source: {repeat['seq_type']}\n")

# Main
def main():
    file_path = '/path/to/your/Parsed_yass_output_file.txt'  # Define input file 
    output_dir = '/path/to/your/identified_repeat_output_directory'  # Predefined output directory
    min_length = int(input("Enter the minimum sequence length threshold: "))  # Sequence length threshold
    
    print("Reading alignments from file...")
    alignments = parse_alignment_file(file_path)
    print(f"Total alignments found: {len(alignments)}")
    
    repeats = []
    
    # Code interation select query
    for idx, query_alignment in enumerate(alignments):
        print(f"\nProcessing query alignment {idx + 1}...")
        
        # Code iteration when other alignments become templates against selected query
        templates = alignments[:idx] + alignments[idx + 1:]
        
        matches = match_query_to_templates(query_alignment, templates, min_length)
        
        if matches:
            print(f"Found {len(matches)} matching sequences for query alignment {idx + 1}")
            repeats.extend(matches)
    
    # Save matched sequences (repeats) to files
    if repeats:
        print(f"\nWriting {len(repeats)} repeats to files in {output_dir}...")
        write_repeats_to_files(repeats, output_dir)
        print(f"{len(repeats)} repeats saved in the specified directory.")
    else:
        print("No matching repeats found.")


if __name__ == "__main__":
    main()

