import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.models import Person

app = FastAPI()

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
session = Session()

session.execute(
    text("""
    INSERT INTO person (name, birthday, password) VALUES
    ("Ronaldo", "2024-12-01", "password1"),
    ("James", "1970-01-01", "password2")
    """)
)

session.commit()

@app.get("unsafe-query/people/{id}")
async def unsafe_get_person(id: int):
    query = session.execute(f"SELECT * FROM person WHERE id = {id}")
    result = session.execute(query)
    return result.one_or_none()

@app.get("safe-query/people/{id}")
async def safe_get_person(id: int):
    person = session.query(Person).filter_by(id=id).one_or_none()
    if person:
        return {repr(person)}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
