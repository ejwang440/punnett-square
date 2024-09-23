import random
import matplotlib.pyplot as plt

from collections import namedtuple
Creature = namedtuple("Creature", ["shape", "color"])


def choose_feature(pheno1, pheno2):
    """
    Given two phenotypes (strings of two letters),
    returns a new phenotype (a string of two letters
    where one comes from each of the original two, each
    with probability 1/2).
    """
    pheno = ""
    r = random.uniform(0, 1)
    if r <= 0.5:
        pheno = pheno1[0]
    else:
        pheno = pheno1[1]

    q = random.uniform(0, 1)
    if q <= 0.5:
        pheno += pheno2[0]
    else:
        pheno += pheno2[1]
    return pheno


# print(choose_feature("Aa", "Rr"))


def cross(c1, c2):
    """
    Returns a new Creature that is a child of c1 and c2.
    """
    return Creature(
        shape=choose_feature(c1.shape, c2.shape),
        color=choose_feature(c1.color, c2.color)
    )


def is_green(creature):
    """
    Returns True if the creature's color phenotype is
    recessive (both genes are "a") and False otherwise.
    """
    color_phen = creature.color
    if color_phen == "aa":
        return True
    return False


def is_wrinkled(creature):
    """
    Returns True if the creature's shape phenotype is
    recessive (both genes are "r") and False otherwise.
    """
    if creature.shape == "rr":
        return True
    return False


def percentage_green(population):
    """
    Returns the percentage of the population
    (which is a list of creatures) that are green.
    """
    perc = 0.0
    for i in range(len(population)):
        if is_green(population[i]) == True:
            perc += 1.0
    return float(perc/len(population))*100


def percentage_wrinkled(population):
    """
    Returns the percentage of the population
    (which is a list of creatures) that are wrinkled.
    """
    perc = 0.0
    for i in range(len(population)):
        if is_wrinkled(population[i]) == True:
            perc += 1.0
    return float(perc/len(population))*100


def percentage_green_and_wrinkled(population):
    """
    Returns the percentage of the population
    (which is a list of creatures) that are *both* green and wrinkled.
    """
    perc = 0.0
    for i in range(len(population)):
        if is_green(population[i]) == True and is_wrinkled(population[i]) == True:
            perc += 1.0
    return float(perc/len(population))*100


def generation(population):
    """
    Returns a new generation (list) of Creatures by randomly
    choosing 50,000 pairs of parents from the population
    and crossing them into a child.
    """
    genZ = []
    i = 0
    for i in range(50000):
        r1 = random.randint(0, len(population)-1)
        r2 = random.randint(0, len(population)-1)
        if r1 != r2:
            genZ.append(cross(population[r1], population[r2]))
            i += 1
        else:
            i = i
    return genZ


# Initialize a population of creatures where nobody has
# *any* recessive genes.
population = []
for shape in ["Rr", "RR", "rR"]:
    for color in ["Aa", "AA", "aA"]:
        population.append(Creature(shape=shape, color=color))

# Do simulation
xs = []
green = []
wrinkled = []
both = []
for i in range(10):
    xs.append(i)
    green.append(percentage_green(population))
    wrinkled.append(percentage_wrinkled(population))
    both.append(percentage_green_and_wrinkled(population))
    population = generation(population)

# Plot the trends of green, wrinkled and both.
plt.plot(xs, green, 'g-')
plt.plot(xs, wrinkled, 'b--')
plt.plot(xs, both, "r--")
plt.savefig('out.png')
