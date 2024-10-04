from enum import Enum

class Statuses(Enum):
    New = 'New'
    In_Progress = 'InProgress'
    Pending = 'Pending'
    Blocked = 'Blocked'
    Testing = 'Testing'
    Closed = 'Closed'

    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]
