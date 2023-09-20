
import os
import pandas as pd
import logging

class FileHandlerLogged:
    @staticmethod
    def read_files(directory: str):
        data = []
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if filename.endswith('.csv'):
                    df = pd.read_csv(file_path)
                elif filename.endswith('.xls'):
                    df = pd.read_excel(file_path, engine='xlrd')
                elif filename.endswith('.xlsx'):
                    df = pd.read_excel(file_path, engine='openpyxl')
                else:
                    continue
                
                required_columns = ['name', 'email']
                if not all(column in df.columns for column in required_columns):
                    continue
                
                for record in df.to_dict('records'):
                    contact = ContactEnhanced(**record)
                    data.append(contact)
                logging.info(f"Processed file {filename} successfully.")
            except Exception as e:
                logging.error(f"Error processing file {filename}: {str(e)}")
                continue
        return data

    @staticmethod
    def write_to_excel(data, output_file, max_sheets=10):
        if len(data) > max_sheets:
            sorted_categories = sorted(data.keys(), key=lambda x: len(data[x]), reverse=True)
            main_categories = sorted_categories[:max_sheets-1]
            misc_categories = sorted_categories[max_sheets-1:]
            
            data["Miscellaneous"] = []
            for cat in misc_categories:
                data["Miscellaneous"].extend(data.pop(cat))
        
        with pd.ExcelWriter(output_file) as writer:
            for category, contacts in data.items():
                df = pd.DataFrame([contact.properties for contact in contacts])
                df.to_excel(writer, sheet_name=category, index=False)
