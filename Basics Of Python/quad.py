import cmath as cm

a = int(input("Enter coefficient of x^2 :"))
b = int(input("Enter coefficient of x   :"))
c = int(input("Enter the constant term  :"))

print ("The solution of ", a, " x^2 + ", b, " x + ", c, " are ", ((-1) * b + cm.sqrt(b * b - 4 * a * c)) / (2 * a),
       "and", ((-1) * b + cm.sqrt(b * b - 4 * a * c)) / (2 * a))
