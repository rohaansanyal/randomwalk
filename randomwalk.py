import random
import statistics

num = 0
lst = []
#total = 0

print(
    "random walk is a concept where a particle on a number line goes up or down based on chance for a specific number of times. this program simulates it."
)
print()
totalrun = int(
    input("how many times would you like to simulate random walk? "))
simrun = int(
    input("how many times would you like to randomly walk (per simulation)? "))
print()
leftprob = int(
    input(
        "what probability would you like for the particle to move one left? (whole number out of 100) "
    ))
rightprob = 100 - leftprob
print("the probability of the particle moving right is " + str(rightprob) +
      "%")

for j in range(totalrun):

    num = 0

    for i in range(simrun):  #for loop to simulate single walk

        upordown = random.randint(0, 100)

        if upordown <= leftprob:  #particle moves left

            num -= 1
            #print("particle moved up on " + str(leftprob) + "/" + str(rightprob) + " chance")

        if upordown > leftprob:  #particle moves right

            num += 1
            #print("particle moved down on " + str(leftprob) + "/" + str(rightprob) + " chance")

    lst.append(num)

print("median value for all simulations: " + str(statistics.median(lst)))
print("mean value for all simulations: " + str(statistics.mean(lst)))
