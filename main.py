import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

run("git add .")
run('git commit -m "Update from Python script"')
run("git push origin master")

print("✅ Code pushed to GitHub successfully")
