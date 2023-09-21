
import openai
from dotenv import load_dotenv
import os
from Contact import Contact , CategorizedContact

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

# Load OpenAI key
load_dotenv()
openai.api_key = os.getenv('OPEN_AI_KEY')

@staticmethod
def categorize_contact(contact: Contact) -> CategorizedContact:
        # Define the function signature for categorize_contact
        functions = [
            {
                "name": "categorize_contact",
                "description": "Categorize a contact based on its details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact": {
                            "type": "object",
                            "description": "The contact to be categorized"
                        }
                    },
                    "required": ["contact"]
                },
                "returns": {
                    "type": "object",
                    "description": "The categorized contact"
                }
            }
        ]


        # Make the initial API call to categorize the contact
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[{"role": "user", "content": f"categorize_contact({contact.to_dict()})"}],
            functions=functions
        )

        # Extract the categorized attributes from the model's response
        function_call = response['choices'][0]['message'].get('function_call')
        if not function_call:
            raise ValueError("The model did not generate a function call")

        attributes = json.loads(function_call['arguments'])
        industry = attributes.get('industry')
        organization = attributes.get('organization')
        seniority = attributes.get('seniority')

        # Ensure the attributes are available, else raise an error
        if not all([industry, organization, seniority]):
            raise ValueError("The model did not provide all required categorized attributes")

        # Return a CategorizedContact object using the attributes provided by GPT
        return CategorizedContact(contact, industry, organization, seniority)
