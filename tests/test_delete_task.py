import unittest
from database import add_task, delete_task, show_tasks

class TestDeleteTask(unittest.TestCase):
    def test_delete_task(self):
        add_task("Task to delete")
        tasks = show_tasks()
        task_id = tasks[-1][0]
        delete_task(task_id)
        tasks = show_tasks()
        self.assertFalse(any(task[0] == task_id for task in tasks))

if __name__ == "__main__":
    unittest.main()