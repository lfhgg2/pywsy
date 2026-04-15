# test_app.py
import unittest
from app import add

class TestAddFunction(unittest.TestCase):
    # 测试正常加法
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    # 测试负数相加
    def test_add_negative(self):
        self.assertEqual(add(-1, 1), 0)
    # 测试加0
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
