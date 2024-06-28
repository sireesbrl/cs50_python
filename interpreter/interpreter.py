#simplified calculator in python

print("Types of operations allowed:\n",
      "Addition (+)\n",
      "Subtraction (-)\n",
      "Division (/)\n",
      "Multiplication (*)\n")

expression = input("Expression: ").strip().split()

x = float(expression[0])
y = expression[1]
z = float(expression[2])

match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "/":
        print(x/z)
    case "*":
        print(x*z)
    case _:
        print("syntax error!")

