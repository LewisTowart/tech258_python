import os

# Directory
directory = "test_dir"

# Parent directory
parent_directory = "C:/Users/lewis/Desktop/Sparta_Global/Tech_258/github/python_learning"

# Path
path = os.path.join(parent_directory, directory)

# Create Dir
os.mkdir(path)