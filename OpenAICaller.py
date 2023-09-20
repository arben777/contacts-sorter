
import json
import random

class OpenAICaller:

    @staticmethod
    def categorize_contact(contact: Contact) -> CategorizedContact:
        # Mock GPT function call to get categorized attributes
        # In a real-world scenario, you'd replace this with the actual GPT function call
        response = {
            'industry': random.choice(["Tech", "Finance", "Healthcare", "Entertainment"]),
            'organization': random.choice(["OrgA", "OrgB", "OrgC", "OrgD"]),
            'seniority': random.randint(1, 10)
        }
        
        # Create and return a CategorizedContact object
        return CategorizedContact(contact, response['industry'], response['organization'], response['seniority'])
