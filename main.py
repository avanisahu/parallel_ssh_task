import os
import threading
import time

user = "avani"
command = "C:/Python313/python.exe C:/parallel_ssh_task_avani/process_file.py C:/parallel_ssh_task_avani/input.txt"

with open("ips.txt") as f:
    servers = [ip.strip() for ip in f if ip.strip()]

def run(ip):
    print("running_on", ip)
    os.system(f'ssh {user}@{ip} "{command}"')

threads =[]
start = time.time()

for ip in servers:
    t = threading.Thread(target=run, args=(ip,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print("time_taken for 3 servers parallely:", end - start)
print("task_completed")


# now we are done with paralle ,now sequential one by one run for comparison
start = time.time()
for ip in servers:
    run(ip)
end = time.time()

print("time_taken for 3 servers one after one:", end - start)
print("task_completed")
