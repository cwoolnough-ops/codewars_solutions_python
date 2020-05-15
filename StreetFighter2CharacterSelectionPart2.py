# handles horizontal rotation
def horizontal_move_checker(num, list, index):
    if num > len(list[index[0]]) - 1:
        num = 0
    if num < 0:
        num = len(list[index[0]]) - 1
    return num

  # prevents vertical movement off the board


def vertical_move_checker(num, list, index):
    if num > len(list) - 1:
        num = num - 1
    if num < 0:
        num = 0
    return num


def super_street_fighter_selection(fighters, position, moves):
    index = list(position)  # holds the current space on the character list
    move_order = []  # return value

    for move in moves:
      # handles upward moves
        if move == "up":
            index[0] = index[0] - 1
            index[0] = vertical_move_checker(index[0], fighters, index)

          # if space is empty revert the move
        if fighters[index[0]][index[1]] == "":
            index[0] = index[0] + 1

      # handles downward moves
        if move == "down":
            index[0] = index[0] + 1
            index[0] = vertical_move_checker(index[0], fighters, index)

          # if space is empty revert the move
        if fighters[index[0]][index[1]] == "":
           index[0] = index[0] - 1

      # handles leftward moves
        if move == "left":
            index[1] = index[1] - 1
            index[1] = horizontal_move_checker(index[1], fighters, index)

          # continue moving left untill were at a fighter
        while fighters[index[0]][index[1]] == "":
            index[1] = index[1] - 1
            index[1] = horizontal_move_checker(index[1], fighters, index)

      # handles rightward moves
        if move == "right":
            index[1] = index[1] + 1
            index[1] = horizontal_move_checker(index[1], fighters, index)

          # continue moving right untill were at a fighter
        while fighters[index[0]][index[1]] == "":
            index[1] = index[1] + 1
            index[1] = horizontal_move_checker(index[1], fighters, index)

      # add the fighter at the new postion to our return value
        move_order.append(fighters[index[0]][index[1]])
    return move_order
