import os
import sys
import subprocess

file_dir = os.path.dirname( os.path.realpath(__file__) )
lib_path = os.path.join(file_dir, "lib", "python")

if __name__ == "__main__":


    #cmd = "LD_LIBRARY_PATH={} python demo.py".format(lib_path)

    cmd = "python demo.py".format(lib_path)

    sub_env = os.environ.copy()

    yenv = os.environ.get("LD_LIBRARY_PATH","")

    if not lib_path in yenv:

        print("importing.. . .. ")
        sub_env["LD_LIBRARY_PATH"] = lib_path + os.pathsep + os.environ.get("LD_LIBRARY_PATH", "")

    proc = subprocess.Popen(cmd, shell=True, env=sub_env)


    try:
        print(cmd)
        proc.wait()

    except Exception as exc:
        print('Failed re-exec:', exc)
        sys.exit(1)
    else:
        print("DONE")

