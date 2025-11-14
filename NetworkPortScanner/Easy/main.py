import socket

target = input("Enter IP or Domain : \n")
start_port = int(input("Enter starting port :\n"))
end_port = int(input("Enter end port :\n"))

try :
    ip = socket.gethostbyname(target)

except :
    print("Could not resolve host name")


print(f"Scannin target [{target}] From {start_port} TO {end_port}")

for i in range(start_port,end_port+1):
    s = socket.socket()
    s.settimeout(0.5)

    result = s.connect_ex((ip,i))
    if result == 0:
        print(f"port : {i}")
    s.close()

print("Scan Completed")