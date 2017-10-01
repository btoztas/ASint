print("### EXAMPLE 1 ###")
f = open('data', 'r')
s1 = f.read()
print(s1)

print("### EXAMPLE 2 ###")
f2 = open('data', 'r')
v1 = f2.readlines()
for s in v1:
    print(s)

print("### EXAMPLE 3 ###")
f2 = open('data', 'r')
for line in f2:
    print(line)
