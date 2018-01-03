import re
import string
from typing import Set, Dict, Sequence, List
from uuid import uuid4

__author__ = "Bogdan Gladyshev"
__copyright__ = "Copyright 2017, Bogdan Gladyshev"
__credits__ = ["Bogdan Gladyshev"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Bogdan Gladyshev"
__email__ = "siredvin.dark@gmail.com"
__status__ = "Production"

__all__ = ['TodoEntry', 'DEFAULT_EMPTY_PRIORITY']


TODO_TXT_PRIORITY_REGEX = re.compile(r'\([A-Z]\)')
TODO_TXT_PRIORITY_EXTENDED_REGEX = re.compile(r'\([A-Z]\)\s')
TODO_TXT_DATE_FORMAT = re.compile(r'\d{4}-\d{2}-\d{2}')
DEFAULT_EMPTY_PRIORITY = 'ZZZ'


class TodoEntry:  # pylint: disable=too-many-instance-attributes

    __slots__ = [
        '_full_text', '_projects', '_contexts', '_tags',
        '_priority', '_completed_date', '_created_date',
        '_completed'
    ]

    def __init__(  # pylint: disable=too-many-arguments
            self, full_text: str) -> None:
        self._full_text: str = full_text.strip()
        self._projects: Set[str] = set()
        self._contexts: Set[str] = set()
        self._completed: bool = False
        self._completed_date: str = None
        self._created_date: str = None
        self._tags: Dict[str, str] = {}
        self._priority: str = None
        self._load_text()

    def _load_text(self) -> None:
        tokenized_entries: List[str] = self._full_text.split(' ')
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
    def completed(self) -> bool:
        return self._completed

    @completed.setter
    def completed(self, value: bool) -> None:
        if self._completed != value:
            if value:
                self._full_text = f"x {self._full_text}"
            else:
                self._full_text = self._full_text[2:]
            self._completed = value

    @property
    def priority(self) -> str:
        return self._priority

    @priority.setter
    def priority(self, priority: str) -> None:
        if priority is not None and priority not in string.ascii_uppercase:
            raise ValueError("Priority should be one upper case english letter")
        if priority is None:
            if self._priority is not None:
                self._full_text = TODO_TXT_PRIORITY_EXTENDED_REGEX.sub("", self._full_text, count=1)
        else:
            if self._priority is not None:
                self._full_text = TODO_TXT_PRIORITY_REGEX.sub(f"({priority})", self._full_text, count=1)
            else:
                if self._completed:
                    self._full_text = self._full_text.replace('x', f"x ({priority})", 1)
                else:
                    self._full_text = f"({priority}) {self._full_text}"
        self._priority = priority

    @property
    def projects(self) -> Set[str]:
        return self._projects

    @property
    def contexts(self) -> Set[str]:
        return self._contexts

    @property
    def tags(self) -> Dict[str, str]:
        return self._tags

    @property
    def completed_date(self) -> str:
        return self._completed_date

    @completed_date.setter
    def completed_date(self, value: str) -> None:
        if not self._completed:
            raise ValueError("Please, complete todo entry first")
        if not self._created_date:
            raise ValueError("Cannot set completed_date without created_date")
        if self._completed_date:
            self._full_text = self._full_text.replace(self._completed_date, value, 1)
        else:
            self._full_text = self._full_text.replace(
                self._created_date, f"{value} {self._created_date}", 1
            )
        self._completed_date = value

    @property
    def created_date(self) -> str:
        return self._created_date

    @created_date.setter
    def created_date(self, value: str) -> None:
        if self._created_date:
            if self._completed_date == self._created_date:
                self._full_text = self._full_text.replace(self._created_date, value, 2)
                self._full_text = self._full_text.replace(value, self._completed_date, 1)
            else:
                self._full_text = self._full_text.replace(self._created_date, value, 1)
        else:
            if self._priority:
                self._full_text = self._full_text.replace(
                    f"({self._priority})",
                    f"({self._priority}) {value}",
                    1
                )
            else:
                if self._completed:
                    self._full_text = self._full_text.replace('x', f"x {value}", 1)
                else:
                    self._full_text = f"{value} {self._full_text}"
        self._created_date = value

    def add_project(self, project: str) -> None:
        self._projects.add(project)
        self._full_text = f'{self._full_text} +{project}'

    def add_context(self, context: str) -> None:
        self._contexts.add(context)
        self._full_text = f'{self._full_text} @{context}'

    def add_tag(self, key: str, value: str) -> None:
        tag = f"{key}:{value}"
        self._tags[key] = value
        self._full_text = f'{self._full_text} {tag}'

    def merge_with_issue(self, issue: 'TodoEntry') -> None:
        self.priority = min(self.priority or DEFAULT_EMPTY_PRIORITY, issue.priority or DEFAULT_EMPTY_PRIORITY)
        if self.priority == DEFAULT_EMPTY_PRIORITY:
            self.priority = None
        self.projects |= issue.projects
        self.contexts |= issue.contexts
        self.completed = issue.completed or self.completed
        for tag_name, tag_value in issue.tags.items():
            if tag_name in self.tags:
                if self.tags.get(tag_name) != tag_value:
                    self.add_tag(f'{tag_name}-{str(uuid4())}', tag_value)
            else:
                self.add_tag(tag_name, tag_value)

    def merge_with_issues(self, issues: Sequence['TodoEntry']) -> None:
        for issue in issues:
            self.merge_with_issue(issue)

    def __eq__(self, other) -> bool:
        return str(self) == str(other)

    def __hash__(self) -> int:
        return hash(self._full_text)

    def __str__(self) -> str:
        return self._full_text

    def __repr__(self) -> str:
        return self._full_text