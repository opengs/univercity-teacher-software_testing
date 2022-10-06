from main import run_command
from database import StudentDatabase

def test_runAdd():
    db = StudentDatabase()
    assert run_command(db, "add 1 Tom")
    assert len(db.list()) == 1
    assert db.list()[0].name == "Tom"

def test_runAddBadArgument():
    '''If argument for add command is bad - dont add user and return false.'''
    db = StudentDatabase()
    assert run_command(db, "add 1") == False
    assert len(db.list()) == 0

def test_runRemove():
    db = StudentDatabase()
    run_command(db, "add 1 Tom")
    assert run_command(db, "remove 1")
    assert len(db.list()) == 0

def test_runRemoveBadArgument():
    db = StudentDatabase()
    run_command(db, "add 1 Tom")
    assert run_command(db, "remove") == False
    assert len(db.list()) == 1