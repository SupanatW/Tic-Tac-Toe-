
from socket import * 
from threading import Thread
import os,sys

count = 0
SERV_PORT = 50000

def handle_client(s):
  global count, place,turn
  place = []
  count = 0
  turn = 0
  lists = []
  while True:
    txtin = s.recv(1024) # recv input 2
    txtin_decode = txtin.decode('utf-8')
    print ('Client> %s' %(txtin).decode('utf-8'))
    print(place)
    # print("buff")
    mark = s.recv(1024)
    mark_decode = mark.decode('utf-8')
    # print(mark_decode)
    if turn % 2 == 0 and mark_decode == 'O':
      if txtin_decode in place:   #if ช่องซ้ำ
        s.send("Please choose other space".encode('utf-8'))
      else:
        if txtin == b'quit':
          print('Client disconnected ...')
          break
        else:
          place.append(txtin.decode('utf-8'))
          lists.append(txtin.decode('utf-8'))
          # print('Form O')
          # print(lists)
          if len(lists) >= 3 :
            checkWin(lists,mark_decode)
          txtout = txtin.upper()    
          s.send(txtout)
          # print(count)
          count += 1
          turn += 1
    elif turn % 2 == 1 and mark_decode == 'X':
      if txtin_decode in place:   #if ช่องซ้ำ
        s.send("Please choose other space".encode('utf-8'))
      else:
        if txtin == b'quit':
          print('Client disconnected ...')
          break
        else:
          place.append(txtin.decode('utf-8'))
          lists.append(txtin.decode('utf-8'))
          # print('Form X')
          # print(lists)
          if len(lists) >= 3 :
            checkWin(lists,mark_decode)
          txtout = txtin.upper()    
          s.send(txtout)
          print(count)
          count += 1
          turn += 1
    else:
      s.send("This is not your turn".encode('utf-8'))
  s.close()
  return

def checkWin(listed,marked):
  win_list = [['0','1','2'],['3','4','5'],['6','7','8'],['0','3','6'],['1','4','7'],['2','5','8'],['0','4','8'],['2','4','6']]
  for tup in win_list:
    x,y,z = tup
    if x in listed:
      if y in listed:
        if z in listed:
          print(marked + 'Win')
      # print("No")
  return False

def main():
  comein = 0
  addr = ('127.0.0.1', SERV_PORT)
  s = socket(AF_INET, SOCK_STREAM)
  s.bind(addr)
  s.listen(5)
  print ('TCP threaded server started ...')


  while True:
    sckt, addr = s.accept()
    ip, port = str(addr[0]), str(addr[1]) 
    print ('New client connected from ..' + ip + ':' + port)
    if comein == 0:
      sckt.send("O".encode('utf-8')) #send mark 1
      comein = 1
    elif comein == 1:
      sckt.send("X".encode('utf-8'))#send mark1 
      comein = 2
    else:
      sckt.send("You are spectator".encode('utf-8'))#send mark 1
  
    try:
      Thread(target=handle_client, args=(sckt,)).start()
    except:
      print("Cannot start thread..")
      import traceback
      trackback.print_exc()

  s.close()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print ('Interrupted ..')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
