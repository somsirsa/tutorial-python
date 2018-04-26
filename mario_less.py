# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 20:37:58 2018

@author: somsirsa
"""
def main():
    height = get_height()

    for i in range(height):
        num_spaces = height - i + 1
        num_hashes = i + 1

        for j in range(num_spaces):
            if j == 1:
                print("\n")
                print(" ", end="")
            else:
                print(" ", end="")
        #num_spaces -= 1

        for k in range(num_hashes):
            if k == num_hashes:
                print("#")
            else:
                print("#", end="")
        #num_hashes -= 1
    print("\n", end="")



def get_height():
    h = int(input("Height: "))
    while True:
        if h <= 1 or h >= 26 or h == None:
            h = get_height()
            break
        else:
            return h

if __name__ == "__main__":
    main()