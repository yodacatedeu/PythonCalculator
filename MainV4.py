import math  # for extra math functions
from tkinter import *  # for the GUI objects
import unicodedata # for pi

# creating the basic window
window = Tk()
window.geometry("312x485")  # size of the window width:- 312, height:- 485
window.resizable(0, 0)  # prevents window resizing
window.title("Scientific Calculator") # Window's title


# ################### Calculator's functions ########################

# 'btn_click' function continuously updates the input field whenever a number or operator is pressed
def btn_click(item):
    global expression  # expression that is evaluated
    global expressionDisplay  # expression that is displayed

    if str(item) == "sin(" or str(item) == "cos(" or str(item) == "tan(":  # check for the special case of special functions
        expressionDisplay = expressionDisplay + str(item)  # update display expression
        expression = expression + "math." + str(item)  # add a call to the "math" library since that is where these special functions come from
    elif str(item) == "asin(" or str(item) == "acos(" or str(item) == "atan(": # check for the special case of special inverse functions
        expressionDisplay = expressionDisplay + str(item)  # update display expression
        expression = expression + "math." + str(item)  # add a call to the "math" library since that is where these special functions come from
    elif str(item) == "e^(":
        expressionDisplay = expressionDisplay + str(item)  # update display expression
        expression = expression + "math." + "exp("
    elif str(item) == "ln(":
        expressionDisplay = expressionDisplay + str(item)  # update display expression
        expression = expression + "math." + "log("
    elif str(item) == unicodedata.lookup("GREEK SMALL LETTER PI"):
        expressionDisplay = expressionDisplay + str(item)  # update display expression
        expression = expression + "math.pi"
    elif str(item) == "sqrt(":
        expressionDisplay = expressionDisplay + str(item)  # update display expression
        expression = expression + "math." + "sqrt("
    else:  # else update both expressions normally
        expression = expression + str(item)
        expressionDisplay = expressionDisplay + str(item)

    input_text.set(expressionDisplay)  # set the display text on the screen to expressionDisplay


# 'btn_clear' function clears the screen
def btn_clear():
    global expression
    global expressionDisplay

    # Clear all expressions and the screen itself
    expression = ""

    expressionDisplay = ""

    input_text.set("")


# 'btn_equal' calculates the inputted expression
def btn_equal():
    global expression
    global expressionDisplay

    try:
        result = str(eval(expression))  # 'eval' built in function evaluates the string expression directly
    except Exception:  # Catch errors in input and simply display "ERROR".
        input_text.set("ERROR")
    else:
        input_text.set(result)
    finally:  # Clear the expression since it has now been evaluated
        expression = ""
        expressionDisplay = ""


# ############################## main ###################################

expression = ""  # The expression to be evaluated
expressionDisplay = ""  # The expression that is displayed

# 'StringVar()' is used to get the instance of input field (The display text on the screen will be a string)

input_text = StringVar()

# creating a frame for the input field (The frame containing the screen)

input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="green", highlightcolor="green",
                    highlightthickness=1)               # colors can be specified as words or hex rgb values

input_frame.pack(side=TOP)  # packing input frame to  the top to fill entire available width

# creating the input field inside the input_frame (The screen itself)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="black", fg="yellow", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)  # place input field at gird(0,0): table-like format

input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the HEIGHT of input field

# creating another 'Frame' for all the buttons below the 'input_frame'

btns_frame = Frame(window, width=312, height=272.5, bg="black")

btns_frame.pack()  # fills entire frame, should be right below the screen

# first row: "clear" and "divide"

clear = Button(btns_frame, font=('arial', 9, 'bold'), text="CLEAR", fg="black", width=32, height=3, bd=0, bg="#716ca3", cursor="hand2",
               command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# second row: numbers 7-9 and "multiply"

seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#68747a", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#68747a", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#68747a", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row: numbers 4-6 and "minus"

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#68747a", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#68747a", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#68747a", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row: numbers 1-3 and "plus"

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#68747a", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#68747a", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#68747a", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fifth row: number 0, "point" and "square root"

zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#68747a", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

sqrt = Button(btns_frame, text="√", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
               command=lambda: btn_click("sqrt(")).grid(row=4, column=3, padx=1, pady=1)

# 6th row parentheses and log functions
openParenth = Button(btns_frame, text="(", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
                     command=lambda: btn_click("(")).grid(row=5, column=0, padx=1, pady=1)

closeParenth = Button(btns_frame, text=")", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
                      command=lambda: btn_click(")")).grid(row=5, column=1, padx=1, pady=1)

e = Button(btns_frame, text="e^", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
             command=lambda: btn_click("e^(")).grid(row=5, column=2, padx=1, pady=1)
ln = Button(btns_frame, text="ln", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
             command=lambda: btn_click("ln(")).grid(row=5, column=3, padx=1, pady=1)

# 7th row trig functions and pi
sin = Button(btns_frame, text="sin", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
             command=lambda: btn_click("sin(")).grid(row=6, column=0, padx=1, pady=1)
cos = Button(btns_frame, text="cos", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
             command=lambda: btn_click("cos(")).grid(row=6, column=1, padx=1, pady=1)
tan = Button(btns_frame, text="tan", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
             command=lambda: btn_click("tan(")).grid(row=6, column=2, padx=1, pady=1)
pi = Button(btns_frame, text=unicodedata.lookup("GREEK SMALL LETTER PI"), fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
             command=lambda: btn_click(unicodedata.lookup("GREEK SMALL LETTER PI"))).grid(row=6, column=3, padx=1, pady=1)

# 8th row arc trig functions and "equal"
asin = Button(btns_frame, text="arcsin", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
             command=lambda: btn_click("asin(")).grid(row=7, column=0, padx=1, pady=1)
acos = Button(btns_frame, text="arccos", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
             command=lambda: btn_click("acos(")).grid(row=7, column=1, padx=1, pady=1)
atan = Button(btns_frame, text="arctan", fg="black", width=10, height=3, bd=0, bg="#50768a", cursor="hand2",
             command=lambda: btn_click("atan(")).grid(row=7, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#854a4e", cursor="hand2",
                command=lambda: btn_equal()).grid(row=7, column=3, padx=1, pady=1)


window.mainloop()  # Keep displaying window until it is manually closed.

