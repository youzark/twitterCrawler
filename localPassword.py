import os
def getUserName():
    with open(os.path.expanduser("~/.local/passwd/userName"),"r") as f:
        userName = f.read().strip()
        return userName

def getPasswd():
    with open(os.path.expanduser("~/.local/passwd/password"),"r") as f:
        password = f.read().strip()
        return password
