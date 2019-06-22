import glob

path = '.'

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    print(f)
