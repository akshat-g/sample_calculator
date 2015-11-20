from Tkinter import *

class Calculator():

	def __init__(self,master):

		self.current = ''

		self.frame = Frame(master)
		self.frame.pack()

		self.number = StringVar()
		vcmd = (master.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

		self.entry = Entry(self.frame, textvariable=self.number, bd=10, font=20, insertwidth=2, validate='key', validatecommand=vcmd)
		self.entry.pack(side=TOP, fill=X)

		self.createWidgets(master)

		
	def createWidgets(self,master):

		self.frame1 = Frame(master)
		self.frame1.pack(side=TOP)

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

		self.button1 = Button(self.frame1, text=button1_name, bg='black', fg='white', bd=5, command=lambda num=button1_name:self.insert(num))
		self.button1.pack(side=LEFT)
		self.button2 = Button(self.frame1, text=button2_name, bg='black', fg='white', bd=5, command=lambda num=button2_name:self.insert(num))
		self.button2.pack(side=LEFT)
		self.button3 = Button(self.frame1, text=button3_name, bg='black', fg='white', bd=5, command=lambda num=button3_name:self.insert(num))
		self.button3.pack(side=LEFT)
		self.button4 = Button(self.frame1, text=button4_name, bg='black', fg='white', bd=5, command=lambda num=button4_name:self.insert(num))
		self.button4.pack(side=LEFT)

		self.frame2 = Frame(master)
		self.frame2.pack(side=TOP)

		self.button5 = Button(self.frame2, text=button5_name, bg='black', fg='white', bd=5, command=lambda num=button5_name:self.insert(num))
		self.button5.pack(side=LEFT)
		self.button6 = Button(self.frame2, text=button6_name, bg='black', fg='white', bd=5, command=lambda num=button6_name:self.insert(num))
		self.button6.pack(side=LEFT)
		self.button7 = Button(self.frame2, text=button7_name, bg='black', fg='white', bd=5, command=lambda num=button7_name:self.insert(num))
		self.button7.pack(side=LEFT)
		self.button8 = Button(self.frame2, text=button8_name, bg='black', fg='white', bd=5, command=lambda num=button8_name:self.insert(num))
		self.button8.pack(side=LEFT)

		self.frame3 = Frame(master)
		self.frame3.pack(side=TOP)

		self.button9 = Button(self.frame3, text=button9_name, bg='black', fg='white', bd=5, command=lambda num=button9_name:self.insert(num))
		self.button9.pack(side=LEFT)
		self.button0 = Button(self.frame3, text=button0_name, bg='black', fg='white', bd=5, command=lambda num=button0_name:self.insert(num))
		self.button0.pack(side=LEFT)
		self.buttonplus = Button(self.frame3, text=buttonplus_name, bg='black', fg='white', bd=5, command=lambda op=buttonplus_name:self.insert(op))
		self.buttonplus.pack(side=LEFT)
		self.buttonsubstract = Button(self.frame3, text=buttonsubstract_name, bg='black', fg='white', bd=5, command=lambda op=buttonsubstract_name:self.insert(op))
		self.buttonsubstract.pack(side=LEFT)

		self.frame4 = Frame(master)
		self.frame4.pack(side=TOP)

		self.buttondivide = Button(self.frame4, text=buttondivide_name, bg='black', fg='white', bd=5, command=lambda op=buttondivide_name:self.insert(op))
		self.buttondivide.pack(side=LEFT)
		self.buttonmultiply = Button(self.frame4, text=buttonmultiply_name, bg='black', fg='white', bd=5, command=lambda op=buttonmultiply_name:self.insert(op))
		self.buttonmultiply.pack(side=LEFT)
		self.buttonequal = Button(self.frame4, text=buttonequal_name, bg='black', fg='white', bd=5, command=lambda op=buttonequal_name:self.operate(op))
		self.buttonequal.pack(side=LEFT)
		self.buttonclear = Button(self.frame4, text=buttonclear_name, bg='black', fg='white', bd=5, command=self.clear)
		self.buttonclear.pack(side=LEFT)


	def clear(self):
		self.entry.delete(0,END)

	def insert(self, number):
		self.entry.insert(END, number)

	def operate(self, op):

		if self.entry.get() != '':
			try:
				ans = eval(self.entry.get())
				self.entry.delete(0,END)
				self.entry.insert(0,ans)
			except SyntaxError:
				pass


	def validate(self, action, index, value_if_allowed,
					prior_value, text, validation_type, trigger_type, widget_name):

		
		for ch in list(text):
			if ch not in '0123456789+-/*':
				return False
			else:
				return True


root = Tk()
root.title('Calculator')
c = Calculator(root)

root.mainloop()