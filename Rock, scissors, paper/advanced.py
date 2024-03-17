import random

# Global variables
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
ANSWERS = (ROCK, PAPER, SCISSORS)

def compare_simple(gamer_answer, comp_answer):
    if gamer_answer == comp_answer:
        return 0
    elif gamer_answer == ROCK:
        if comp_answer == PAPER:
            return -1
        else:
            return 1
    elif gamer_answer == SCISSORS:
        if comp_answer == PAPER:
            return 1
        else:
            return -1
    elif gamer_answer == PAPER:
        if comp_answer == ROCK:
            return 1
        else:
            return -1

def compare_advance(gamer_answer, comp_answer):
    if gamer_answer == comp_answer:
        return 0
    elif gamer_answer == ROCK:
        return -1 if comp_answer == PAPER else 1
    elif gamer_answer == SCISSORS:
        return 1 if comp_answer == PAPER else -1
    elif gamer_answer == PAPER:
        return 1 if comp_answer == ROCK else -1

def compare_matrix(gamer_answer, comp_answer):
    truth_table = {
        ROCK: {
            ROCK: 0,
            PAPER: -1,
            SCISSORS: 1
        },
        PAPER: {
            ROCK: 1,
            PAPER: 0,
            SCISSORS: -1
        },
        SCISSORS: {
            ROCK: -1,
            PAPER: 1,
            SCISSORS: 0
        }
    }
    
    return truth_table[gamer_answer][comp_answer]

def print_winner(game_result, gamer_answer):
    if game_result == 0:
        print("Draw!")
    elif game_result == 1:
        print("User wins with " + gamer_answer)
    else:
        print("User lose with " + gamer_answer)

def main():
    print("Welcome to the rock, paper & scissors game with computer!")
    gamer = input("Enter your name: ")

    while True:
        gamer_answer = input(" %s: Choose rock, scissors or paper: " % gamer).lower()
        if gamer_answer not in ANSWERS:
            print("Invalid Entry! Try again")
            continue
        
        comp_answer = random.choice(ANSWERS)
        print("Computer chose: " + comp_answer)
    
        game_result = compare_matrix(gamer_answer, comp_answer)
        print_winner(game_result, gamer_answer)

        willing = input("Do you want to play one more time? ").lower()
        if willing != "yes":
            break

if __name__ == '__main__':
    # for gamer_answer in ANSWERS:
    #     for comp_answer in ANSWERS:
    #         game_result = compare_matrix(gamer_answer, comp_answer)
    #         print(f"gamer_answer: {gamer_answer},\t comp_answer: {comp_answer}:", end="\t")
    #         print_winner(game_result, gamer_answer)
    main()
