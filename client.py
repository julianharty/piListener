import subprocess
print(len(subprocess.check_output(['last','reboot']).split(b'\n')) -3) #Gets number of boots
