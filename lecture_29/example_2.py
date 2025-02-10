from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Create an engine
# pip install sqlalchemy psycopg2
# or
# poetry add sqlalchemy psycopg2

#docker run --name tapi-postgres -e POSTGRES_USER=tapi-admin -e POSTGRES_PASSWORD=mystrongpassword -e POSTGRES_DB=tapi-db -p 5432:5432 -d postgres
engine = create_engine('postgresql://tapi-admin:mystrongpassword@localhost:5432/tapi-db')

# Create a connection
connection = engine.connect()

Base = declarative_base()

Session = sessionmaker(bind=engine)


class University(Base):
    __tablename__ = 'universities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=True)
    students = relationship("Student", back_populates="university")

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    city = Column(String, nullable=True)
    university_id = Column(Integer, ForeignKey('universities.id'), nullable=True)  # Foreign key to University
    university = relationship("University", back_populates="students")

# create tables, if not exists
# Can not detect changes
Base.metadata.create_all(engine)



def main():
    with Session.begin() as session:
        student_1 = Student(name="John Doe", age=25, city="New York")
        university_1 = University(name="NYU", city="New York")
        student_1.university = university_1
        session.add(university_1)
        session.add(student_1)

if __name__ == "__main__":
    main()

