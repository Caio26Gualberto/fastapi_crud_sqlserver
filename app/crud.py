from sqlalchemy.orm import Session
from app.models import Person

def create_person(db: Session, name: str):
    person = Person(name=name)
    db.add(person)
    db.commit()
    db.refresh(person)
    return person

def get_all(db: Session):
    return db.query(Person).all()

def get_by_id(db: Session, person_id: int):
    return db.query(Person).filter(Person.id == person_id).first()

def update_person(db: Session, person_id: int, new_name: str):
    person = get_by_id(db, person_id)
    if person:
        person.name = new_name
        db.commit()
    return person

def delete_person(db: Session, person_id: int):
    person = get_by_id(db, person_id)
    if person:
        db.delete(person)
        db.commit()
    return person