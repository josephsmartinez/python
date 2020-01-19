import os
import time

class Helper:
  def __init__(self, path):
    self.path = path

  def get_path(self):
    base_path = os.getcwd()
    return os.path.join(base_path, self.path)

class Worker:

  def __init__(self):
    self.helper = Helper('db')

  def print_path(self):
    path = self.helper.get_path()
    time.sleep(1)
    print('Working on {}'.format(path))
    return path
