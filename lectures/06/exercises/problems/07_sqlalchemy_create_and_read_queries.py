"""Problem 07: Create and read data with SQLAlchemy.

Task:
1. Open a SQLAlchemy Session on `school.db`.
2. Create one Assignment for an existing student.
3. Read all students.
4. Read students with age >= 22 sorted by age descending.
5. Read assignments with joined student names.

Starter:
- Reuse `Student` and `Assignment` from `db_models.py`.
- Use `select(...)` queries.
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db_models import Assignment, Student

DB_URL = "sqlite:///C:/Users/amal_/harbour.space/school.db"
#couldnt get it to work because of database issues but i think code is correct

def main() -> None:
    engine=create_engine(DB_URL, echo=False)

    with Session(engine) as session:


        student = session.execute(
            select(Student).where(Student.email=="ana@example.com")
        ).scalar_one()

        new_assignment = Assignment(
            title="SQL Homework",
            score=95,
            student_id=student.id,
        )

        session.add(new_assignment)


        print("ALL STUDENTS")
        students=session.execute(select(Student)).scalars().all()
        for s in students:
            print(s.id,s.name,s.age,s.email,s.track)


        print("\nAGE >= 22 (DESC)")
        filtered=session.execute(
            select(Student)
            .where(Student.age>=22)
            .order_by(Student.age.desc())
        ).scalars().all()

        for s in filtered:
            print(s.name,s.age)


        print("\nASSIGNMENTS WITH STUDENTS")
        assignments=session.execute(select(Assignment)).scalars().all()

        for a in assignments:
            print(a.title,a.score,"->",a.student.name)

        session.commit()




if __name__ == "__main__":
    main()
