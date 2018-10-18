import re
import string
from typing import Set, Dict, List
from itertools import count

from .utils import ComparationMock

__author__ = "Bogdan Gladyshev"
__copyright__ = "Copyright 2017, Bogdan Gladyshev"
__credits__ = ["Bogdan Gladyshev"]
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Bogdan Gladyshev"
__email__ = "siredvin.dark@gmail.com"
__status__ = "Production"

__all__ = ['TodoEntry', 'ALWAYS_MAX_MOCK', 'ALWAYS_MIN_MOCK']


TODO_TXT_PRIORITY_REGEX = re.compile(r'\([A-Z]\)')
TODO_TXT_PRIORITY_EXTENDED_REGEX = re.compile(r'\([A-Z]\)\s')
TODO_TXT_DATE_FORMAT = re.compile(r'\d{4}-\d{2}-\d{2}')
ALWAYS_MAX_MOCK = ComparationMock()
ALWAYS_MIN_MOCK = ComparationMock(always_max=False)


class TodoEntry:  # pylint: disable=too-many-instance-attributes

    __slots__ = [
        '_full_text', '_projects', '_contexts', '_tags',
        '_priority', '_completed_date', '_created_date',
        '_completed'
    ]

    def __init__(  # pylint: disable=too-many-arguments
            self, full_text ) :
        self._full_text = full_text.strip()
        self._projects = set()
        self._contexts = set()
        self._completed = False
        self._completed_date = None
        self._created_date = None
        self._tags = {}
        self._priority = None
        self._load_text()

    def _load_text(self) :
        tokenized_entries = self._full_text.split(' ')
        self._completed = self._full_text.startswith('x ')
        self._priority = next(filter(TODO_TXT_PRIORITY_REGEX.match, tokenized_entries), None)
        if self._priority:
            self._priority = self._priority[1]
        self._projects = {x[1:] for x in tokenized_entries if x.startswith('+')}
        self._contexts = {x[1:] for x in tokenized_entries if x.startswith('@')}
        for tokenized_entry in tokenized_entries:
            if tokenized_entry.count(':') == 1 and not tokenized_entry.startswith(':') and not tokenized_entry.endswith(':'):
                key, value = tokenized_entry.split(':')
                self._tags[key] = value
        for index, data_entry in enumerate(filter(TODO_TXT_DATE_FORMAT.match, tokenized_entries)):
            if self._completed and index == 0:
                self._completed_date = data_entry
            elif self._created_date is None:
                self._created_date = data_entry
            else:
                break
        # Swtich date, because competed_date should be used only in case
        # when two dates entries used
        if self._completed_date and not self._created_date:
            self._created_date = self._completed_date
            self._completed_date = None

    @property
    def completed(self) :
        return self._completed

    @completed.setter
    def completed(self, value ) :
        if self._completed != value:
            if value:
                self._full_text = "x " +str(self._full_text)
            else:
                self._full_text = self._full_text[2:]
            self._completed = value

    @property
    def priority(self) :
        return self._priority

    @priority.setter
    def priority(self, priority ) :
        if priority is not None and priority not in string.ascii_uppercase:
            raise ValueError("Priority should be one upper case english letter")
        if priority is None:
            if self._priority is not None:
                self._full_text = TODO_TXT_PRIORITY_EXTENDED_REGEX.sub("", self._full_text, count=1)
        else:
            if self._priority is not None:
                self._full_text = TODO_TXT_PRIORITY_REGEX.sub("({priority})".format(priority=priority), self._full_text, count=1)
            else:
                if self._completed:
                    self._full_text = self._full_text.replace('x', "x ({priority})".format(priority=priority), 1)
                else:
                    self._full_text = "({priority}) {full_text}".format(priority=priority, full_text=self._full_text)
        self._priority = priority

    @property
    def projects(self) :
        return self._projects

    @property
    def contexts(self) :
        return self._contexts

    @property
    def tags(self) :
        return self._tags

    @property
    def completed_date(self) :
        return self._completed_date

    @completed_date.setter
    def completed_date(self, value ) :
        if not self._completed and value is not None:
            raise ValueError("Please, complete todo entry first")
        if not self._created_date and value is not None:
            raise ValueError("Cannot set completed_date without created_date")
        if value is None:
            if self._completed_date is not None:
                self._full_text = self._full_text.replace(str(self._completed_date)+" ", '', 1)
        elif self._completed_date:
            self._full_text = self._full_text.replace(self._completed_date, value, 1)
        else:
            self._full_text = self._full_text.replace(
                self._created_date, "{value} {created_date}".format(value=value, created_date=self._created_date), 1
            )
        self._completed_date = value

    @property
    def created_date(self) :
        return self._created_date

    @created_date.setter
    def created_date(self, value ) :
        if value is None:
            if self._created_date is not None:
                self._full_text = self._full_text.replace("{created_date} ".format(created_date=self._created_date), '', 1)
        elif self._created_date:
            if self._completed_date == self._created_date:
                self._full_text = self._full_text.replace(self._created_date, value, 2)
                self._full_text = self._full_text.replace(value, self._completed_date, 1)
            else:
                self._full_text = self._full_text.replace(self._created_date, value, 1)
        else:
            if self._priority:
                self._full_text = self._full_text.replace(
                    "("+str(self._priority)+")",
                    "("+str(self._priority)+") "+str(value),
                    1
                )
            else:
                if self._completed:
                    self._full_text = self._full_text.replace('x', "x "+str(value), 1)
                else:
                    self._full_text = ""+str(value)+" "+str(self._full_text)
        self._created_date = value

    def add_project(self, project ) :
        self._projects.add(project)
        self._full_text = ''+str(self._full_text)+' +'+str(project)

    def remove_project(self, project ) :
        self._projects.remove(project)
        self._full_text = self._full_text.replace(" +"+str(project), "")

    def add_context(self, context ) :
        self._contexts.add(context)
        self._full_text = ''+str(self._full_text)+' @'+str(context)

    def remove_context(self, context ) :
        self._contexts.remove(context)
        self._full_text = self._full_text.replace(" @"+str(context), "")

    def add_tag(self, key , value ) :
        tag = ""+str(key)+":"+str(value)
        self._tags[key] = value
        self._full_text = ''+str(self._full_text)+' '+str(tag)

    def remove_tag(self, key , value ) :
        self._tags.pop(key, None)
        self._full_text = self._full_text.replace(" "+str(key)+":"+str(value), "")

    def _search_merge_tag_name(self, tag_name ) :
        for index in count():
            new_tag_name = ""+str(tag_name)+"-merge"+str(index)
            if new_tag_name not in self._tags:
                return new_tag_name
        # Impossible to get here, just to fix CQ tools warning
        return tag_name  # pragma: no cover

    def merge(self, entry ) :
        """
        Merge given entry into this one. Merge with processed with next rules:

        1. Choose max priority from original and given entry
        2. All projects from given entry will be added to original
        3. All contexts from given entry will be added to original
        4. All tags from given entry will be added to original
        5. If given entry has same tag with different value, new tag like :code:`tag-merge` will be created with this value.
           If :code:`tag-merge0` already exists, :code:`tag-merge1` will be used and so.
        6. If given or original issue is completed, that result will be completed too.
        7. Select min creation date
        8. Select max completed_date

        :param entry: entry to merge with
        """
        self.priority = min(self.priority, entry.priority, key=lambda x: x or ALWAYS_MAX_MOCK)
        self.created_date = min(self.created_date, entry.created_date, key=lambda x: x or ALWAYS_MAX_MOCK)
        for project in entry.projects:
            if project not in self._projects:
                self.add_project(project)
        for context in entry.contexts:
            if context not in self._contexts:
                self.add_context(context)
        self.completed = entry.completed or self.completed
        if self.completed:
            self.completed_date = max(self.completed_date, entry.completed_date, key=lambda x: x or ALWAYS_MIN_MOCK)
        for tag_name, tag_value in entry.tags.items():
            if tag_name in self.tags:
                if self.tags.get(tag_name) != tag_value:
                    self.add_tag(self._search_merge_tag_name(tag_name), tag_value)
            else:
                self.add_tag(tag_name, tag_value)

    def __eq__(self, other) :
        return str(self) == str(other)

    def __hash__(self) :
        return hash(self._full_text)

    def __str__(self) :
        return self._full_text

    def __repr__(self) :
        return self._full_text
