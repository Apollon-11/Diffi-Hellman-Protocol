# Alice & Bob a and b exchange numbers a & b
a = 3  # Primitive root
n = 23  # Module

# (Alice)
Xa = 7  # Secret number of the first subscriber
m = pow(a, Xa, n)  # m transferred to the second subscriber
print(m)

# (Bob)
Xb = 31  # Secret number of the second subscriber
q = pow(a, Xb, n)  # q transferred to the first subscriber
print(q)

# (Alice)
m1 = pow(q, Xa, n)
print(m1)  # The secret key
# (Bob)
q1 = pow(m, Xb, n)
print(q1)  # The secret key
