from fastapi.encoders import jsonable_encoder
from typing import List

from fastapi import Body, Response, HTTPException, status

from core.app import app
from database import db
from models import Course


@app.get("/courses/get", response_model=List[Course])
def list_courses():
    courses = list(db["courses"].find(limit=100))
    return courses


@app.post("/courses/create")
def create_course(course: Course = Body(...)):
    new_course = db["courses"].insert_one(
        jsonable_encoder(course)
    )
    created_course = db["courses"].find_one(
        {"_id": new_course.inserted_id}
    )
    return created_course


@app.put("/courses/update")
def update_course(course: Course = Body(...)):
    if db["courses"].find_one({"_id": course.id}) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with ID {course.id} not found")
    updated_course = jsonable_encoder(course)
    update_result = db["courses"].update_one({"_id": course.id}, {"$set": updated_course})
    if update_result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with ID {course.id} not modified!")
    return updated_course


@app.delete("/courses/delete")
def delete_course(_id: str, response: Response):
    delete_posts_result = db["posts"].delete_many({"courseID": _id})
    delete_result = db["courses"].delete_one({"_id": _id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with ID {_id} not found")
