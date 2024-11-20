import unittest
from database import add_task, complete_task, show_tasks

class TestCompleteTask(unittest.TestCase):
    def test_complete_task(self):
        add_task("Task to complete")
        tasks = show_tasks()
        task_id = tasks[-1][0]
        complete_task(task_id)
        tasks = show_tasks()
        self.assertTrue(any(task[0] == task_id and task[2] for task in tasks))

if __name__ == "__main__":
    unittest.main()
