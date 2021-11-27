import subprocess

# SUMANTH
PRESENT_DIRECTORY = r'cd C:\Users\ravit\Desktop\Teaching\Raviteja_teaching'
ADD_COMAND = r'git add .'
STAUTS_CMD = r'git status'
COMMIT_COMAND = r'git commit -m "Nov_27"'
PUSH_COMMAND = r'git push origin main'

print("Entering required directory.")
output = subprocess.run(PRESENT_DIRECTORY, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)

print("status files to git.")
output = subprocess.run(STAUTS_CMD, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)

print("Adding files to git.")
output = subprocess.run(ADD_COMAND, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)

print("committing files to git.")
output = subprocess.run(COMMIT_COMAND, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)

print("pushing files to git.")
output = subprocess.run(PUSH_COMMAND, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)




