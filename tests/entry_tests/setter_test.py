import unittest

import pytest

from todotxt import TodoEntry
from .test_data import PRIORITY_TEST_TUPLE, COMPLETED_TEST_TUPLE, COMPLETED_DATE_TEST_TUPLE, CREATED_DATE_TEST_TUPLE


@pytest.mark.parametrize("initial_entry, result_entry, priority_value", PRIORITY_TEST_TUPLE)
def test_priority_setter_positive(initial_entry, result_entry, priority_value):
    todo_entry = TodoEntry(initial_entry)
    todo_entry.priority = priority_value
    assert str(todo_entry) == result_entry


@pytest.mark.parametrize("initial_entry, result_entry, completed_value", COMPLETED_TEST_TUPLE)
def test_completed_setter_positive(initial_entry, result_entry, completed_value):
    todo_entry = TodoEntry(initial_entry)
    todo_entry.completed = completed_value
    assert str(todo_entry) == result_entry


@pytest.mark.parametrize("initial_entry, result_entry, completed_date_value", COMPLETED_DATE_TEST_TUPLE)
def test_completed_date_setter_positive(initial_entry, result_entry, completed_date_value):
    todo_entry = TodoEntry(initial_entry)
    todo_entry.completed_date = completed_date_value
    assert str(todo_entry) == result_entry


@pytest.mark.parametrize("initial_entry, result_entry, created_date_value", CREATED_DATE_TEST_TUPLE)
def test_created_date_setter_positive(initial_entry, result_entry, created_date_value):
    todo_entry = TodoEntry(initial_entry)
    todo_entry.created_date = created_date_value
    assert str(todo_entry) == result_entry


class SetterValidationTest(unittest.TestCase):

    def test_priority_setter_exception(self):
        todo_entry = TodoEntry('x (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c')
        with self.assertRaises(ValueError) as cm:
            todo_entry.priority = 'AA'
        with self.assertRaises(TypeError) as cm:
            todo_entry.priority = 5
        with self.assertRaises(TypeError) as cm:
            todo_entry.priority = TodoEntry('')

    def test_completed_date_setter_exception(self):
        todo_entry = TodoEntry('(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c')
        with self.assertRaises(ValueError) as cm:
            todo_entry.completed_date = '2017-01-01'
        self.assertEqual(cm.exception.args[0], "Please, complete todo entry first")
        todo_entry.completed = True
        with self.assertRaises(ValueError) as cm:
            todo_entry.completed_date = '2017-01-01'
        self.assertEqual(cm.exception.args[0], "Cannot set completed_date without created_date")
