import os
import sys
import subprocess

file_dir = os.path.dirname( os.path.realpath(__file__) )
lib_path = os.path.join(file_dir, "lib", "python")

print("Demo.py", os.environ.get("LD_LIBRARY_PATH", "No Path"))

sys.path.insert(0, lib_path)

import ogdf

if __name__ == "__main__":

    try:
        ogdf.system("ls -al")
    except Exception as e:
        print(e)

    print("YAY!!!")
