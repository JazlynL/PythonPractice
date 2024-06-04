#main function
def main():
    #input value from user
    y = int(input("What's y?"))
    # call function below, return boolean value
    if is_even(y):
        print("Even")
    else:
        print("Odd")


def is_even(y):
    #version 1
    #if y % 2 == 0:
     #   return True
    #else:
     #   return False


    #version 2 1 line
     #return True if y % 2 == 0 else False


    # version 3
    return y % 2 == 0


main()
