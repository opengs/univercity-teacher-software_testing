from database import Student, StudentDatabase


def _print_help():
    print("add <id> <name> - adds user to the database or updates its current information")
    print("remove <id> - remove user from the database")
    print("list - list all the users and theirs information")
    print("quit - quits the program")
    print("")

def run_command(db: StudentDatabase, cmd: str) -> bool:
    '''Validates command and runs it. If everything ok - returns True. If there is validation error - returns False'''

    cmd_splits = cmd.split(" ")
    if cmd_splits[0] == "add":
        if len(cmd_splits) != 3: return False
        db.addOrUpdate(Student(cmd_splits[1], cmd_splits[2]))
    elif cmd_splits[0] == "remove":
        # TODO: maybe here we have to check if it has two elements??
        db.removeById(cmd_splits[1])
    elif cmd_splits[0] == "list":
        print(db.list())
    else:
        return False
    
    # Everything is ok
    return True

def main():
    print("This is the \"Fire Student\" database! How can i help?")
    _print_help()

    db = StudentDatabase()

    # Start main loop. Read and execute commands
    while True:
        cmd = input(">>>")
        if cmd == "quit": break
        run_command(db, cmd)

    print("Bye! :)")

if __name__ == "__main__":
    main()