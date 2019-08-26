import sys, os

if len(sys.argv) == 1:
    raise TypeError("must at least one argument that is git commit message!")
os.system("git add -f *")
os.system("git commit -am '" + sys.argv[1] + "'")
os.system("git push")
