"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()


    cur.execute("SELECT COUNT(*) FROM students")
    total=cur.fetchone()[0]
    print("total students:",total)


    cur.execute("SELECT AVG(age) FROM students")
    avg=cur.fetchone()[0]
    print("average age:", avg)


    cur.execute("SELECT MIN(age),MAX(age) FROM students")
    mina,maxa = cur.fetchone()
    print("Min age:", mina)
    print("Max age:", maxa)


    cur.execute(
        "SELECT track, COUNT(*) FROM students GROUP BY track"
    )
    rows=cur.fetchall()

    print("\nStudents per track:")
    for track, count in rows:
        print(f"{track}: {count}")

    conn.close()



if __name__ == "__main__":
    main()
