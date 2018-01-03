import unittest

import pytest
from todotxt import TodoEntry

from .test_data import MERGE_TEST_TUPLE


@pytest.mark.parametrize("initial_entry_text, additional_entry_text, required_result", MERGE_TEST_TUPLE)
def test_merge_logic(initial_entry_text, additional_entry_text, required_result):
    initial_entry = TodoEntry(initial_entry_text)
    additional_entry = TodoEntry(additional_entry_text)
    initial_entry.merge(additional_entry)
    assert str(initial_entry) == required_result
