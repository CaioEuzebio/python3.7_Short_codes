""" This program check a list of IPs in to a single colum .txt file and return 2 files with valis and invalid IPs.
regarding invalids IPs with bytes that exceed 255 """

def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
        return True
filecheck = open("IPS.txt")
valid = open('Valids.txt', 'w')
invalid = open('Invalids.txt', 'w')
for line in filecheck.readlines():
    if ip_ok(line):
        valid.write(line)
    else:
        invalid.write(line)
filecheck.close()
valid.close()
invalid.close
