import unittest

from todotxt import TodoEntry


class EntryModifyTest(unittest.TestCase):

    def test_add_project(self):
        todotxt_text = '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        todo_entry.add_project('T3')
        self.assertEqual(todo_entry.completed, False)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2', 'T3'})
        self.assertEqual(todo_entry.contexts, {'Cute', })
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, None)
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))
        self.assertEqual(
            str(todo_entry),
            '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c +T3'
        )

    def test_remove_project(self):
        todotxt_text = '(A) Make @Cute +T1 +T2 +T3 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        todo_entry.remove_project('T3')
        self.assertEqual(todo_entry.completed, False)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute', })
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, None)
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))
        self.assertEqual(
            str(todo_entry),
            '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        )

    def test_add_contexts(self):
        todotxt_text = '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        todo_entry.add_context('T3')
        self.assertEqual(todo_entry.completed, False)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute', 'T3'})
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, None)
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))
        self.assertEqual(
            str(todo_entry),
            '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c @T3'
        )

    def test_remove_contexts(self):
        todotxt_text = '(A) Make @Cute @Very +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        todo_entry.remove_context('Very')
        self.assertEqual(todo_entry.completed, False)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute'})
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, None)
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))
        self.assertEqual(
            str(todo_entry),
            '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        )

    def test_add_tag(self):
        todotxt_text = '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        todo_entry.add_tag('c5', 'c6')
        self.assertEqual(todo_entry.completed, False)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute'})
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, None)
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4', c5='c6'))
        self.assertEqual(
            str(todo_entry),
            '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c c5:c6'
        )

    def test_add_tag(self):
        todotxt_text = '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        todo_entry.remove_tag('c3', 'c4')
        self.assertEqual(todo_entry.completed, False)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute'})
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, None)
        self.assertEqual(todo_entry.tags, dict(c1='c2'))
        self.assertEqual(
            str(todo_entry),
            '(A) Make @Cute +T1 +T2 c1:c2 with c-c-c-c-c'
        )
