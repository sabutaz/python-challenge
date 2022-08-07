# 1. Convert radians into degrees
import math


def radian_to_degree(rad):
    deg = rad * (180 / math.pi)
    return deg


print(radian_to_degree(10))


# 2. Sort a list

def list_sorter(the_list, sort_order):
    if sort_order == "asc":
        the_list.sort()
    elif sort_order == "desc":
        the_list.sort(reverse=True)
    elif sort_order == "none":
        return the_list
    else:
        raise ValueError
    return the_list


try:
    the_sorted_list = list_sorter([7, 11, 1, 32, 6, 9, 99, 2], "sdfgsdg")
except ValueError:
    print("Sort order value must be : asc,desc or none")
else:
    print("Sorted list :", the_sorted_list)


# 3. Convert a decimal number into binary
bin_number = 50


def decimal_to_binary(dec):
    div_dec = int(dec/2)
    if div_dec != 0:
        decimal_to_binary(div_dec)
    print(dec % 2, end='')


print(f"the number {bin_number} in decimal is - ", end='')
decimal_to_binary(bin_number)


# 4. Count the vowels in a string
the_word = "alelulya"
vowels = "aeio"
count_before = len(the_word)
print(count_before)
for char in vowels:
    the_word = the_word.replace(char, '')
print(count_before - len(the_word))

