import unittest
from database import add_task, show_tasks

class TestShowTasks(unittest.TestCase):
    def test_show_tasks(self):
        add_task("Task to show")
        tasks = show_tasks()
        self.assertGreater(len(tasks), 0)

if __name__ == "__main__":
    unittest.main()
