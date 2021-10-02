def reverseDisplay(number):
    # base case
    if len(str(number)) < 2:
        return (number)
    else:
        # get the last number
        lastNumber = str(number)[-1:]
        print(lastNumber)
        # get everything else
        print("*****")
        everythingElse = int(str(number)[:-1])
        print(everythingElse)
        print("*")
        return (lastNumber  + str(reverseDisplay(everythingElse)))

print(reverseDisplay(123))