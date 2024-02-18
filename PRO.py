import os, sys
os.system("git pull")
try:
    __import__("one_enc").menu()
except Exception as e:
    exit(str(e))
