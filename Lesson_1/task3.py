firstnumber = int(input("write first number: "))
Secondnumber = int(input("write second number: "))
equation = input("what equation you want: ")
if equation == "+":
    result = (firstnumber + Secondnumber)
if equation == "-":
    result = (firstnumber - Secondnumber)
if equation == "*":
    result = (firstnumber * Secondnumber)
if equation == "/":
    result = (firstnumber / Secondnumber)
print(result)