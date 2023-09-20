
import logging

class OpenAICallerLogged:
    @staticmethod
    def _construct_prompt(contact):
        try:
            return ""
        except Exception as e:
            logging.error(f"Error constructing API prompt for contact {contact.properties.get('name')}: {str(e)}")
            return ""

    @staticmethod
    def get_contact_attributes(contact):
        try:
            response = {}
            logging.info(f"API call successful for contact {contact.properties.get('name')}.")
            return response
        except Exception as e:
            logging.error(f"API call error for contact {contact.properties.get('name')}: {str(e)}")
            return {}
