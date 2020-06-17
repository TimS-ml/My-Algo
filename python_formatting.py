import os
import subprocess


PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
os.chdir(PATH)

cmd = [r"autopep8", PATH, "--recursive", "--in-place",
       "--pep8-passes", "2000", "--verbose"]
print(cmd)

process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
output, error = process.communicate()

print('Done!')
