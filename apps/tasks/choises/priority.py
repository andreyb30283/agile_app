from enum import Enum

class Priority(Enum):
    LOW = (1, 'low')
    MEDIUM = (2, 'medium')
    HIGH = (3, 'high')
    CRITICAL = (4, 'critical')

    @classmethod
    def choices(cls):
        return [(priority.value[0], priority.value[1]) for priority in cls]

    def __getitem__(self, item):
        return self.value[item]