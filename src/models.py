import uuid
from pydantic import BaseModel, Field
from typing import Optional


class Auth(BaseModel):
    token: str = Field(...)

    class Config:
        schema_extra = {
            "example": {"token": "123"}
        }


class Course(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    description: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "3d2f4f04-8e16-45ad-9d7c-73485f737ea8",
                "name": "Course 1"
            }
        }


class Post(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    course_id: str = Field(..., alias="courseID")
    title: str = Field(...)
    body: Optional[str] = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "courseID": "3d2f4f04-8e16-45ad-9d7c-73485f737ea8",
                "title": "Some Title",
                "body": "Some Content"
            }
        }
