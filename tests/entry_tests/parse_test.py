import unittest

from todotxt import TodoEntry


class EntryParseTest(unittest.TestCase):

    def test_base_entry(self):
        todotxt_text = '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        self.assertEqual(todo_entry.completed, False)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute', })
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, None)
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))

    def test_with_date(self):
        todotxt_text = '(A) 2016-05-05 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        self.assertEqual(todo_entry.completed, False)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute', })
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, '2016-05-05')
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))

    def test_completed(self):
        todotxt_text = 'x (B) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        self.assertEqual(todo_entry.completed, True)
        self.assertEqual(todo_entry.priority, 'B')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute', })
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, None)
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))

    def test_strange_completed(self):
        todotxt_text = 'x(B) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        self.assertEqual(todo_entry.completed, False)
        self.assertEqual(todo_entry.priority, None)
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute', })
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, None)
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))

    def test_create_with_complete_date(self):
        todotxt_text = 'x (B) 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        self.assertEqual(todo_entry.completed, True)
        self.assertEqual(todo_entry.priority, 'B')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute', })
        self.assertEqual(todo_entry.completed_date, None)
        self.assertEqual(todo_entry.created_date, '2017-01-01')
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))

    def test_completed_with_date(self):
        todotxt_text = 'x (A) 2016-05-06 2016-05-05 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        self.assertEqual(todo_entry.completed, True)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute', })
        self.assertEqual(todo_entry.completed_date, '2016-05-06')
        self.assertEqual(todo_entry.created_date, '2016-05-05')
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))

    def test_completed_with_many_dates(self):
        todotxt_text = 'x (A) 2016-05-06 2016-05-05 2016-05-04 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c'
        todo_entry = TodoEntry(todotxt_text)
        self.assertEqual(todo_entry.completed, True)
        self.assertEqual(todo_entry.priority, 'A')
        self.assertEqual(todo_entry.projects, {'T1', 'T2'})
        self.assertEqual(todo_entry.contexts, {'Cute', })
        self.assertEqual(todo_entry.completed_date, '2016-05-06')
        self.assertEqual(todo_entry.created_date, '2016-05-05')
        self.assertEqual(todo_entry.tags, dict(c1='c2', c3='c4'))
