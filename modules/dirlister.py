import os

def run(**args):
    print "[*] In dirlister module."
    folders = os.listdir(".")
    return str(folders)