from tkinter import *


root = Tk()
root.geometry("208x300")
root.resizable(False, False)

class aplication:
    def __init__(self):
        self.create_buttons()
        self.a = ""
        self.num1 = 0
        self.num2 = 0
        self.operation = ""
        self.total = 0

    def create_buttons(self):
        self.zero_button = Button(root, text="0", height=2, width=6)
        self.zero_button.grid(column=0, row=6, columnspan=2, sticky="we")
        self.zero_button["command"] = self.add_0_to_str

        self.dot_button = Button(root, text=".", height=2, width=6)
        self.dot_button.grid(column=2, row=6)
        self.dot_button["command"] = self.add_dot_to_str

        self.equal_button = Button(root, text="=", height=2, width=6)
        self.equal_button.grid(column=3, row=6)
        self.equal_button["command"] = self.equal

        self.one_button = Button(root, text="1", height=2, width=6)
        self.one_button.grid(row=5, column=0)
        self.one_button["command"] = self.add_1_to_str

        self.two_button = Button(root, text="2", height=2, width=6)
        self.two_button.grid(row=5,column=1)
        self.two_button["command"] = self.add_2_to_str

        self.three_button = Button(root, text="3", height=2, width=6)
        self.three_button.grid(row=5, column=2)
        self.three_button["command"] = self.add_3_to_str

        self.plus_button = Button(root, text="+", height=2,width=6)
        self.plus_button.grid(row=5, column=3)
        self.plus_button["command"] = self.plus

        self.four_button = Button(root, text="4", height=2, width=6)
        self.four_button.grid(row=4, column=0)
        self.four_button["command"] = self.add_4_to_str

        self.five_button = Button(root, text="5", height=2, width=6)
        self.five_button.grid(row=4, column=1)
        self.five_button["command"] = self.add_5_to_str

        self.six_button = Button(root, text="6", height=2, width=6)
        self.six_button.grid(row=4, column=2)
        self.six_button["command"] = self.add_6_to_str

        self.minus_button = Button(root, text="-", height=2, width=6)
        self.minus_button.grid(row=4, column=3)

        self.seven_button = Button(root, text="7", height=2, width=6)
        self.seven_button.grid(row=3, column=0)
        self.seven_button["command"] = self.add_7_to_str

        self.eigth_button = Button(root, text="8", height=2, width=6)
        self.eigth_button.grid(row=3, column=1)
        self.eigth_button["command"] = self.add_8_to_str

        self.nine_button = Button(root, text="9", height=2, width=6)
        self.nine_button.grid(row=3, column=2)
        self.nine_button["command"] = self.add_9_to_str

        self.multiply_button = Button(root, text="*", height=2, width=6)
        self.multiply_button.grid(row=3, column=3)

        self.clear_button = Button(root, text="AC",height=2, width=6)
        self.clear_button.grid(column=0, row=2, columnspan=2, sticky="we")
        self.clear_button["command"] = self.clear_all

        self.negative_button = Button(root, text="-/+", height=2, width=6)
        self.negative_button.grid(column=2, row=2)


        self.divide_button = Button(root, text="/", height=2, width=6, bg="orange", fg="white")
        self.divide_button.grid(column=3, row=2)

    def add_1_to_str(self):
        self.a = self.a + "1"

    def add_2_to_str(self):
        self.a = self.a + "2"

    def add_3_to_str(self):
        self.a = self.a + "3"

    def add_4_to_str(self):
        self.a = self.a + "4"

    def add_5_to_str(self):
        self.a = self.a + "5"

    def add_6_to_str(self):
        self.a = self.a + "6"

    def add_7_to_str(self):
        self.a = self.a + "7"

    def add_8_to_str(self):
        self.a = self.a + "8"

    def add_9_to_str(self):
        self.a = self.a + "9"

    def add_0_to_str(self):
        self.a = self.a + "0"

    def add_dot_to_str(self):
        self.a = self.a + "."

    def clear_all(self):
        self.a = ""
        self.num1 = 0
        self.num2 = 0
        self.ope = ""

    def plus(self):
        self.operation = "+"
        self.a = int(self.a)
        self.num1 = self.a
        self.a = str(self.a)
        self.a = ""

    def equal(self):
        self.num2 = self.a
        self.num1 = int(self.num1)
        self.num2 = int(self.num2)
        if self.operation == "+":
            self.total = self.num1 + self.num2
        elif self.operation == "-":
            self.total = self.num1 - self.num2
        elif self.operation == "*":
            self.total = self.num1 * self.num2
        elif self.operation == "/":
            self.total = self.num1 / self.num2
        self.num1 = str(self.num1)
        self.num2 = str(self.num2)
        self.total = str(self.total)
        print(self.num1 + self.operation + self.num2 + '=' + self.total)


aplication()
root.mainloop()
