from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    email : EmailStr
    linkedin: AnyUrl
    weight : Optional[float] = None
    married : bool = False
    allergies : List[str]
    contact : Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        domains = [ "hdfc.com", "test.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in domains:
            raise ValueError("Not eligible for discounts")

        return True

    @field_validator('name')
    @classmethod
    def name_transform(cls,value): #default mode=after
        return value.upper()

    @field_validator('age', mode="before")
    @classmethod
    def ageLimits(cls, age):
        if 0 < age < 100:
            return age
        else:
            raise ValueError('age limit exceeds')

dict = {"name": "sneha", "age" : 45 , "email": "test@test.com", "linkedin":"http://test.com", "weight": 58.2, "allergies": ["dust", "odour"], "contact": {"phone":"7415201541", "email": "asdf@ghn.cgv" }}
patient1 = Patient(**dict)
print(patient1.name)
print(patient1.age)
print(patient1.weight)
print(patient1.married)
print(patient1.allergies)
print(patient1.contact)

