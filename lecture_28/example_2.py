from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

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


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    city = Column(String, nullable=True)

# create tables, if not exists
# Can not detect changes
Base.metadata.create_all(engine)



def main():
    session = Session()
    for i in range(100):
        student_1 = Student(name=f"{i} - John Doe ", age=25, city="New York")
        session.add(student_1)
        if i % 10 == 0:
            session.commit()
        if i == 13:
            raise ValueError("Some error")
    session.commit()

if __name__ == "__main__":
    main()

