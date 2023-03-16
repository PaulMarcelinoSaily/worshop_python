print("Source code praktik 3.1.3. Daftar ")

squares = [1, 4, 9, 16, 25]
print(squares)

print("*******************************")

print(squares[0])
print(squares[-1])
print(squares[-3:])

print("*******************************")

print(squares[:])

print("*******************************")

print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
print(4 ** 3)
print(cubes[3])
print(cubes)

print(cubes.append(216))
print(cubes.append(7 ** 3))
print(cubes)

print("**********************************")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)

print("**********************************")

letters = ['a', 'b', 'c', 'd']
print(len(letters))

print("**********************************")

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])