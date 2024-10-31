# Repeat-Identification-and-Multiplicities-Finder
This pipeline provides a Python-based workflow for parsing YASS output (dot-plot), identifying repeat units, and finding their multiplicities. It would benefit the bioinformatics fraternity; this tool can help analyze repeat units in any length of the genome sequences, with applications in immunology, genomics, and related fields.

## Table of Contents

* Overview
* Scripts and Functionality
  1. YASS_Parser
  2. Repeat_identification
  3. Repeat_multiplicities_calculator
* Installation
* Usage
* Dependencies
* Contributions

## Overview
The workflow comprises three scripts, each responsible for a specific part of the repeat identification process:
- Parsing YASS output files and extracting local alignments.
- Identifying potential repeat units from parsed alignments.
- Calculating multiplicities of each identified repeat unit.

## Scripts and Functionality
# 1. YASS_Parser
This script reads YASS output files to extract local alignments. These alignments are filtered based on a minimum length, ensuring that only relevant alignments are considered for downstream repeat identification.

**Key functions:**
- parse_yass_output(): Parses YASS output files, extracting alignments and saving them to a structured format.
- filter_alignments(): Applies a minimum length threshold to select alignments that meet a specific size requirement.

# 2. Repeat_identification
This script uses the alignments extracted from YASS_Parser.py to identify candidate repeat units. It generates all possible substrings of a defined length and stores unique repeat candidates in a dictionary or set for efficient tracking.

**Key functions:**
- generate_candidate_repeats(): Generates substrings of specified lengths from the alignments.
- store_unique_repeats(): Utilizes hashing to store and track unique repeats, efficiently identifying potential repeat units.

# 3. Repeat_multiplicities_calculator
The final script calculates the multiplicity of each identified repeat unit, providing quantitative insights into the recurrence of each repeat across the input sequences.

**Key functions:**
- calculate_multiplicities(): Counts occurrences of each unique repeat, outputting a summary of repeats with their multiplicities.
- export_results(): Saves results to a file or displays them as specified, providing a comprehensive view of repeat distribution.

## Installation
1.  Clone the repository:
   git clone https://github.com/your-username/repeat-identification.git
2.  Navigate to the project directory
   cd repeat-identification

## Usage
- Step 1: Parse YASS output files.
  ('python YASS_Parser.py --input your_yass_output.txt --min_length 50')
- Step 2: Identify candidate repeat units.
  python Repeat_identification.py --input parsed_alignments.txt --min_length 50
- Step 3: Calculate repeat multiplicities
  python Repeat_multiplicities_calculator.py --input candidate_repeats.txt --output repeat_multiplicities.txt
  


