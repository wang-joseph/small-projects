#---------------#
# Title -   computerSorterA.py
# Author -  Joseph Wang
# Date -    8/5/2019
# Desc -    An attempt at an algorithm that sorts people with computers, attempt 1
#---------------#

class Computer(object):
    def __init__(self, grouping, number, index):
        self.group = grouping
        self.number = number
        self.index = index
        self.occupied = False
        self.model = self.group + str(self.number)

    def __str__(self):
        return self.group + str(self.number) + " of grouping" + str(self.index)
        
    def __repr__(self):
        return self.model + " of grouping " + str(self.index) + ". Occupied: " + str(self.occupied)

    def occupy(self):
        self.occupied = True

    def evict(self):
        self.occupied = False

#---------------#

def unoccupySeats(computerList, grouping, computerModel):
    if computerModel == "all":
        for computer in computerList[grouping]:
            computer.evict()

    else:
        for computer in computerList[grouping]:
            if computer.model == computerModel:
                computer.evict()
                print("Model " + computer.model + " has been successffuly liberated.")

def findEqualSeatings(computerList, amount):
    print("Looking for entire full computer rows...")
    successfullyOccupied = False

    for grouping in range(len(computerList)):
        if successfullyOccupied:
            continue
        if len(computerList[grouping]) == amount:
            available = []
            for computer in computerList[grouping]:
                isTaken, number = checkToOccupy(computer)
                if not isTaken:
                    available.append(number)

            if len(available) == amount:
                occupyComputers(computerList, grouping, available, "multiple")
                successfullyOccupied = True
            
    if not successfullyOccupied:
        return findAdjustedSeatings(computerList, amount)
    return "Successfully found a full computer seatment! \n"

def findAdjustedSeatings(computerList, amount):
    print("Looking for partially filled computer rows...")
    successfullyOccupied = False
    for grouping in range(len(computerList)):
        available = []
        for computer in computerList[grouping]:
            if len(available) == amount:
                continue
            isTaken, number = checkToOccupy(computer)
            if not isTaken:
                available.append(number)

        if len(available) == amount:
            occupyComputers(computerList, grouping, available, "multiple")
            successfullyOccupied = True
    
        if successfullyOccupied:
            return "Successfully found a partial computer seatment! \n"
    
    print ("Looking for fragmented computer seatment...")
    return findFragmentedSeatings(computerList, amount)

def findFragmentedSeatings(computerList, amount):
    available = []
    groupings = []
    for grouping in range(len(computerList)):
        if len(available) == amount:
                continue
        for computer in computerList[grouping]:
            if len(available) == amount:
                continue

            isTaken, number = checkToOccupy(computer)
            if not isTaken:
                available.append(number)
                groupings.append(grouping)
    
    if len(available) == amount:
        for num in range(len(available)):
            occupyComputers(computerList, groupings[num], available[num], "single")
        return "Found a free fragmented computer section!\n"

    return "Couldn't find any computers for you. Sorry!\n"
            
def checkToOccupy(computer):
    if computer.occupied == True:
        return True, computer.number     
    return False, computer.number

def occupyComputers(computerList, grouping, amount, mode):
    if mode == "multiple":
        for i in amount:
            computerList[grouping][i].occupy()
    else:
        computerList[grouping][amount].occupy()

#---------------#      

computerLayout = [["A", "B", "C"], ["A", "B", "C"], ["A", "B"], ["A", "B", "C"], ["A"]]

computerList = []
for layout in range(len(computerLayout)):
    tempList = []
    for i in range(len(computerLayout[layout])):
        tempList.append(Computer(computerLayout[layout][i], i, layout))
    
    computerList.append(tempList)

#---------------#      
active = True

while active:
    action = input("\nWhat would you like to do? ")

    if action == "quit":
        active = False

    elif action == "occupy":
        validAnswer = False
        while not validAnswer:
            numberOfPeople = int(input("How many computers would you like? "))
            if numberOfPeople <= 0:
                print("Someone has to go on a computer...")
            else:
                validAnswer = True
            
        print(findEqualSeatings(computerList, numberOfPeople))
    
    elif action == "evict":
        evictedGrouping = int(input("What grouping would you like to evict? "))
        computerNum = input("Which computer is finished for today? ")
        unoccupySeats(computerList, evictedGrouping, computerNum)
        print("They have been forcefully cleared. \n")

    elif action == "show":
        for thing in computerList:
            print(thing)

    elif action == "nuke":
        for grouping in range(len(computerList)):
            unoccupySeats(computerList, grouping, "all")
        print("They have been forcefully cleared. \n")

        
        