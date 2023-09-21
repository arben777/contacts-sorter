
import openai
from dotenv import load_dotenv
import os
from Contact import Contact , CategorizedContact

import json
import random

class OpenAICaller:
# Load OpenAI key
    load_dotenv()
    openai.api_key = os.getenv('OPEN_AI_KEY')

    @staticmethod
    def categorize_contact(contact: Contact) -> CategorizedContact:
            # Define the function signature for categorize_contact
            functions = [
                {
                    "name": "categorize_contact",
                    "description": "Get the industry, organization, and seniority from contact information",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "contact": {
                                "type": "string",
                                "description": "The contact to be categorized" ## Fix the GPT fucntion calling  
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
                messages=[{"role": "user", "content": f"What is the industry, organization, and seniority of this contact categorize_contact({contact.to_dict()})?"}],
                functions=functions
            )

            # Extract the categorized attributes from the model's response
            function_call = response['choices'][0]['message'].get('function_call')
            if not function_call:
                raise ValueError("The model did not generate a function call")

            # Print the function call
            print(f"Function Call: {function_call}")

            attributes = json.loads(function_call['arguments'])
            industry = attributes.get('industry')
            organization = attributes.get('organization')
            seniority = attributes.get('seniority')

            # Print the categorized attributes for each contact
            print(f"Categorized attributes for contact: {contact}")
            print(f"Industry: {industry}")
            print(f"Organization: {organization}")
            print(f"Seniority: {seniority}")

            # Ensure the attributes are available, else raise an error
            if not all([industry, organization, seniority]):
                raise ValueError("The model did not provide all required categorized attributes")

            # Return a CategorizedContact object using the attributes provided by GPT
            return CategorizedContact(contact, industry, organization, seniority)
