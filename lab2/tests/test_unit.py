from database import StudentDatabase, Student

def test_userAdd():
    '''Checks if user adds to the database'''
    db = StudentDatabase()
    db.addOrUpdate(Student(1, "Tom"))
    assert len(db._students) == 1

def test_userUpdate():
    '''Checks if user information updates'''
    db = StudentDatabase()
    db.addOrUpdate(Student(1, "Tom"))
    db.addOrUpdate(Student(1, "Ben"))
    assert len(db._students) == 1, "Update adds same value several times"
    assert db._students[0].name == "Ben", "Update doesnt overrides existing value"

def test_userRemove():
    '''Checks if user removes on remove operation'''

    db = StudentDatabase()
    db.addOrUpdate(Student(1, "Tom"))

    db.removeById(1)
    assert len(db._students) == 0
