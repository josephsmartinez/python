import os


def list_files():
  path = '.'

  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
      for file in f:
          if '.txt' in file:
              files.append(os.path.join(r, file))

  for f in files:
      print(f)

def list_directories():
  path = '.'

  folders = []

  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
      for folder in d:
          folders.append(os.path.join(r, folder))

  for f in folders:
      print(f)

if __name__ == "__main__":
    list_directories()
    list_files()
    