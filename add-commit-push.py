import subprocess
import sys

Message = "Update files."
# Check if the user has a parameter of m for message
if len(sys.argv) > 1 and sys.argv[1] == "-m":
    if len(sys.argv) > 2:
        Message = sys.argv[2]
    else:
        print("Error: No commit message provided after -m")
        sys.exit(1)

print ("Starting add-commit-push")
print ("git status")
subprocess.run(["git", "status"])

# Ask the user if they want to continue
confirm = input("Do you want to continue? (y/n): ")

if confirm.lower() == "y":
    print("Continuing with add commit push")
else:
    print("Exiting...")
    sys.exit()


print ("git add -A")
subprocess.run(["git", "add", "-A"])

print ("git commit -m \"" + Message +"\"")
subprocess.run(["git", "commit", "-m", Message])

print ("git push")
subprocess.run(["git", "push"])
