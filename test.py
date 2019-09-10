import subprocess
import os
import msvcrt as m
import shlex

dir = os.path.dirname(os.path.realpath(__file__))

def wait():
    m.getch()

def run_command(command, curr_dir):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, cwd=curr_dir, shell=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.decode('utf-8').strip()
    rc = process.poll()
    return rc

print("=================FRONTEND=================")
print("Please make sure the Tomcat7 server and MySQL database are running")
print("Press any key to run frontend tests")
wait()

run_command("yarn test", dir + os.sep + "frontend" + os.sep)

print("=================BACKEND=================")
print("Please make sure the Tomcat7 server and MySQL database are running")
print("Press any key to run backend tests")
wait()

run_command("mvn test", dir + os.sep + "backend" + os.sep)
