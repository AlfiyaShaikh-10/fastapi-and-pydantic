from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    email : EmailStr
    linkedin: AnyUrl
    weight : Optional[float] = None
    height : Optional[float] = None
    married : bool = False
    allergies : List[str]
    contact : Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi_val = round(self.weight / (self.height ** 2), 2)
        return bmi_val 

dict = {"name": "sneha", "age" : "65" , "height":1.72, "email": "test@gmail.com", "linkedin":"http://test.com", "weight": 58.2, "allergies": ["dust", "odour"], "contact": {"emergency":"7415201541", "email": "asdf@ghn.cgv" }}
patient1 = Patient(**dict)
print(patient1.name)
print(patient1.age)
print(patient1.weight)
print(patient1.bmi)
print(patient1.married)
print(patient1.allergies)
print(patient1.contact)

