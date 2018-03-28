from socket import * 
import sys
import os

SERV_PORT = 50000
count = 0
turn = 0
addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
s.listen(1)
print ('TCP forked server started ...')
address = []
print(s)

while True:
  sckt, addr = s.accept()
  print(sckt)
  print(addr)
  #address.append(sckt)
  if count == 0:
    check = "You are O"
    sckt.send(check.encode('utf-8')) #send you are o
    count = 1
    #o_addr = sckt
  else:
    check = "You are X"
    sckt.send(check.encode('utf-8')) #send you are x
    count = 2
    x_addr = sckt
  print ('New client connected ..')
  print(count)
  if count == 2:
    print("in count")
    if os.fork() == 0: 
      print('1')
      txtin = sckt.recv(1024) #recv input
      print('2')
      while True:
        
        turn = sckt.recv(1024) #recv turn
        print('3')
        decode_turn = turn.decode('utf-8')
        decode_turn += 1
        print(decode_turn)
        sckt.send(decode_turn.encode('utf-8'))
        print ('Client> %s' %(txtin).decode('utf-8')) 
        if txtin == b'quit':
          print('Client disconnected ...')
          break
        else:
          txtout = txtin.upper()    
          sckt.send(txtout)
      sckt.close()
    else:
      sckt.close()
  
s.close()
