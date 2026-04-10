from pssh.clients import ParallelSSHClient

hosts = ['127.0.0.1', '127.0.0.1', '127.0.0.1']
cmd = 'C:/Python313/python.exe C:/parallel_ssh_task_avani/process_file.py C:/parallel_ssh_task_avani/input.txt'

client = ParallelSSHClient(hosts)
output = client.run_command(cmd)
client.join(output)

for host_out in output:
    for line in host_out.stdout:
        print(line)