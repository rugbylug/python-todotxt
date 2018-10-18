from typing import Sequence, List

from .entry import TodoEntry, ALWAYS_MAX_MOCK

__author__ = "Bogdan Gladyshev"
__copyright__ = "Copyright 2017, Bogdan Gladyshev"
__credits__ = ["Bogdan Gladyshev"]
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Bogdan Gladyshev"
__email__ = "siredvin.dark@gmail.com"
__status__ = "Production"

__all__ = ['TodoFile']


class TodoFile:

    def __init__(self, file_link ) :
        self.file_link = file_link
        self.todo_entries = []

    def add_entries(self, entries , with_sort = False, sort_field = 'priority') :
        for entry in entries:
            self.add_entry(entry)
        if with_sort:
            self.sort_entries(sort_field=sort_field)

    def remove_entries(self, entries , with_sort = False, sort_field = 'priority') :
        for entry in entries:
            self.todo_entries.remove(entry)
        if with_sort:
            self.sort_entries(sort_field=sort_field)

    def remove_entry(self, entry , with_sort = False, sort_field = 'priority') :
        self.todo_entries.remove(entry)
        if with_sort:
            self.sort_entries(sort_field=sort_field)

    def add_entry(self, entry , with_sort = False, sort_field = 'priority') :
        self.todo_entries.append(entry)
        if with_sort:
            self.sort_entries(sort_field=sort_field)

    def load(self) :
        with open(self.file_link) as todo_file:
            self.todo_entries.extend(TodoEntry(x) for x in todo_file.readlines())

    def sort_entries(self, sort_field='priority') :
        self.todo_entries = sorted(self.todo_entries, key=lambda x: getattr(x, sort_field) or ALWAYS_MAX_MOCK)

    def save(self, sort_field='priority') :
        self.sort_entries(sort_field=sort_field)
        with open(self.file_link, mode='w') as todo_file:
            for todo_entry in self.todo_entries:
                todo_file.write(str(todo_entry))
                todo_file.write('\n')

    def __str__(self) :
        return "\n".join(map(str, self.todo_entries))
