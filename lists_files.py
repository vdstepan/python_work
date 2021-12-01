import pathlib

example_dir = '.'
dir = pathlib.Path(example_dir)
files = [file.name for file in dir.iterdir() if file.is_file()]
subdirs = [file.name for file in dir.iterdir() if file.is_dir()]


print(subdirs)
print("--------------")
print(files)
