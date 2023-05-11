#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# Prediction: terminal prints '5'


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# Prediction: terminal prints error because the var number_of_days_in_a_week_silicon_or_triangle_sides() is not defined


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# Prediction: terminal prints '5' becasue it is the first value returned in the loop


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# Prediction: terminal prints '5' because the return 5 statement comes before print(10) in the loop and once the condition is met, the program terminates


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# Prediction: terminal prints '5' and 'none' because the loop tells the program to print '5' and then tells it to print the value of x which is defined as
# the number_of_great_lakes() and since the tuple is empty, the program prints none for its value


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# Prediction: terminal prints '3' and '5'. the variable add(b,c) is defined then in the next line the program is told
# to print(b+c) , then in the third line inside the tuple b is given an integer value of 1 and c is given a value of 2, then
# the values of b and c are changed to 2 and 3 respectively so we get 1 + 2 = 3 followed by 2 + 3 = 5, so the printed outputs end
# up being '3' and '5'

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# Prediction: terminal prints '25'. the variable concatenate(b,c) is defined and in the next line the program is told to
# return str(b) + str(c) and in the third line, b and c are given the integer values of 2 and 5, and since the program is told
# to return str(b) + str(c) previously, we get the numbers 2 and 5 printed out as a string --> '25'


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# Prediction: terminal prints '100' '10' 'none' because b is given a value of 100 and then the program prints b, so '100'
# is printed to the terminal. Next we get an elif statement stating that if b < 10, return 5...since b = 100 we do not print 5 but instead
# print '10' as stated in the else statement because b = 100 and 100 is greater than 10. There is a return 7 after the return 10, but it is ignored
# because the elif loop already ended. Finally, we are told to print(number_of_oceans_or_fingers_or_continents()) which is empty so a 'none' is printed for that statement


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# Prediction: terminal prints '7' '14' '21' because of the elif loop and the print statements that follows. In the first print statement
# we are given (2,3) as the values of (b,c) and as the loop states, if b < c, return 7. 2 is less than 3 so '7' is printed. in the second
# print statement, (b,c) are given the values (5,3) and we go back to the loop...5 is not less than 3, therefore the else statement is executed ans
# we retuen 14, so '14' is printed to the terminal. In the third print statement we are told to print the sum of (2,3) and (5,3). We already determined
# from the loop that (2,3) returned 7 and (5,3) returned 14 and the sum of 7 + 14 = 21, so '21' is printed to the terminal


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# Prediction: terminal prints '8' because (b,c) is given the values of (3,5) and the first return statement says to return b+c,
# which is 8, so '8' is printed. The second return 10 is ignored because the first one is read in the program


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# Prediction: terminal prints '500' '500' '300' '500'because we are told the value of b is 500 and then told to print(b), so
# '500' is printed to the terminal. Next, we get a new variable in foobar() defined with a value of b as 300 inside the code block for
# foobar() and another print(b) statement. Since b still equals 500 outside of foobar(), '500' is once again printed to the terminal.
# Then the code calls foobar() so we go to line 113 and the print(b) statement inside the foobar() code block prints the value of b for
# foobar() which is 300, so '300' is printed to the terminal. Finally, after line 117 we have another print(b) statement and 500 is
# printed again so '500' is printed to the terminal again


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# Prediction: terminal prints '500' '500' '300' '500' because b is given the value of 500 then we are told to print(b) so '500'
# is printed to the terminal. Then we get a code block for the variable foobar() and after that another print(b) statement, so '500' is
# printed to the terminal again. After that we call on the foobar() function and we have a value of b as 300 and a print(b) and return b statement.
# the print(b) statement comes first, so '300' is printed to the terminal. We exit the foobar() code block and return to line 137 and print(b), so
# '500' is printed to the terminal again


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# Prediction: terminal prints '500' '500' '300' '300' because b is given the value of 500 at the beginning and then we are told to
# print(b) which is 500 so we get '500' printed to the terminal. Next we get a new variable foobar() defined and inside the foobar() block we
# get a new value for b which = 300. Next we are told to print(b) again, so we get '500' printed to the terminal once again. We then get b=foobar()
# and since b = 300 within foobar(), '300' is printed to the terminal. Finally, we get another print(b) statement and b is now 300 because of the
# previous line of code, so '300' is printed to the terminal again giving us '500', '500', '300', '300'


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# Prediction: terminal prints '1' '3' '2' because after foo() is defined, we are told to print(1) so '1' is printed to the terminal.
# Next bar() is called upon so we jump to line 169 where bar() is defined and told to print(3) so '3' is printed to the terminal. Afterwards we are
# told print(2) so '2' is printed to the terminal, then foo() is called upon again at the end, giving us '1', '3', '2'


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# Prediction: terminal prints '1' '3' '5' '10' because foo() is defined then we are told to print '1' to the terminal, next we get x = bar()
# and told to print(x) and bar() is defined as having the value of 3 so the print(x) command prints '3' to the terminal. We are still within the bar()
# block of code and after printing the value of x, we are told to return 5 so '5' is printed to the terminal. Finally, y = foo() and
# we print(y) which following the order of commands within the foo() block since foo() was called upon gives us the command return 10 which prints '10'
# to the terminal giving us '1', '3', '5', '10'