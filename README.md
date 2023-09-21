
# Contact Sorter Program

## Overview
The Contact Sorter program reads contact data from various file formats, categorizes each contact based on its attributes using GPT-4, sorts the categorized contacts, and then writes the sorted contacts to a master Excel sheet.

## Data Structures
- `Contact`: Represents the original data/content from each contact's row. It can hold arbitrary attributes and is flexible in its structure.
- `CategorizedContact`: Wraps around a `Contact` object and includes categorized attributes like `industry`, `organization`, and `seniority`.

## Classes and Methods
- `OpenAICaller`: Interacts with the GPT model to categorize contacts.
- `DataProcessor`: Handles the categorization and sorting of contacts.
- `FileHandler`: Manages file operations, reading from and writing to files.

## Usage

### Setting up locally
1. Clone the repository to your local machine.
2. Ensure you have Python installed (Python 3.6 or above recommended).
3. Install the required libraries: `pandas`, `openai`, and `docx`.
   ```
   pip install pandas openai python-docx
   ```
4. Navigate to the directory containing the program.

### Running the Program
1. Place your contact files in the `contact_files` directory. The program supports `.csv`, `.xls`, and `.xlsx` file formats.
2. Run the main script:
   ```
   python main.py
   ```
3. The program will read the contact files, categorize and sort the contacts, and then write the sorted contacts to a master Excel sheet named `master_sheet.xlsx`.
