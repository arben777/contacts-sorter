
from Contact import Contact, CategorizedContact
import pandas as pd
import os
from typing import List

class FileHandler:

    @staticmethod
    def read_files(directory: str) -> List[Contact]:
        data = []
        try:
            for file in os.listdir(directory):
                if file.endswith(('.csv', '.xls', '.xlsx')):
                    path = os.path.join(directory, file)
                    try:
                        df = pd.read_csv(path) if file.endswith('.csv') else pd.read_excel(path)
                        for _, row in df.iterrows():
                            contact = Contact(**row.to_dict())
                            data.append(contact)
                    except Exception as e:
                        print(f"Error reading file {file}: {e}")
        except IOError as e:
            print(f"Error reading files from directory {directory}: {e}")
        return data

    @staticmethod
    def write_to_excel(categorized_contacts: List[CategorizedContact], output_file: str):
        try:
            categorized_data = {}
            for contact in categorized_contacts:
                category = contact.industry
                if category not in categorized_data:
                    categorized_data[category] = []
                categorized_data[category].append(contact.contact.__dict__)

            with pd.ExcelWriter(output_file) as writer:
                for category, contacts in categorized_data.items():
                    df = pd.DataFrame(contacts)
                    df.to_excel(writer, sheet_name=category, index=False)
        except IOError as e:
            print(f"Error writing to Excel file {output_file}: {e}")

