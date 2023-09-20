
import pandas as pd
import os

class FileHandler:

    @staticmethod
    def read_files(directory: str) -> [Contact]:
        data = []
        for file in os.listdir(directory):
            if file.endswith(('.csv', '.xls', '.xlsx')):
                path = os.path.join(directory, file)
                df = pd.read_csv(path) if file.endswith('.csv') else pd.read_excel(path)
                for _, row in df.iterrows():
                    contact = Contact(**row.to_dict())
                    data.append(contact)
        return data

    @staticmethod
    def write_to_excel(categorized_contacts: [CategorizedContact], output_file: str):
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
