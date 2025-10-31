import subprocess
import sys

Message = "Update files."

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

print ("git commit -m " + Message )
subprocess.run(["git", "commit", "-m", Message])

print ("git push")
subprocess.run(["git", "push"])

