from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine is the connection between database and python code.
engine = create_engine('sqlite:///:memory:', echo=True)

# Create table
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(Float)


# Create table in memory
Base.metadata.create_all(engine)

# Add data to table
Session = sessionmaker(bind=engine)
session = Session()

student_a = Student(id=1, name='positive', grade=99.9)
student_b = Student(id=2, name='negative', grade=0.1)

session.add_all([student_a, student_b])
session.commit()

students = session.query(Student).all()
for student in students:
    print(f' {student.name} is in grade {student.grade} and his/her id is {student.id}')

session.close()
