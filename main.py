from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import Optional
from uuid import uuid4

from database import SessionLocal, engine, Base
from models import Candidate

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/candidates")
async def create_candidate(
    full_name: str = Form(...),
    dob: str = Form(...),
    contact_number: str = Form(...),
    contact_address: str = Form(...),
    education: str = Form(...),
    graduation_year: int = Form(...),
    years_of_experience: int = Form(...),
    skills: str = Form(...),
    resume: UploadFile = File(...)
):

    candidate_id = str(uuid4())
    db = SessionLocal() 
    db_candidate = Candidate(
        id=candidate_id,
        full_name=full_name,
        dob=dob,
        contact_number=contact_number,
        contact_address=contact_address,
        education=education,
        graduation_year=graduation_year,
        years_of_experience=years_of_experience,
        skills=skills,
        resume_filename=resume.filename
    )

    db.add(db_candidate)
    db.commit()
    db.close()

    return {"message": "Candidate added successfully", "id": candidate_id}


@app.get("/candidates")
def list_candidates(
    skill: Optional[str] = None,
    min_experience: Optional[int] = None,
    graduation_year: Optional[int] = None
):
    db = SessionLocal()

    candidates = db.query(Candidate).all()

    filtered = []

    for c in candidates:
        if skill and skill.lower() not in c.skills.lower():
            continue
        if min_experience and c.years_of_experience < min_experience:
            continue
        if graduation_year and c.graduation_year != graduation_year:
            continue
        filtered.append(c)

    db.close()

    return filtered


@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: str):
    db = SessionLocal()

    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

    db.close()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return candidate


@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: str):
    db = SessionLocal()

    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

    if not candidate:
        db.close()
        raise HTTPException(status_code=404, detail="Candidate not found")

    db.delete(candidate)
    db.commit()
    db.close()

    return {"message": "Candidate deleted successfully"}