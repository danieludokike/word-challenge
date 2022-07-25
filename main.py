def print_el_structure(char):
    [print(f"{char}") if i < 5 else print(f"{char}" * i) for i in range(6)]


def print_o_structure(char):
    _val = ""
    for _row in range(0, 7):
        for _col in range(0, 7):
            if (((_col == 1 or _col == 5) and _row != 0 and _row != 6) or (
                    (_row == 0 or _row == 6) and 1 < _col < 5)):
                _val = _val + f"{char}"
            else:
                _val = _val + " "
        _val = _val + "\n"
    print(_val)


def print_w_structure(char):
    str2 = ""
    for __row in range(0, 7):
        for __Col in range(0, 7):
            if ((__Col == 1 or __Col == 5) and __row < 6) or ((__row == 5 or __row == 4) and __Col == 3) or (
                    __row == 6 and (__Col == 2 or __Col == 4)):
                str2 = str2 + f"{char}"
            else:
                str2 = str2 + " "
        str2 = str2 + "\n"
    print(str2)


while True:
    char_input = input("Enter a character: ")
    if len(char_input) == 1:
        break

# # PRINT C STRUCTURE
for row in range(7):
    for col in range(5):
        if (col == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0)):
            print(f"{char_input}", end=" ")
        else:
            print(end=" ")
    print()
print()
print()

# # PRINT H STRUCTURE
val = ""
for Row in range(0, 7):
    for Col in range(0, 7):
        if (Col == 1 or Col == 5) or (Row == 3 and 1 < Col < 6):
            val = val + f"{char_input}"
        else:
            val = val + " "
    val = val + "\n"
print(val)

# # PRINT E STRUCTURE
[print(f"{char_input}" * i) for i in [7, 2, 7, 2, 7]]
print()

#  PRINT L STRUCTURE
for _ in range(2):
    print_el_structure(char_input)
    print()

# PRINT O STRUCTURE
print_o_structure(char_input)

# print w structure
print_w_structure(char_input)
print()

# PRINTING WORLD STRUCTURE
# print w structure
print_w_structure(char_input)
# PRINT O STRUCTURE
print_o_structure(char_input)

# PRINT R FUNCTION
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if column == 1 or ((row == 0 or row == 3) and 1 < column < 5) or (column == 5 and row != 0 and row < 3) or (
                column == row - 1 and row > 2):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)

# PRINT L STRUCTURE
print_el_structure(char_input)

# PINT D FUNCTION
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if column == 1 or ((row == 0 or row == 6) and (1 < column < 5)) or (column == 5 and row != 0 and row != 6):
            result_str = result_str + f"{char_input}"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)
