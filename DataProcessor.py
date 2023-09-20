
class DataProcessor:

    @staticmethod
    def categorize_contacts(contacts: [Contact]) -> [CategorizedContact]:
        return [OpenAICaller.categorize_contact(contact) for contact in contacts]
    
    @staticmethod
    def sort_contacts(categorized_contacts: [CategorizedContact]) -> [CategorizedContact]:
        return sorted(categorized_contacts, key=lambda x: (x.industry, x.organization, -x.seniority))
