import unittest

from Lab3.src.TaskList import TaskList

class TaskListTestCase(unittest.TestCase):
    def test_add_task_should_add_task_to_list(self):
        # given
        task_list = TaskList()

        # then
        task_list.add_task("Buy milk")

        # then
        self.assertEqual(task_list.tasks(), ["Buy milk"])


if __name__ == '__main__':
    unittest.main()