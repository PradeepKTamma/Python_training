import sys

n = len(sys.argv)

print("Total arguments passed:", n)
print("\nName argument:", sys.argv[1])

Fname = sys.argv[1]
FF = Fname.split(".")

if FF[1] == 'yml':
    print("Done !")
else:
    print("Wrong file type")
    exit()