from typing import Sequence, List

from .entry import TodoEntry, EMPTY_PRIORITY_MOCK

__author__ = "Bogdan Gladyshev"
__copyright__ = "Copyright 2017, Bogdan Gladyshev"
__credits__ = ["Bogdan Gladyshev"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Bogdan Gladyshev"
__email__ = "siredvin.dark@gmail.com"
__status__ = "Production"

__all__ = ['TodoFile']


class TodoFile:

    def __init__(self, file_link: str) -> None:
        self.file_link = file_link
        self.todo_entries: List[TodoEntry] = []

    def add_entries(self, entries: Sequence[TodoEntry], with_sort: bool = False, sort_field: str = 'priority') -> None:
        for entry in entries:
            self.add_entry(entry)
        if with_sort:
            self.sort_entries(sort_field=sort_field)

    def remove_entries(self, entries: Sequence[TodoEntry], with_sort: bool = False, sort_field: str = 'priority') -> None:
        for entry in entries:
            self.todo_entries.remove(entry)
        if with_sort:
            self.sort_entries(sort_field=sort_field)

    def remove_entry(self, entry: TodoEntry, with_sort: bool = False, sort_field: str = 'priority') -> None:
        self.todo_entries.remove(entry)
        if with_sort:
            self.sort_entries(sort_field=sort_field)

    def add_entry(self, entry: TodoEntry, with_sort: bool = False, sort_field: str = 'priority') -> None:
        self.todo_entries.append(entry)
        if with_sort:
            self.sort_entries(sort_field=sort_field)

    def load(self) -> None:
        with open(self.file_link) as todo_file:
            self.todo_entries.extend(TodoEntry(x) for x in todo_file.readlines())

    def sort_entries(self, sort_field='priority') -> None:
        self.todo_entries = sorted(self.todo_entries, key=lambda x: getattr(x, sort_field) or EMPTY_PRIORITY_MOCK)

    def save(self, sort_field='priority') -> None:
        self.sort_entries(sort_field=sort_field)
        with open(self.file_link, mode='w') as todo_file:
            for todo_entry in self.todo_entries:
                todo_file.write(str(todo_entry))
                todo_file.write('\n')

    def __str__(self) -> str:
        return "\n".join(map(str, self.todo_entries))
