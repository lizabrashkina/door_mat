# for the code to run a user needs to enter two numbers with space in between
# the second number must be 3 times larger
# for instance: 9 27

n_m = input().split(" ")
n = int(n_m[0])
m = int(n_m[1])


start = int(((n-1)/2) + 1)
multiplier = -1

for i in range(1, start):
    multiplier += 2
    centre = ".|."*multiplier
    line = "-"*int(((m-len(centre))/2)) + centre + "-"*int(((m-len(centre))/2))
    print(line)

welcome_line = "-"*int(((m-7)/2)) + "WELCOME" + "-"*int(((m-7)/2))
print(welcome_line)

for i in range(start, 1, -1):
    centre = ".|."*multiplier
    line = "-"*int(((m-len(centre))/2)) + centre + "-"*int(((m-len(centre))/2))
    print(line)
    multiplier -= 2
