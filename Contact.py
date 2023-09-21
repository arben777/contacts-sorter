
class Contact:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_dict(self):
        return self.__dict__.copy()
    
    def __repr__(self):
        return str(self.__dict__)

class CategorizedContact:
    def __init__(self, contact: Contact, industry: str, organization: str, seniority: int):
        self.contact = contact
        self.industry = industry
        self.organization = organization
        self.seniority = seniority
    
    def __repr__(self):
        return str({"contact": self.contact, "industry": self.industry, 
                    "organization": self.organization, "seniority": self.seniority})
