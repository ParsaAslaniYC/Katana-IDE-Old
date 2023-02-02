import subprocess

filepath='install.bat'
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

stdout, stderr = p.communicate()
print(p.returncode) # is 0 if success