import unittest

from src.unittest_demo import write_to_file


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.file = open("test_data/file.txt", "w")

    def tearDown(self):
        self.file.close()

    def test_file_is_not_closed(self):
        write_to_file(self.file, "Hello from unittest")
        self.assertFalse(self.file.closed)


if __name__ == '__main__':
    unittest.main()
