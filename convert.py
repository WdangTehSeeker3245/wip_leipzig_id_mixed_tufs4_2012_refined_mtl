import csv

# Load the txt file content
file_path = 'ind_mixed-tufs4_2012_300K-sources.txt'  # Update with the actual file path
output_csv_path = 'leipzig_id_mixed_tufs4_2012_sources.csv'  # Update with the actual output path

# Function to extract the right-hand side text after the tab or space
def extract_right_side(text):
    # Check if there is a tab or just space to split properly
    if '\t' in text:
        return text.split('\t')[1].strip()
    else:
        return text.split(maxsplit=1)[1].strip()  # Fallback for lines without tabs

# Read the txt file and extract the right-hand side of each line
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Extract right-side sentences
right_side_sentences = [extract_right_side(line) for line in lines]

# Save to CSV
with open(output_csv_path, mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['text'])  # Write header
    for sentence in right_side_sentences:
        writer.writerow([sentence])

print(f"Processed file saved to: {output_csv_path}")
