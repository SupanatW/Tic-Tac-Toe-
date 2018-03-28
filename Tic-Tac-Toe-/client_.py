from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)
mark = s.recv(2048) # recv mark 1
print(mark.decode('utf-8'))
username = input('Enter your name: ')
while True:
    print ('%s> ' %(username), end='') 
    sys.stdout.flush()
    txtout = sys.stdin.readline().strip()
    s.send(txtout.encode('utf-8')) #send input 2
    # print("eiei")
    s.send(mark) # send mark 3
    if txtout == 'quit':
      break
    modifiedMsg = s.recv(2048)
    print (modifiedMsg.decode('utf-8'))

s.close()
