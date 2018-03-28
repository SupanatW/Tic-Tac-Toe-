from tkinter import *
from tkinter import messagebox
import sys
from tkinter.ttk import Entry, Button

global turn
class Tile(Label):
	def __init__(self,parent,checkWin):
		Label.__init__(self,parent,font=('',50),width=2,justify='center', relief='raised',bg='white')
		self.checkWin = checkWin
		self.bind('<Button-1>',self.markX)
		self.bind('<Button-2>',self.markO)
		self.marked = ''


	def markX(self,event):
		if not self.marked:
			self.config(text = 'X')
			self.marked = 'X'
			self.checkWin()

	def markO(self,event):
		if not self.marked:
			self.config(text = 'O')
			self.marked = 'O'
			self.checkWin()

class Main():
	def __init__(self,parent):
		self.parent = parent

		self.player1 = StringVar()
		self.player2 = StringVar()
		self.winner = StringVar()

		self.createWidgets()

	def createWidgets(self):
		self.mainFrame = Frame(self.parent)
		Label(self.mainFrame,text = 'Tic Tac Toe').pack()
		frame1 = Frame(self.mainFrame)
		Label(frame1,text='Player1(X,button-1)').grid()
		Entry(frame1,textvariable = self.player1).grid(row = 0, column = 1,padx = 5,pady = 5)
		Label(frame1,text='Player2(O,button-2)').grid()
		Entry(frame1,textvariable = self.player2).grid(row = 1, column = 1,padx = 5,pady = 5)
		frame1.pack()
		start_button = Button(self.mainFrame,text = 'Start',command = self.start).pack()
		exit_button = Button(self.mainFrame,text = 'Exit', command = self.exit).pack()
		self.mainFrame.pack(padx=10,pady=10)
		self.gameFrame = Frame(self.parent)
		self.winFrame = Frame(self.parent)
		Label(self.winFrame,textvariable = self.winner , font=('',50)).pack()
		Button(self.winFrame,text = 'Play Again', command = self.start).pack()
		Button(self.winFrame,text = 'Exit', command = self.exit).pack()

	def start(self):
		player1 = self.player1.get()
		player2 = self.player2.get()
		self.tiles = []
		self.winFrame.pack_forget()

		if player1 and player2 and player1 != player2:
			self.mainFrame.forget()
			for i in range(3):
				for j in range(3):
					tile = Tile(self.gameFrame,self.checkWin)
					tile.grid(row=i,column=j)
					self.tiles.append(tile)
			
	
		# Button(self.gameFrame,text = 'Start Again',command = self.start).pack()
		# Button(self.gameFrame,text = 'Exit', command = self.exit).pack()
		self.gameFrame.pack()	
		

	def checkWin(self):
		global draw
		print(draw)
		for x,y,z in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
			if self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'X':
				messagebox.showinfo(title="Result", message="Player1 Win!!")
				self.showWin(self.player1.get())
				#Button(text = 'Start Again',command = self.start).pack()
			if self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'O':
				messagebox.showinfo(title="Result", message="Player2 Win!!")
				self.showWin(self.player2.get())
				#Button(text = 'Start Again',command = self.start).pack()
			if draw == 8:
				messagebox.showinfo(title="Result", message="Game Draw!!")
				self.showDraw()
				draw = draw + 1
		draw = draw + 1

	def showWin(self,player):
		global draw
		draw = -1
		self.gameFrame.pack_forget()
		self.winFrame.pack(pady = 10,padx=10)
		self.winner.set(player + ' Win!!!!' )

	def showDraw(self):
		global draw
		draw = -1
		self.gameFrame.pack_forget()
		self.winFrame.pack(pady = 10,padx=10)
		self.winner.set('Game Draw!!!!' )


	def exit(self):
		sys.exit()


if __name__ == '__main__':
	global draw
	draw = 0
	root = Tk()
	root.geometry("550x550")
	Main(root)
	root.mainloop()