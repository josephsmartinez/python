import os

def path_listing():
  path = '/Users/josephmartinez/Downloads/'
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
    for file in f:
      print(file)
      # if '.txt' in file:
      #   files.append(os.path.join(r, file))
  for file in files:
    print(f)

def read():
  f = open("test1.txt", "r")
  print(f.read())
  f.close

if __name__ == "__main__":
    #read()
    path_listing()

