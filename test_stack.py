import unittest
from stack import Stack
from stack import Element


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_stack_push_pop(self):

        n = 50
        self.assertTrue(self.stack.is_empty())
        for i in range(n):
            self.stack.push(i)
            self.assertEqual(self.stack.top(), i)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), n)
        for i in range(n-1, -1, -1):
            k = self.stack.pop()
            self.assertEqual(k, i)
        self.assertEqual(self.stack.size(), 0)
        for i in range(0, -4, -1):
            k = self.stack.pop()
            self.assertEqual(k, None)
        self.assertEqual(self.stack.size(), 0)

    def test_stack_clear(self):

        n = 50
        for i in range(n):
            self.stack.push(i)
        self.assertFalse(self.stack.is_empty())
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())

    def test_stack_empty(self):
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.top(), None)
        self.assertEqual(self.stack.size(), 0)

if __name__ == '__main__':
    unittest.main()
