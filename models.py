from sqlalchemy import Column, Integer, String
from database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    dob = Column(String)
    contact_number = Column(String)
    contact_address = Column(String)
    education = Column(String)
    graduation_year = Column(Integer)
    years_of_experience = Column(Integer)
    skills = Column(String)
    resume_filename = Column(String)