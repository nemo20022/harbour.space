"""Problem 04: Practice WHERE, ORDER BY, LIMIT.

Task:
1. Get students with age >= 22
2. Sort students by age DESC
3. Return only top 3 oldest students
4. Get backend students younger than 23

Use parameterized queries for filter values.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()


    cur.execute(
        "SELECT * FROM students WHERE age >= ?",
        (22,),
    )
    rows=cur.fetchall()

    print("AGE >= 22")
    for i in rows:
        print(i)


    cur.execute(
        "SELECT * FROM students ORDER BY age DESC LIMIT 3"
    )
    top=cur.fetchall()

    print("\nTOP 3 OLDEST")
    for j in top:
        print(j)


    cur.execute(
        "SELECT * FROM students WHERE track = ? AND age < ?",
        ("backend",23),
    )
    backend=cur.fetchall()

    print("\nBACKEND AND AGE < 23")
    for k in backend:
        print(k)

    conn.close()



if __name__ == "__main__":
    main()
