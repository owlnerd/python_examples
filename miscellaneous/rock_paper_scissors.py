from random import choice

rps_map = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

pl_name = raw_input("%sInput player name >> " % ('\n' * 100))
ai_name = choice(["R2D2", "HAL 9000", "C3PO", "T-800", "T-1000",
                         "Nexus", "Marvin", "Iron Giant", "Eve", "Skynet"])
pl_scr = 0
ai_scr = 0

print("\n%s vs %s\n%s" % (pl_name, ai_name, '-' * (len(pl_name + ai_name) + 4)))

while True:
    inpt = raw_input("\nInput [rock|scissors|paper|quit] >> ")
    if inpt == "quit":
        break
    elif inpt in rps_map.keys():
        ai_sel = choice(rps_map.keys())
        print("\n%s: %s\n%s: %s\n" % (pl_name, inpt, ai_name, ai_sel))
        if rps_map[inpt] == ai_sel:
            print("%s wins" % pl_name)
            pl_scr += 1
        elif rps_map[ai_sel] == inpt:
            print("%s wins" % ai_name)
            ai_scr += 1
        else:
            print("Draw xD")
    else:
        print("Unknown command")

print("\nScore:\n-----")
print("%s - %d : %d - %s\n" % (pl_name, pl_scr, ai_scr, ai_name))
