from random import choice

rps_map = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

pl_name = raw_input("%sInput player name >> " % ('\n' * 100))
ai_name = choice(["R2D2", "HAL 9000", "C3PO", "T-800", "T-1000",
                  "Nexus", "Marvin", "Iron Giant", "Eve", "Skynet"])
pl_score = 0
ai_score = 0

print("\n%s vs %s\n%s" % (pl_name, ai_name, '-' * (len(pl_name + ai_name) + 4)))

while True:
    pl_input = raw_input("\nInput [rock|scissors|paper|quit] >> ")
    if pl_input == "quit":
        break
    elif pl_input in rps_map.keys():
        ai_input = choice(rps_map.keys())
        print("\n%s: %s\n%s: %s\n" % (pl_name, pl_input, ai_name, ai_input))
        if rps_map[pl_input] == ai_input:
            print("%s wins" % pl_name)
            pl_score += 1
        elif rps_map[ai_input] == pl_input:
            print("%s wins" % ai_name)
            ai_score += 1
        else:
            print("Draw xD")
    else:
        print("Unknown command")

print("\nScore:\n-----")
print("%s - %d : %d - %s\n" % (pl_name, pl_score, ai_score, ai_name))
