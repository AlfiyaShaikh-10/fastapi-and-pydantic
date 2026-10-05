from pydantic import BaseModel, EmailStr, AnyUrl, field_validator

class Address(BaseModel):
    city: str
    state: str
    pin_code: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address  # Ye hai nested model

address_info = {"city": "Gurgaon", "state": "Haryana", "pin_code": "122001"}
address_1 = Address(**address_info)

patient_info = {
    "name": "Nitesh",
    "gender": "Male",
    "age": 30,
    "address": address_1
}
patient_1 = Patient(**patient_info)

# Nested data ko asaani se access karna
print(patient_1.address.city)  # Gurgaon