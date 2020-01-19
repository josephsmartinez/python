from unittest import TestCase, mock
from os_path import Helper, Worker


class TestWorkerModule(TestCase):

  def test_patching_class(self):
    with mock.patch('os_path.Helper') as MockHelper:
      MockHelper.return_value.get_path.return_value = 'testing'
      worker = Worker()
      MockHelper.assert_called_once_with('db')
      self.assertEqual(worker.print_path(), 'testing')