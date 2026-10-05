from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
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

    @model_validator(mode="after")
    def emerg_Validator(cls, model):
        if model.age > 60 and "emergency" not in model.contact:
            raise ValueError("patients above 60 requires emergency contact")
        return model

dict = {"name": "sneha", "age" : "65" , "email": "test@gmail.com", "linkedin":"http://test.com", "weight": 58.2, "allergies": ["dust", "odour"], "contact": {"emergency":"7415201541", "email": "asdf@ghn.cgv" }}
patient1 = Patient(**dict)
print(patient1.name)
print(patient1.age)
print(patient1.weight)
print(patient1.married)
print(patient1.allergies)
print(patient1.contact)

