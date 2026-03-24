from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os

app = FastAPI()

# 👇 PASTE YOUR RAILWAY URL HERE
DATABASE_URL = "postgresql://postgres:TqyilAwxcyvqBpDFHlhVqLzSgvSqCFbA@centerbeam.proxy.rlwy.net:42446/railway"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

Base.metadata.create_all(bind=engine)

# CREATE
@app.post("/notes")
def create_note(note: dict):
    db = SessionLocal()
    new_note = Note(title=note["title"], content=note["content"])
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

# GET ONE
@app.get("/notes/{id}")
def get_note(id: int):
    db = SessionLocal()
    note = db.query(Note).filter(Note.id == id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Not found")
    return note

# LIST ALL
@app.get("/notes")
def list_notes():
    db = SessionLocal()
    return db.query(Note).all()