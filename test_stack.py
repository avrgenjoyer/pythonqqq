import unittest
from stack import Stack
from stack import Element


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_stack_1(self):

        self.assertTrue(self.stack.is_empty())
        for n in range(0, 50):
            self.stack.push(n)
            self.assertEqual(self.stack.top(), n)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), (n+1))
        for n in range(n, -1, -1):
            k = self.stack.pop()
            self.assertEqual(k, n)
        self.assertEqual(self.stack.size(), 0)
        for n in range(n, -4, -1):
            k = self.stack.pop()
            self.assertEqual(k, None)
        self.assertEqual(self.stack.size(), 0)

    def test_stack_2(self):
        for n in range(0, 50):
            self.stack.push(n)
        self.assertFalse(self.stack.is_empty())
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())

    def test_stack_3(self):
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.top(), None)
        self.assertEqual(self.stack.size(), 0)

if __name__ == '__main__':
    unittest.main()
