from fastapi import FastAPI, UploadFile, File, Form,HTTPException
from typing import List,Optional
from uuid import uuid4

app = FastAPI()


candidates = []

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

    candidate = {
        "id": candidate_id,
        "full_name": full_name,
        "dob": dob,
        "contact_number": contact_number,
        "contact_address": contact_address,
        "education": education,
        "graduation_year": graduation_year,
        "years_of_experience": years_of_experience,
        "skills": skills.split(","),
        "resume_filename": resume.filename
    }

    candidates.append(candidate)

    return {"message": "Candidate added successfully", "id": candidate_id}

from typing import Optional

@app.get("/candidates")
def list_candidates(
    skill: Optional[str] = None,
    min_experience: Optional[int] = None,
    graduation_year: Optional[int] = None
):
    filtered_candidates = candidates

    if skill:
        filtered_candidates = [
            c for c in filtered_candidates
            if skill.lower() in [s.strip().lower() for s in c["skills"]]
        ]

    if min_experience is not None:
        filtered_candidates = [
            c for c in filtered_candidates
            if c["years_of_experience"] >= min_experience
        ]

    if graduation_year is not None:
        filtered_candidates = [
            c for c in filtered_candidates
            if c["graduation_year"] == graduation_year
        ]

    return filtered_candidates
@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: str):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate

    raise HTTPException(
        status_code=404,
        detail="Candidate not found"
    )
@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: str):
    for index, candidate in enumerate(candidates):
        if candidate["id"] == candidate_id:
            candidates.pop(index)
            return {"message": "Candidate deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Candidate not found"
    )