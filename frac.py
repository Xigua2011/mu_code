from fractions import Fraction
a = Fraction('0.3333333333333333').limit_denominator()
b = Fraction('1/6')
c = a/b
print(a)
