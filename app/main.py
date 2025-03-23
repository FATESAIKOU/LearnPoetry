from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

todos: List[Todo] = []

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    if any(existing_todo.id == todo.id for existing_todo in todos):
        raise HTTPException(status_code=400, detail="Todo with this ID already exists.")
    todos.append(todo)
    return todo

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found.")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found.")

@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            return todos.pop(index)
    raise HTTPException(status_code=404, detail="Todo not found.")
