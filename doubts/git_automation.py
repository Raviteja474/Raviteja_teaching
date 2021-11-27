import subprocess

PRESENT_DIRECTORY = r'cd C:\Users\ravit\Desktop\Teaching\Raviteja_teaching'
ADD_COMAND = r'git add .'
STAUTS_CMD = r'git status'
COMMIT_COMAND = r'git commit -m "Nov_27"'
PUSH_COMMAND = r'git push origin main'

output = subprocess.run(PRESENT_DIRECTORY, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)

output = subprocess.run(STAUTS_CMD, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)

output = subprocess.run(ADD_COMAND, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)

output = subprocess.run(COMMIT_COMAND, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)

output = subprocess.run(PUSH_COMMAND, stdout=subprocess.PIPE, encoding="utf-8", shell=True)
print(output.stdout, output.stderr)




