import os
import pickle

if not os.path.isdir("files"):
    os.mkdir("files")

os.chdir("files")
open("key.txt", "w")
with open("base.txt", "w") as file:
    pickle.dump([], file)
