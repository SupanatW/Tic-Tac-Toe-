from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000
addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)
checkin = s.recv(2048) #recv o,x
turn = '0'
print(checkin)

while True:

    sys.stdout.flush()

    if checkin == b'You are O' :
        sys.stdout.flush()
        print("Input : ")
        txtout = sys.stdin.readline().strip()
        if turn == '0':
            s.send(txtout.encode('utf-8')) # send input
            turn = '1'
            s.send(turn.encode('utf-8')) # send turn
            print("Sent from O")
        else :
            print("Not your turn O!!!")

    else :
        sys.stdout.flush()
        print("Input : ")
        txtout = sys.stdin.readline().strip()
        if turn == '1':
            s.send(txtout.encode('utf-8'))
            turn = '0'
            s.send(turn.encode('utf-8'))
            print("Sent from X ")
            
        else:
            print("Not your turn X!!!")
    turn_encode = s.recv(2048)
    turn = turn_encode.decode('utf-8')
    print('turn = ' + turn)

s.close()
