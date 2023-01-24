from typing import List
from random import randint
import matplotlib.pyplot as plt

PEOPLE_CNT: int = 20  # Number of random people to consider
SIM_CNT: int = 1000  # Number of simulations to run


# A simulation of PEOPLE_CNT people with random birthdays
def simulation(people_cnt: int) -> int:
    # Create a list of random birthdays
    bdays: List[int] = []
    for _ in range(people_cnt):
        bdays.append(randint(1, 365))
    # Return the number of people that share their birthday with at least another person
    return sum([1 if bdays.count(bdays[i]) > 1 else 0 for i in range(people_cnt)])


# Use the Monte Carlo method and run the simulation SIM_CNT times to get more accurate results
def monte_carlo(people_cnt: int, simulations_cnt: int) -> List[int]:
    same_bday_cnts: List[int] = []
    for _ in range(simulations_cnt):
        same_bday_cnts.append(simulation(people_cnt))
    return same_bday_cnts


# Draw an histogram to visualize the computed data and save it
def draw_histogram(same_bday_cnts: List[int], probability: float) -> None:
    plt.figure(figsize=(8, 6.5), dpi=80)
    plt.hist(same_bday_cnts)
    plt.title(
        f"Birthday paradox in a set of {PEOPLE_CNT} random people\nusing the Monte Carlo method",
        fontsize=16, fontweight="bold", pad=12
    )
    plt.xlabel("Number of people that share their birthday with at least another person", fontsize=12, labelpad=10)
    plt.ylabel("Number of simulations (absolute frequency)", fontsize=12, labelpad=10)
    plt.subplots_adjust(bottom=0.22)
    plt.figtext(
        0.03, 0.03,
        f"The probability that, in a set of {PEOPLE_CNT} random people, at least two will share a\n" +
        "birthday is " + r"$\bf{" + str(probability) + "\%" + "}$",
        ha="left", fontsize=14
    )
    plt.savefig("output.png")


def main() -> None:
    # Run Monte Carlo
    same_bday_cnts = monte_carlo(PEOPLE_CNT, SIM_CNT)
    # Calculate the probability of two people having the same birthday
    probability: float = (SIM_CNT - same_bday_cnts.count(0)) * 100 / SIM_CNT
    print(f"The probability that, in a set of {PEOPLE_CNT} random people, " +
          f"at least two will share a birthday is {probability}%")
    # Draw the histogram (duh)
    draw_histogram(same_bday_cnts, probability)


if __name__ == "__main__":
    main()
