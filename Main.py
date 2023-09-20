from FileHandler import FileHandler
from DataProcessor import DataProcessor
from OpenAICaller import OpenAICaller

# Read files
contacts = FileHandler.read_files('contact_files')

# Categorize contacts
categorized_contacts = DataProcessor.categorize_contacts(contacts)

# Sort contacts
sorted_contacts = DataProcessor.sort_contacts(categorized_contacts)

# Write to Excel
FileHandler.write_to_excel(sorted_contacts, 'master.xlsx')