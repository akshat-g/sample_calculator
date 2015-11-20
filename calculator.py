from Tkinter import *

class Calculator():

	def __init__(self,master):

		self.current = ''

		frame = Frame(master)
		frame.pack()

		self.number = StringVar()
		self.entry = Entry(frame, textvariable=self.number, bd=10, font=20, insertwidth=2)
		self.entry.pack(side=TOP, fill=X)

		frame1 = Frame(master)
		frame1.pack(side=TOP)

		button1_name = '1'
		button2_name = '2'
		button3_name = '3'
		button4_name = '4'
		button5_name = '5'
		button6_name = '6'
		button7_name = '7'
		button8_name = '8'
		button9_name = '9'
		button0_name = '0'
		buttonplus_name = '+'
		buttonsubstract_name = '-'
		buttondivide_name = '/'
		buttonmultiply_name = '*'
		buttonequal_name = '='
		buttonclear_name = 'C'

		self.button1 = Button(frame1, text=button1_name, bg='black', fg='white', bd=5, command=lambda num=button1_name:self.insert(num))
		self.button1.pack(side=LEFT)
		self.button2 = Button(frame1, text=button2_name, bg='black', fg='white', bd=5, command=lambda num=button2_name:self.insert(num))
		self.button2.pack(side=LEFT)
		self.button3 = Button(frame1, text=button3_name, bg='black', fg='white', bd=5, command=lambda num=button3_name:self.insert(num))
		self.button3.pack(side=LEFT)
		self.button4 = Button(frame1, text=button4_name, bg='black', fg='white', bd=5, command=lambda num=button4_name:self.insert(num))
		self.button4.pack(side=LEFT)

		frame2 = Frame(master)
		frame2.pack(side=TOP)

		self.button5 = Button(frame2, text=button5_name, bg='black', fg='white', bd=5, command=lambda num=button5_name:self.insert(num))
		self.button5.pack(side=LEFT)
		self.button6 = Button(frame2, text=button6_name, bg='black', fg='white', bd=5, command=lambda num=button6_name:self.insert(num))
		self.button6.pack(side=LEFT)
		self.button7 = Button(frame2, text=button7_name, bg='black', fg='white', bd=5, command=lambda num=button7_name:self.insert(num))
		self.button7.pack(side=LEFT)
		self.button8 = Button(frame2, text=button8_name, bg='black', fg='white', bd=5, command=lambda num=button8_name:self.insert(num))
		self.button8.pack(side=LEFT)

		frame3 = Frame(master)
		frame3.pack(side=TOP)

		self.button9 = Button(frame3, text=button9_name, bg='black', fg='white', bd=5, command=lambda num=button9_name:self.insert(num))
		self.button9.pack(side=LEFT)
		self.button0 = Button(frame3, text=button0_name, bg='black', fg='white', bd=5, command=lambda num=button0_name:self.insert(num))
		self.button0.pack(side=LEFT)
		self.buttonplus = Button(frame3, text=buttonplus_name, bg='black', fg='white', bd=5, command=lambda op=buttonplus_name:self.insert(op))
		self.buttonplus.pack(side=LEFT)
		self.buttonsubstract = Button(frame3, text=buttonsubstract_name, bg='black', fg='white', bd=5, command=lambda op=buttonsubstract_name:self.insert(op))
		self.buttonsubstract.pack(side=LEFT)

		frame4 = Frame(master)
		frame4.pack(side=TOP)

		self.buttondivide = Button(frame4, text=buttondivide_name, bg='black', fg='white', bd=5, command=lambda op=buttondivide_name:self.insert(op))
		self.buttondivide.pack(side=LEFT)
		self.buttonmultiply = Button(frame4, text=buttonmultiply_name, bg='black', fg='white', bd=5, command=lambda op=buttonmultiply_name:self.insert(op))
		self.buttonmultiply.pack(side=LEFT)
		self.buttonequal = Button(frame4, text=buttonequal_name, bg='black', fg='white', bd=5, command=lambda op=buttonequal_name:self.operate(op))
		self.buttonequal.pack(side=LEFT)
		self.buttonclear = Button(frame4, text=buttonclear_name, bg='black', fg='white', bd=5, command=self.clear)
		self.buttonclear.pack(side=LEFT)


	def clear(self):
		self.entry.delete(0,END)

	def insert(self, number):
		self.entry.insert(END, number)

	def operate(self, op):
			
		if self.entry.get() != '':
			ans = eval(self.entry.get())
			self.entry.delete(0,END)
			self.entry.insert(0,ans)



root = Tk()
root.title('Calculator')
c = Calculator(root)

root.mainloop()