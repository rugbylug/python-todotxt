import unittest

from todotxt import TodoEntry


class EntryModifyTest(unittest.TestCase):

    def test_equality(self):
        entry1 = TodoEntry('(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c')
        entry2 = TodoEntry('(B) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c')
        entry2.priority = 'A'
        self.assertEqual(entry1, entry2)

    def test_hash(self):
        todo_text = '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todo_text)
        self.assertEqual(hash(todo_text), hash(todo_entry))

    def test_repr(self):
        todo_text = '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todo_text)
        self.assertEqual(repr(todo_entry), todo_text)

    def test_str(self):
        todo_text = '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todo_text)
        self.assertEqual(str(todo_entry), todo_text)
