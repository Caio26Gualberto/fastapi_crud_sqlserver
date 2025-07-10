from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, crud

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/pessoas/")
def create(name: str, db: Session = Depends(get_db)):
    return crud.create_person(db, name)

@app.get("/pessoas/")
def read_all(db: Session = Depends(get_db)):
    return crud.get_all(db)

@app.get("/pessoas/{person_id}")
def read_one(person_id: int, db: Session = Depends(get_db)):
    person = crud.get_by_id(db, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return person

@app.put("/pessoas/{person_id}")
def update(person_id: int, name: str, db: Session = Depends(get_db)):
    person = crud.update_person(db, person_id, name)
    if not person:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return person

@app.delete("/pessoas/{person_id}")
def delete(person_id: int, db: Session = Depends(get_db)):
    person = crud.delete_person(db, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return {"ok": True}