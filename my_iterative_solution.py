# Rules:
# only top most disk can be moved
# only can move 1 disk at a time
# For empty towers with no disks, a disk of any size can be put into it
# For towers with disks, only smaller disk can be put on top of bigger disk

def reversed_tower_order(tower):
    # syntax range(start, stop, step)
    result = ""
    for i in range(len(tower)-1, -1, -1):   
        result += str(tower[i]) + " "
    return result

# Towers' status will be printed from initialization and for every move to see the transfer 
def print_current_towers(count):
    print("Step no.", count)
    print("tower_A = ", reversed_tower_order(tower_A))
    print("tower_B = ", reversed_tower_order(tower_B))
    print("tower_C = ", reversed_tower_order(tower_C))
    print("")

# "legal move" means only a smaller disk can move on top of a bigger disk, or on top of an 
# at any point in time, this function checks any two towers required for disk transfer
# checks include both sides so it will work for both directions
# syntax insert(index)
# syntax pop function takes in index number as arguments

def make_legal_move(tower1, tower2):
    if len(tower2) == 0:
        tower2.insert(0, tower1[0])
        tower1.pop(0)
    
    elif len(tower1) == 0:
        tower1.insert(0, tower2[0])
        tower2.pop(0)

    else:
        if tower1[0] > tower2[0]:
            tower1.insert(0, tower2[0])
            tower2.pop(0)

        else:
            tower2.insert(0, tower1[0])
            tower1.pop(0)



def solve(n, from_tower, to_tower, support_tower):

    count = 0

    if n == 1:
        while len(to_tower) != n:
            make_legal_move(from_tower, to_tower)
            count += 1
            print_current_towers(count)

    elif n % 2 == 0:
        while len(to_tower) != n:
            make_legal_move(from_tower, support_tower)
            count += 1
            print_current_towers(count)

            make_legal_move(from_tower, to_tower)
            count += 1
            print_current_towers(count)

            make_legal_move(support_tower, to_tower)
            count += 1
            print_current_towers(count)

    else:
        # count = 0
        while len(to_tower) != n:
            
            make_legal_move(from_tower, to_tower)
            count += 1
            print_current_towers(count)
            if len(to_tower) == n:
                break

            make_legal_move(from_tower, support_tower)
            count += 1
            print_current_towers(count)

            make_legal_move(to_tower, support_tower)
            count += 1
            print_current_towers(count)


# Program starts with asking user input for no. of disks
print("Please enter no. of disks for your tower height :")
n = int(input())

# accounts for user input less than 1 disk
if n < 1:
    print("You need at least 1 disk to play Towers of Hanoi. Try running the game again.")

# any user input of at least 1 disk and above will run the program
else:
    # towers will take on the role as "FROM Tower", "TO Tower" and "SUPPORT Tower"
    # initialize the 3 towers, with the FROM Tower containing the number of disks as inputted by user
    
    # FROM Tower
    tower_A = []
    tower_A = [i+1 for i in range(n)] 
    
    # TO Tower
    tower_B = [] 

    # SUPPORT Tower
    tower_C = [] 

    print("")
    print("*** Starting Towers ***")
    print_current_towers(0)
    

    solve(n, tower_A, tower_B, tower_C)


