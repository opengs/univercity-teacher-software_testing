from typing import List
from dataclasses import dataclass


@dataclass
class Student():
    id: int
    name: str

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id

    def __hash__(self) -> int:
        return self.id

class StudentDatabase():
    '''Holds information about students'''
    def __init__(self) -> None:
        self._students: List[Student] = []

    def addOrUpdate(self, student: Student) -> None:
        '''Adds student to the database or updates existing value'''
        # TODO: maybe check if it already exist in list. And if exists - delete?
        self._students.append(student)

    def removeById(self, id: int) -> None:
        '''Removes user from the database using its id'''
        self._students.remove(Student(id, ""))

    def list(self) -> List[Student]:
        '''Returns list of all user'''
        return self._students