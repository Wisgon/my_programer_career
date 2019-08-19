import sys, os

print(sys.argv[1])
os.system("git add *")
os.system("git commit -m '" + sys.argv[1] + "'")
os.system("git push")
