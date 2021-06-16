def tic_tac_toe(value_lst):
    print("     |     |     ")
    print("  {}  |  {}  |  {} ".format(value_lst[0], value_lst[1], value_lst[2]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {} ".format(value_lst[3], value_lst[4], value_lst[5]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {} ".format(value_lst[6], value_lst[7], value_lst[8]))
    print("     |     |     ")
    

tic_tac_toe(list(range(1,10)))