import os
import subprocess


PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
os.chdir(PATH)

cmdCommand = "autopep8 " + PATH + \
    " --recursive --in-place --pep8-passes 2000 --verbose"
print(PATH, cmdCommand)

process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print('Done!')
