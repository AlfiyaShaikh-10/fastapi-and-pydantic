from pydantic import BaseModel, EmailStr, AnyUrl, Field 
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str , Field(max_length= 50, title="name of patient", examples=['Patient1', "patient2"])]
    age: int = Field(lt=120, gt=0)
    email : EmailStr
    linkedin: AnyUrl
    weight : Annotated[float , Field(gt=0 , strict=True)] #//constraints
    married : Annotated[bool, Field(default=None, description="is the patient married or not")] 
    allergies : Optional[List[str]] = Field(max_length = 5)
    contact : Dict[str, str]


dict = {"name": "sneha", "age" : "10" , "email": "test@gmail.com", "linkedin":"http://test.com", "weight": 58.2, "allergies": ["dust", "odour"], "contact": {"phone":"7415201541", "email": "asdf@ghn.cgv" }}
patient1 = Patient(**dict)
print(patient1.name)
print(patient1.age)
print(patient1.weight)
print(patient1.married)
print(patient1.allergies)
print(patient1.contact)

