from main import run_command
from database import StudentDatabase, Student


def test_userCase():
    '''
    User want to add ~10 students. Then modify 2-3 of them. After modificatinon - pernamently delete 1-2 students. 
    After those operations, system must be able to show information about registered students.
    '''

    #TODO: check this test, read and uncomment parts. Try to understand the purpose of the test and how it is implemented
    #TODO: remove next line. It just shows that this test is not implemented
    #raise NotImplementedError()

    db = StudentDatabase()
    students_data = [(i, "Name " + i) for i in range(10)]



    # TODO: add students to the database running commands
    #for student in students_data:
    #    assert run_command(db, f"add {student[0]} {student[1]}")
   
    # TODO: modify first two students (change their names)
    #students_data[0][1] = "Tom"
    #students_data[1][1] = "Ben"
    #assert run_command(db, f"add 0 Tom")
    #assert run_command(db, f"add 1 Ben")

    # TODO: delete last two students
    #students_data.pop()
    #students_data.pop()
    #assert run_command(db, f"remove 8")
    #assert run_command(db, f"remove 9")

    # TODO: get students from the database and compare if theirs data is same that expected
    #students_from_db = db.list()
    #assert len(students_from_db) == len(students_data)
    #for idx, db_student in enumerate(students_from_db):
    #    assert students_from_db[idx].name == students_data[idx][1]
