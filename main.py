from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8080'],
    allow_methods=['*'],
)

class BookSchemas(BaseModel):
    id: str
    title: str
    completed: bool


class BookCreateSchemas(BaseModel):
    title: str


class BookUpdateSchemas(BaseModel):
    book: str


like_books = ""
tasks: list[BookSchemas] = []

@app.get('/favorite')
def read_favorite_book() -> str:
    return f'Любимая книга :{like_books}'


@app.get('/book')
def read_task() ->list[BookSchemas]:
    return tasks


@app.post('/book')
def create_tasks(payload: BookCreateSchemas) -> BookSchemas:
    new_task = BookSchemas(id=str(uuid4()), title=payload.title, completed=False)
    tasks.append(new_task)
    return new_task


@app.post('/favorite')
def favorite_book(payload: BookUpdateSchemas):
    global like_books
    like_books = payload.book
    return {"status": 'ok'}