#Programmed by Brandon Stewart
#Comfy equations dervied by Jett Huffaker and T.K. Wallace
#Ver 1.2
#Last modified 11/15/2017

def get_vals():

    test = True

    while test:
        energy = raw_input("Enter your energy on a scale from 0-10\n")
        try:
            energy = float(energy)
        except ValueError:
            print("Input is not a number!")
            continue
        if(energy > 10 or energy < 0):
            print("Energy value out of range")
            continue
        break


    while test:
        ent = raw_input("Enter the quality of your entertainment on a scale from 0-10\n")
        try:
            ent = float(ent)
        except ValueError:
            print("Input is not a number!")
            continue
        if(ent > 10 or ent < 0):
            print("Entertainment quality value out of range")
            continue
        break

    while test:
        snack = raw_input("Enter the quality of the snacks on a scale from 0-10\n")
        try:
            snack = float(snack)
        except ValueError:
            print("Input is not a number!")
            continue
        if(snack > 10 or snack < 0):
            print("Snack value out of range")
            continue
        break

    while test:
        amount = raw_input("Enter the amount of snacks on a scale from 0-10\n")
        try:
            amount = float(amount)
        except ValueError:
            print("Input is not a number!")
            continue
        if(amount > 10 or amount < 0):
            print("Amount of snacks out of range")
            continue
        break

    while test:
        stand = raw_input("Are you standing? 1 for yes, 0 for no\n")
        try:
            stand = float(stand)
        except ValueError:
            print("Input is not a number!")
            continue
        if (stand < 0 or stand > 1):
            print("Energy value out of range")
            continue
        break

    while test:
        shoe = raw_input("Enter the comfort level of your shoes a scale from 0-10\n")
        try:
            shoe = float(shoe)
        except ValueError:
            print("Input is not a number!")
            continue
        if(shoe > 10 or shoe < 0):
            print("Shoe comfort level out of range")
            continue
        break

    while test:
        time = raw_input("Enter the time spent standing in minutes\n")
        try:
            time = float(time)
        except ValueError:
            print("Input is not a number!")
            continue
        break

    while test:
        ment = raw_input("Enter your mental stability ranging from -10(heavily depressed) to 10(very happy)\n")
        try:
            ment = float(ment)
        except ValueError:
            print("Input is not a number!")
            continue
        if(ment < -10 or ment > 10):
            print("Mental stability out of range")
            continue
        break

    return energy, ent, snack, amount, stand, shoe, time, ment

def comfy(energy, ent, snack, amount, stand, shoe, time, ment):
    return (energy * ent) + (snack * amount) - ((stand - (1./3.)*(shoe/10.)) * time * stand) + ment

if __name__ == "__main__":
    energy, ent, snack, amount, stand, shoe, time, ment = get_vals()
    res = comfy(energy, ent, snack, amount, stand, shoe, time, ment)
    res = round(res, 2)
    print "Your comfy level is:", res
    raw_input("Press Any key to exit")
