from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    status: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Arie Kurniawan",
                "email": "hubungi.aja@gmail.com",
                "password": "Sampl3P@ssw0rd",
                "status": "Offline"
            }
        }

class ListUsersModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    status: str = Field(...)