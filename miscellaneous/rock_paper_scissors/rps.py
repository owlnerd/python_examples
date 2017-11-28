from random import choice

# Dict of rock, paper, scissors objects. Key "defeats" value
# An elegant soution to obscure if-elif-else structures
rps_map = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

pl_name = raw_input("%sInput player name >> " % ('\n' * 100))
# Randomly selectin ai_name from a file
ai_name = choice(open("ai_names.txt", "r").readlines()).strip('\n')
# Scores
pl_score = 0
ai_score = 0
# Number of rounds played
rounds = 0

print("\n%s vs %s\n%s" % (pl_name, ai_name, '-' * (len(pl_name + ai_name) + 4)))

while True:
    # Get player input
    pl_input = raw_input("\nInput [rock|scissors|paper|quit] >> ")
    # If input equals "quit", exit loop
    if pl_input == "quit":
        break
    # If input equals rock, paper or scissors
    elif pl_input in rps_map.keys():
        rounds += 1
        # Get ai input (chosen randomly from dict keys)
        ai_input = choice(rps_map.keys())
        print("\n%s: %s\n%s: %s\n" % (pl_name, pl_input, ai_name, ai_input))
        # If the value of the dict element with players input as key
        # equals ai input, player wins
        if rps_map[pl_input] == ai_input:
            print("%s wins" % pl_name)
            pl_score += 1
        # Otherwise, if the value of the dict element with ai input as
        # key equals player input, ai wins
        elif rps_map[ai_input] == pl_input:
            print("%s wins" % ai_name)
            ai_score += 1
        # Otherwise, round is draws
        else:
            print("Draw xD")
    else:
        print("Unknown command")

print("\nRounds: %d\n------" % rounds)
print("\nScore:\n-----")
print("%s - %d : %d - %s\n" % (pl_name, pl_score, ai_score, ai_name))
