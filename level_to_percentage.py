#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: November 2019
# This program takes the users level
#  and prints its percentage


def percentage(level):
    # This function processes the user input
    # process
    percentage = None

    if level == "4+" or level == "A+":
        percentage = 97
    elif level == "4" or level == "A":
        percentage = 90
    elif level == "4-" or level == "A-":
        percentage = 83
    elif level == "3+" or level == "B+":
        percentage = 78
    elif level == "3" or level == "B":
        percentage = 74
    elif level == "3-" or level == "B-":
        percentage = 71
    elif level == "2+" or level == "C+":
        percentage = 68
    elif level == "2" or level == "C":
        percentage = 64
    elif level == "2-" or level == "C-":
        percentage = 61
    elif level == "1+" or level == "D+":
        percentage = 58
    elif level == "1" or level == "D":
        percentage = 54
    elif level == "1-" or level == "D-":
        percentage = 51
    elif level == "0+" or level == "R+":
        percentage = 45
    elif level == "0" or level == "R":
        percentage = 35
    elif level == "0-" or level == "R-":
        percentage = 15
    elif level == "NE":
        percentage = "No Evidence"
    else:
        percentage = "Not a Valid Mark"

    return percentage


def main():
    # This function takes the user input
    # input
    grade = input("Enter your level: ")
    print("")
    # enters function
    Percentage = percentage(grade)
    # output
    print(Percentage)


if __name__ == "__main__":
    main()
