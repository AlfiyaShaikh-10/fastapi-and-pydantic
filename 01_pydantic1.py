from pydantic import BaseModel, EmailStr, AnyUrl
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


dict = {"name": "sneha", "age" : "10" , "weight": 58.2, "allergies": ["dust", "odour"], "contact": {"phone":"7415201541", "email": "asdf@ghn.cgv" }}
patient1 = Patient(**dict)
print(patient1.name)
print(patient1.age)
print(patient1.weight)
print(patient1.married)
print(patient1.allergies)
print(patient1.contact)

