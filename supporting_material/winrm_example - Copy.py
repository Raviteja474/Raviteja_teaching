import winrm

# here 2019B is machine name and auth is authentication in that we will give username and password

session = winrm.Session("2019B", auth=("ansible", "start!12345"))

output = session.run_cmd("powershell", ["-c", "(get-eventlog -logname Application -newest 10).Message"])

print(f"The status of the output is : {output.status_code}")

print("#" * 50)

print(output.std_out.decode().split("\r\n"))

print("#" * 50)
