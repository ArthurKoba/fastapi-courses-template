from fastapi.encoders import jsonable_encoder
from typing import List

from fastapi import Body, Response, HTTPException, status

from core.app import app
from models import Post
from database import db


@app.get("/posts/get", response_model=List[Post])
def list_posts(courseID: str):
    if db["courses"].find_one({"_id": courseID}) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with ID {courseID} not found")
    posts = list(db["posts"].find({"courseID": courseID}))
    return posts


@app.post("/posts/create")
def create_post(post: Post = Body(...)):
    if db["courses"].find_one({"_id": post.course_id}) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with ID {post.course_id} not found")
    new_post = db["posts"].insert_one(
        jsonable_encoder(post)
    )
    created_post = db["posts"].find_one(
        {"_id": new_post.inserted_id}
    )
    return created_post


@app.put("/posts/update", response_model=Post)
def update_book(post: Post = Body(...)):
    if db["posts"].find_one({"_id": post.id}) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {post.id} not found")
    updated_post = jsonable_encoder(post)
    update_result = db["posts"].update_one({"_id": post.id}, {"$set": updated_post})
    if update_result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {post.id} not modified!")
    return updated_post


@app.delete("/posts/delete")
def delete_book(_id: str, response: Response):
    delete_result = db["posts"].delete_one({"_id": _id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {_id} not found")
