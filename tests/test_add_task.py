import unittest
from database import add_task, show_tasks

class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        add_task("Test task")
        tasks = show_tasks()
        self.assertTrue(any(task[1] == "Test task" for task in tasks))

if __name__ == "__main__":
    unittest.main()