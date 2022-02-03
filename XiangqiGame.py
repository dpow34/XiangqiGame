
class XiangqiGame:
    """Represents a game of Xiangqi"""

    def __init__(self):
        soldier1 = Soldier("red", 0, 3, 1)
        soldier2 = Soldier("red", 2, 3, 2)
        soldier3 = Soldier("red", 4, 3, 3)
        soldier4 = Soldier("red", 6, 3, 4)
        soldier5 = Soldier("red", 8, 3, 5)
        soldier6 = Soldier("black", 0, 6, 6)
        soldier7 = Soldier("black", 2, 6, 7)
        soldier8 = Soldier("black", 4, 6, 8)
        soldier9 = Soldier("black", 6, 6, 9)
        soldier10 = Soldier("black", 8, 6, 10)
        elephant1 = Elelphant("red", 2, 0, 1)
        elephant2 = Elelphant("red", 6, 0, 2)
        elephant3 = Elelphant("black", 2, 9, 3)
        elephant4 = Elelphant("black", 6, 9, 4)
        chariot1 = Chariot("red", 0, 0, 1)
        chariot2 = Chariot("red", 8, 0, 2)
        chariot3 = Chariot("black", 0, 9, 3)
        chariot4 = Chariot("black", 8, 9, 4)
        horse1 = Horse("red", 1, 0, 1)
        horse2 = Horse("red", 7, 0, 2)
        horse3 = Horse("black", 1, 9, 3)
        horse4 = Horse("black", 7, 9, 4)
        advisor1 = Advisor("red", 3, 0, 1)
        advisor2 = Advisor("red", 5, 0, 2)
        advisor3 = Advisor("black", 3, 9, 3)
        advisor4 = Advisor("black", 5, 9, 4)
        cannon1 = Cannon("red", 1, 2, 1)
        cannon2 = Cannon("red", 7, 2, 2)
        cannon3 = Cannon("black", 1, 7, 3)
        cannon4 = Cannon("black", 7, 7, 4)
        general1 = General("red", 4, 0, 1)
        general2 = General("black", 4, 9, 2)
        self._board = [[[] for x in range(9)] for y in range(10)]
        self._board[0][0].append(chariot1)
        self._board[0][1].append(horse1)
        self._board[3][4].append(elephant1)
        self._board[0][3].append(advisor1)
        self._board[0][4].append(general1)
        self._board[0][5].append(advisor2)
        self._board[0][6].append(elephant2)
        self._board[0][7].append(horse2)
        self._board[0][8].append(chariot2)
        self._board[2][4].append(cannon1)
        self._board[2][7].append(cannon2)
        self._board[3][0].append(soldier1)
        self._board[3][2].append(soldier2)
        self._board[3][4].append(soldier3)
        self._board[3][6].append(soldier4)
        self._board[3][8].append(soldier5)
        self._board[9][0].append(chariot3)
        self._board[9][1].append(horse3)
        self._board[9][2].append(elephant3)
        self._board[9][3].append(advisor3)
        self._board[6][0].append(general2)
        self._board[9][5].append(advisor4)
        self._board[9][6].append(elephant4)
        self._board[9][7].append(horse4)
        self._board[6][4].append(chariot4)
        self._board[7][1].append(cannon3)
        self._board[7][7].append(cannon4)
        self._board[6][0].append(soldier6)
        self._board[6][2].append(soldier7)
        self._board[6][4].append(soldier8)
        self._board[6][6].append(soldier9)
        self._board[6][8].append(soldier10)
        self._game_state = 'UNFINISHED'
        self._player_turn = 'red'
        self._black_gen_x = 4
        self._black_gen_y = 9
        self._black_gen_status = 'NOT_CHECK'
        self._red_gen_status = 'NOT_CHECK'
        self._red_gen_x = 4
        self._reg_gen_y = 0



    def get_game_state(self):
        """Returns the current game state"""
        return self._game_state

    def get_board(self):
        """Returns self._board"""
        return self._board

    def print_board(self):
        """Prints board for testing"""
        for i in range(len(self._board)):
            print(self._board[i])
        print('')

    def set_red_gen(self, x, y):
        """Sets red general's x and y coordinates"""
        self._red_gen_x = x
        self._reg_gen_y = y

    def set_black_gen(self, x, y):
        """Sets black general's x and y coordinates"""
        self._black_gen_x = x
        self._black_gen_y = y



    def is_in_check(self, player):
        """* A method called is_in_check that takes as a parameter either 'red' or 'black' and returns True if that
        player is in check, but returns False otherwise."""

    def make_move(self, current, target, moves=[0]):
        """Returns true if the move is legal and increases the number of moves by 1.
        If move is not legal returns False"""
        alpha_num = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "a": 0, "b": 1,
                     "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8}  # dictionary to decode coordinates
        current_x = alpha_num.get(current[0])
        current_y = alpha_num.get(current[1:])
        target_x = alpha_num.get(target[0])
        target_y = alpha_num.get(target[1:])
        if self._game_state == 'RED_WON' or self._game_state == 'BLACK_WON':
            return False
        if moves[0] % 2 == 0:  # if move is even
            self._player_turn = 'red'
        else:
            self._player_turn = 'black'  # if move is odd
        if target_x < 0 or target_x > 8 or target_y < 0 or target_y > 9:  # if move is not on the board
            return False
        if not self._board[current_y][current_x]:  # if there is not a piece at the initial spot
            return False
        if self._board[current_y][current_x] is not None:  # if there is a piece at the initial spot
            piece = self._board[current_y][current_x][0]
            if piece.get_player() == self._player_turn:  # checks to see if piece belongs to the correct player
                if piece.fly_general(self._board, current_x, current_y, target_x) == False:
                    # if moving the piece will cause the flying general rule
                    return False
                if isinstance(piece, Soldier):  # if piece object is a Soldier
                    if self.soldier_moves(self._player_turn, current_x, current_y, target_x, target_y,[piece]) == False:
                        # if the move is not legal
                        return False
                    # need to check if king is in check
                    else:
                        # soldier is moved
                        moves[0] += 1  # increases moves by 1
                        if piece.get_player() == 'red':
                            if piece.check_general(self._black_gen_x, self._black_gen_y) == True:
                                # if moving the soldier put the general in check
                                self._black_gen_status = 'IN_CHECK'
                            if piece.get_player() == 'black':
                                if piece.check_general(self._red_gen_x, self._red_gen_y) == True:
                                    # if moving the soldier put the general in check
                                    self._black_gen_status = 'IN_CHECK'
                        return True
                elif isinstance(piece, Elelphant):  # if piece object is an Elephant
                    if self.elephant_moves(self._player_turn, current_x, current_y, target_x, target_y,[piece]) == False:
                        # if the move is not legal
                        return False
                    # need to check if king is in check
                    else:
                        # moves elephant
                        moves[0] += 1  # increases moves by 1
                        return True
                elif isinstance(piece, General):  # if piece object is a General
                    if self.general_moves(self._player_turn, current_x, current_y, target_x, target_y,[piece]) == False:
                        # if the move is not legal
                        return False
                    # need to check if king is in check
                    else:
                        # moves general
                        moves[0] += 1  # increases moves by 1
                        return True
                elif isinstance(piece, Advisor):  # if piece object is an Advisor
                    if self.advisor_moves(self._player_turn, current_x, current_y, target_x, target_y,[piece]) == False:
                        # if move is not legal
                        return False
                    # need to check if king is in check
                    else:
                        # moves advisor
                        moves[0] += 1  # increases moves by 1
                        return True
                elif isinstance(piece, Horse):  # if piece object is an Horse
                    if self.horse_moves(self._player_turn, current_x, current_y, target_x, target_y,[piece]) == False:
                        # if the move is not legal
                        return False
                    # need to check if king is in check
                    else:
                        # moves horse
                        moves[0] += 1  # increases moves by 1
                        return True
                elif isinstance(piece, Chariot):  # if piece object is an Chariot
                    # need to check if king is in check
                    if self.chariot_moves(self._player_turn, current_x, current_y, target_x, target_y,[piece]) == False:
                        # if the move is not legal
                        return False
                    else:
                        # moves chariot
                        moves[0] += 1  # increases moves by 1
                        return True
                elif isinstance(piece, Cannon):  # if piece object is an Cannon
                    if self.cannon_moves(self._player_turn, current_x, current_y, target_x, target_y,[piece]) == False:
                        # if move is not legal
                        return False
                    # need to check if king is in check
                    else:
                        # moves cannon
                        moves[0] += 1  # increases moves by 1
                        return True
            else:
                return False




        """A method called make_move that takes two parameters - strings that represent the square moved from and the 
        square moved to.  For example, make_move('b3', 'b10').  If the square being moved from does not contain a 
        piece belonging to the player whose turn it is, or if the indicated move is not legal, or if the game has 
        already been won, then it should just return False.  Otherwise it should make the indicated move, remove any 
        captured piece, update the game state if necessary, update whose turn it is, and return True. """

    def soldier_moves(self, player, current_x, current_y, target_x, target_y, piece):
        """Returns True and updates self._board if soldier move is legal. Otherwise, returns False."""
        if current_x == target_x and current_y == target_y:
            return False
        if player == 'red':
            x_move = target_x - current_x  # how much to move in x direction
            y_move = target_y - current_y  # how much to move in y direction
            if x_move != 1 and x_move != 0 and x_move != -1:  # if soldier is moving over one space in x direction
                return False
            elif y_move != 1 and y_move != 0:  # if soldier is moving illegally in the y direction
                return False
            elif current_y == 3 or current_y == 4:
                if not self._board[current_y +1][current_x]:  # if space is free
                    self._board[current_y][current_x].clear()
                    self._board[current_y +1][current_x] = piece  # moves red soldier
                    piece[0].set_piece(target_x, target_y)  # updates soldier object
                else:
                    if self._board[current_y +1][current_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[current_y +1][current_x].clear()  # captures black piece
                        self._board[current_y +1][current_x] = piece  # moves red soldier
                        piece[0].set_piece(target_x, target_y)  # updates soldier object
            elif current_y == 5 or current_y == 6 or current_y == 7 or current_y == 8:
                if y_move == 0:
                    if x_move == 1:  # if moving right
                        if not self._board[current_y][current_x +1]:  # if space is free
                            self._board[current_y][current_x].clear()
                            self._board[current_y][current_x +1] = piece  # moves red soldier
                            piece[0].set_piece(target_x, target_y)  # updates soldier object
                        else:
                            if self._board[current_y][current_x +1][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[current_y][current_x +1].clear()  # captures black piece
                                self._board[current_y][current_x +1] = piece  # moves red soldier
                                piece[0].set_piece(target_x, target_y)  # updates soldier object
                    elif x_move == -1:  # if moving left
                        if not self._board[current_y][current_x -1]:  # if space is free
                            self._board[current_y][current_x].clear()
                            self._board[current_y][current_x -1] = piece  # moves red soldier
                            piece[0].set_piece(target_x, target_y)  # updates soldier object
                        else:
                            if self._board[current_y][current_x -1][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[current_y][current_x -1].clear()  # captures black piece
                                self._board[current_y][current_x -1] = piece  # moves red soldier
                                piece[0].set_piece(target_x, target_y)  # updates soldier object
                    else:
                        return False
                elif x_move == 0:
                    if y_move != 1:  # if illegal move
                        return False
                    elif not self._board[current_y +1][current_x]:  # if space is free
                        self._board[current_y][current_x].clear()
                        self._board[current_y +1][current_x] = piece  # moves red soldier
                        piece[0].set_piece(target_x, target_y)  # updates soldier object
                    else:
                        if self._board[current_y +1][current_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[current_y +1][current_x].clear()  # captures black piece
                            self._board[current_y +1][current_x] = piece  # moves red soldier
                            piece[0].set_piece(target_x, target_y)  # updates soldier object
            elif current_y == 9:  # if made it to black's last row
                if y_move != 0:  # if illegal move
                    return False
                elif x_move == 1:  # if moving right
                    if not self._board[current_y][current_x + 1]:  # if space if free
                        self._board[current_y][current_x].clear()
                        self._board[current_y][current_x + 1] = piece  # moves red soldier
                        piece[0].set_piece(target_x, target_y)  # updates soldier object
                    else:
                        if self._board[current_y][current_x + 1][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[current_y][current_x + 1].clear()  # captures black piece
                            self._board[current_y][current_x + 1] = piece  # moves red soldier
                            piece[0].set_piece(target_x, target_y)  # updates soldier object
                elif x_move == -1:
                    if not self._board[current_y][current_x - 1]:  # if space if free
                        self._board[current_y][current_x].clear()
                        self._board[current_y][current_x - 1] = piece  # moves red soldier
                        piece[0].set_piece(target_x, target_y)  # updates soldier object
                    else:
                        if self._board[current_y][current_x - 1][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[current_y][current_x - 1].clear()  # captures black piece
                            self._board[current_y][current_x - 1] = piece  # moves red soldier
                            piece[0].set_piece(target_x, target_y)  # updates soldier object
            else:
                return False
        if player == 'black':
            x_move = target_x - current_x
            y_move = target_y - current_y
            if x_move != 1 and x_move != 0 and x_move != -1:  # if soldier is moving over one space in x direction
                return False
            elif y_move != -1 and y_move != 0:  # if solder is moving illegally in y direction
                return False
            elif current_y == 5 or current_y == 6:
                if not self._board[current_y -1][current_x]:  # if space is free
                    self._board[current_y][current_x].clear()
                    self._board[current_y -1][current_x] = piece  # moves black soldier
                    piece[0].set_piece(target_x, target_y)  # updates soldier object
                else:
                    if self._board[current_y -1][current_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[current_y -1][current_x].clear()  # captures red piece
                        self._board[current_y -1][current_x] = piece  # moves black soldier
                        piece[0].set_piece(target_x, target_y)  # updates piece object
            elif current_y == 1 or current_y == 2 or current_y == 3 or current_y == 4:
                if y_move == 0:
                    if x_move == 1:  # if moving right
                        if not self._board[current_y][current_x +1]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[current_y][current_x +1] = piece  # moves black soldier
                            piece[0].set_piece(target_x, target_y)  # updates piece object
                        else:
                            if self._board[current_y][current_x +1][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[current_y][current_x +1].clear()  # captures red piece
                                self._board[current_y][current_x +1] = piece  # moves black soldier
                                piece[0].set_piece(target_x, target_y)  # updates piece object
                    elif x_move == -1:
                        if not self._board[current_y][current_x -1]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[current_y][current_x -1] = piece  # moves black soldier
                            piece[0].set_piece(target_x, target_y)  # updates soldier object
                        else:
                            if self._board[current_y][current_x -1][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[current_y][current_x -1].clear()  # captures red piece
                                self._board[current_y][current_x -1] = piece  # moves black soldier
                                piece[0].set_piece(target_x, target_y)  # updates soldier object
                    else:
                        return False
                elif x_move == 0:
                    if y_move != -1:  # if moving illegally in y direction
                        return False
                    elif not self._board[current_y -1][current_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[current_y -1][current_x] = piece  # moves black soldier
                        piece[0].set_piece(target_x, target_y)  # updates soldier object
                    else:
                        if self._board[current_y -1][current_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[current_y -1][current_x].clear()  # captures red piece
                            self._board[current_y -1][current_x] = piece  # moves black soldier
                            piece[0].set_piece(target_x, target_y)  # updates soldier object
            elif current_y == 0:  # if made it to red's first row
                if y_move != 0:  # if moving illegally in the y direction
                    return False
                elif x_move == 1:  # if moving right
                    if not self._board[current_y][current_x + 1]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[current_y][current_x + 1] = piece  # moves black soldier
                        piece[0].set_piece(target_x, target_y)  # updates soldier object
                    else:
                        if self._board[current_y][current_x + 1][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[current_y][current_x + 1].clear()  # captures red piece
                            self._board[current_y][current_x + 1] = piece  # moves black soldier
                            piece[0].set_piece(target_x, target_y)  # updates soldier object
                elif x_move == -1:
                    if not self._board[current_y][current_x - 1]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[current_y][current_x - 1] = piece  # moves black soldier
                        piece[0].set_piece(target_x, target_y)  # updates soldier object
                    else:
                        if self._board[current_y][current_x - 1][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[current_y][current_x - 1].clear()  # captures red piece
                            self._board[current_y][current_x - 1] = piece  # moves black soldier
                            piece[0].set_piece(target_x, target_y)  # updates soldier object
            else:
                return False

    def elephant_moves(self, player, current_x, current_y, target_x, target_y, piece):
        """Returns True and updates self._board if elephant move is legal. Otherwise, returns False."""
        if current_x == target_x and current_y == target_y:
            return False
        if player == "red":
            move_x = current_x - target_x
            move_y = current_y - target_y
            if current_x != 0 and current_x != 2 and current_x != 4 and current_x != 6 and current_x != 8:
                return False
            elif current_y != 0 and current_y != 2 and current_y != 4:
                return False
            elif target_x != 0 and target_x != 2 and target_x != 4 and target_x != 6 and target_x != 8:
                return False
            elif target_y != 0 and target_y != 2 and target_y != 4:
                return False
            elif current_y == 0 and (move_x == 2 or move_x == -2) and move_y == -2:
                if not self._board[target_y][target_x]:  # if space is empty
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x] = piece  # moves red elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
                elif self._board[target_y][target_x][0].get_player() == player:
                    # if space is occupied by own piece already
                    return False
                else:
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x].clear()  # captures black piece
                    self._board[target_y][target_x] = piece  # moves red elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
            elif current_y == 2 and (move_x == 2 or move_x == -2) and (move_y == 2 or move_y == -2):
                if not self._board[target_y][target_x]:  # if space is empty
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x] = piece  # moves red elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
                elif self._board[target_y][target_x][0].get_player() == player:
                    # if space is occupied by own piece already
                    return False
                else:
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x].clear()  # captures black piece
                    self._board[target_y][target_x] = piece  # moves red elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
            elif current_y == 4 and (move_x == 2 or move_x == -2) and move_y == 2:
                if not self._board[target_y][target_x]:  # if space is empty
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x] = piece  # moves red elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
                elif self._board[target_y][target_x][0].get_player() == player:
                    # if space is occupied by own piece already
                    return False
                else:
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x].clear()  # captures black piece
                    self._board[target_y][target_x] = piece  # moves red elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
            else:
                return False
        if player == "black":
            move_x = current_x - target_x
            move_y = target_y - current_y
            if current_x != 0 and current_x != 2 and current_x != 4 and current_x != 6 and current_x != 8:
                return False
            elif current_y != 9 and current_y != 7 and current_y != 5:
                return False
            elif target_x != 0 and target_x != 2 and target_x != 4 and target_x != 6 and target_x != 8:
                return False
            elif target_y != 9 and target_y != 7 and target_y != 5:
                return False
            elif current_y == 9 and (move_x == 2 or move_x == -2) and move_y == -2:
                if not self._board[target_y][target_x]:  # if space is empty
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x] = piece  # moves black elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
                elif self._board[target_y][target_x][0].get_player() == player:
                    # if space is occupied by own piece already
                    return False
                else:
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x].clear()  # captures red piece
                    self._board[target_y][target_x] = piece  # moves black elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
            elif current_y == 7 and (move_x == 2 or move_x == -2) and (move_y == 2 or move_y == -2):
                if not self._board[target_y][target_x]:  # if space is empty
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x] = piece  # moves black elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
                elif self._board[target_y][target_x][0].get_player() == player:
                    # if space is occupied by own piece already
                    return False
                else:
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x].clear()  # captures red piece
                    self._board[target_y][target_x] = piece  # moves black elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
            elif current_y == 5 and (move_x == 2 or move_x == -2) and move_y == 2:
                if not self._board[target_y][target_x]:  # if space is empty
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x] = piece  # moves black elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
                elif self._board[target_y][target_x][0].get_player() == player:
                    # if space is occupied by own piece already
                    return False
                else:
                    self._board[current_y][current_x].clear()
                    self._board[target_y][target_x].clear()  # captures red piece
                    self._board[target_y][target_x] = piece  # moves black elephant
                    piece[0].set_piece(target_x, target_y)  # updates elephant object
            else:
                return False

    def general_moves(self, player, current_x, current_y, target_x, target_y, piece):
        """Returns True and updates self._board if general move is legal. Otherwise, returns False."""
        if current_x == target_x and current_y == target_y:
            return False
        if target_x != 3 and target_x != 4 and target_x != 5:
            return False
        if player == 'red':
            move_x = target_x - current_x
            move_y = target_y - current_y
            if move_x != 0 and move_y != 0:
                return False
            if current_y == 0:
                if move_x != 0 and move_x != 1 and move_x != -1 or move_y != 1 and move_y != 0:
                    return False
                elif move_y == 0 and move_x != 1 and move_x != -1:
                    return False
                elif move_y == 1 and move_x != 0:
                    return False
                else:
                    if not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves red general
                        piece[0].set_piece(target_x, target_y)  # updates general object
                        self.set_red_gen(target_x, target_y)
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures black piece
                        self._board[target_y][target_x] = piece  # moves red general
                        piece[0].set_piece(target_x, target_y)  # update general object
                        self.set_red_gen(target_x, target_y)
            if current_y == 1:
                if current_x == 4:
                    if move_x != 1 and move_x != -1 and move_x != 0:
                        return False
                    if move_x == 0 and move_y != 1 and move_y != -1:
                        return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # updates general object
                            self.set_red_gen(target_x, target_y)
                        elif self._board[target_y][target_x][0].get_player() == player:
                             # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # update general object
                            self.set_red_gen(target_x, target_y)
                elif current_x == 3:
                    if move_x != 0 and move_x != 1:
                        return False
                    if move_x == 0 and move_y != 1 and move_y != -1:
                        return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # updates general object
                            self.set_red_gen(target_x, target_y)
                        elif self._board[target_y][target_x][0].get_player() == player:
                             # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # update general object
                            self.set_red_gen(target_x, target_y)
                elif current_x == 5:
                    if move_x != 0 and move_x != -1:
                        return False
                    if move_x == 0 and move_y != 1 and move_y != -1:
                        return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # updates general object
                            self.set_red_gen(target_x, target_y)
                        elif self._board[target_y][target_x][0].get_player() == player:
                             # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # update general object
                            self.set_red_gen(target_x, target_y)
            if current_y == 2:
                if current_x == 4:
                    if move_x != 1 and move_x != -1 and move_x != 0:
                        return False
                    if move_x == 0 and move_y != -1:
                        return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # updates general object
                            self.set_red_gen(target_x, target_y)
                        elif self._board[target_y][target_x][0].get_player() == player:
                             # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # update general object
                            self.set_red_gen(target_x, target_y)
                elif current_x == 3:
                    if move_x != 0 and move_x != 1:
                        return False
                    if move_x == 0 and move_y != -1:
                        return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # updates general object
                            self.set_red_gen(target_x, target_y)
                        elif self._board[target_y][target_x][0].get_player() == player:
                             # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # update general object
                            self.set_red_gen(target_x, target_y)
                elif current_x == 5:
                    if move_x != 0 and move_x != -1:
                        return False
                    if move_x == 0 and move_y != -1:
                        return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # updates general object
                            self.set_red_gen(target_x, target_y)
                        elif self._board[target_y][target_x][0].get_player() == player:
                             # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red general
                            piece[0].set_piece(target_x, target_y)  # update general object
                            self.set_red_gen(target_x, target_y)

        if player == 'black':
                move_x = target_x - current_x
                move_y = current_y - target_y
                if move_x != 0 and move_y != 0:
                    return False
                if current_y == 9:
                    if move_x != 0 and move_x != 1 and move_x != -1 or move_y != 1 and move_y != 0:
                        return False
                    elif move_y == 0 and move_x != 1 and move_x != -1:
                        return False
                    elif move_y == 1 and move_x != 0:
                        return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black general
                            piece[0].set_piece(target_x, target_y)  # updates general object
                            self.set_black_gen(target_x, target_y)
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures red piece
                            self._board[target_y][target_x] = piece  # moves black general
                            piece[0].set_piece(target_x, target_y)  # update general object
                            self.set_black_gen(target_x, target_y)
                if current_y == 8:
                    if current_x == 4:
                        if move_x != 1 and move_x != -1 and move_x != 0:
                            return False
                        if move_x == 0 and move_y != 1 and move_y != -1:
                            return False
                        else:
                            if not self._board[target_y][target_x]:  # if space is empty
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # updates general object
                                self.set_black_gen(target_x, target_y)
                            elif self._board[target_y][target_x][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # update general object
                                self.set_black_gen(target_x, target_y)
                    elif current_x == 3:
                        if move_x != 0 and move_x != 1:
                            return False
                        if move_x == 0 and move_y != 1 and move_y != -1:
                            return False
                        else:
                            if not self._board[target_y][target_x]:  # if space is empty
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # updates general object
                                self.set_black_gen(target_x, target_y)
                            elif self._board[target_y][target_x][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # update general object
                                self.set_black_gen(target_x, target_y)
                    elif current_x == 5:
                        if move_x != 0 and move_x != -1:
                            return False
                        if move_x == 0 and move_y != 1 and move_y != -1:
                            return False
                        else:
                            if not self._board[target_y][target_x]:  # if space is empty
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # updates general object
                                self.set_black_gen(target_x, target_y)
                            elif self._board[target_y][target_x][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # update general object
                                self.set_black_gen(target_x, target_y)
                if current_y == 7:
                    if current_x == 4:
                        if move_x != 1 and move_x != -1 and move_x != 0:
                            return False
                        if move_x == 0 and move_y != -1:
                            return False
                        else:
                            if not self._board[target_y][target_x]:  # if space is empty
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # updates general object
                                self.set_black_gen(target_x, target_y)
                            elif self._board[target_y][target_x][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # update general object
                                self.set_black_gen(target_x, target_y)
                    elif current_x == 3:
                        if move_x != 0 and move_x != 1:
                            return False
                        if move_x == 0 and move_y != -1:
                            return False
                        else:
                            if not self._board[target_y][target_x]:  # if space is empty
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # updates general object
                                self.set_black_gen(target_x, target_y)
                            elif self._board[target_y][target_x][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # update general object
                                self.set_black_gen(target_x, target_y)
                    elif current_x == 5:
                        if move_x != 0 and move_x != -1:
                            return False
                        if move_x == 0 and move_y != -1:
                            return False
                        else:
                            if not self._board[target_y][target_x]:  # if space is empty
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # updates general object
                                self.set_black_gen(target_x, target_y)
                            elif self._board[target_y][target_x][0].get_player() == player:
                                # if space is occupied by own piece already
                                return False
                            else:
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black general
                                piece[0].set_piece(target_x, target_y)  # update general object
                            self.set_black_gen(target_x, target_y)


    def advisor_moves(self, player, current_x, current_y, target_x, target_y, piece):
        """Returns True and updates self._board if advisor move is legal. Otherwise, returns False."""
        if current_x == target_x and current_y == target_y:
            return False
        if target_x != 3 and target_x != 4 and target_x != 5:
            return False
        if player == 'red':
            move_x = target_x - current_x
            move_y = target_y - current_y
            if current_y == 0:
                if target_y != 1:
                    return False
                elif target_x != 4:
                    return False
                else:
                    if not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves red advisor
                        piece[0].set_piece(target_x, target_y)  # updates advisor object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures black piece
                        self._board[target_y][target_x] = piece  # moves red advisor
                        piece[0].set_piece(target_x, target_y)  # update advisor object
            if current_y == 1:
                if target_y != 0 and target_y != 2:
                    return False
                elif target_x != 3 and target_x != 5:
                    return False
                else:
                    if not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves red advisor
                        piece[0].set_piece(target_x, target_y)  # updates advisor object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures black piece
                        self._board[target_y][target_x] = piece  # moves red advisor
                        piece[0].set_piece(target_x, target_y)  # update advisor object
            if current_y == 2:
                if target_y != 1 or target_x != 4:
                    return False
                else:
                    if not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves red advisor
                        piece[0].set_piece(target_x, target_y)  # updates advisor object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures black piece
                        self._board[target_y][target_x] = piece  # moves red advisor
                        piece[0].set_piece(target_x, target_y)  # update advisor object
        if player == 'black':
            move_x = target_x - current_x
            move_y = target_y - current_y
            if current_y == 9:
                if target_y != 8:
                    return False
                elif target_x != 4:
                    return False
                else:
                    if not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves black advisor
                        piece[0].set_piece(target_x, target_y)  # updates advisor object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures red piece
                        self._board[target_y][target_x] = piece  # moves black advisor
                        piece[0].set_piece(target_x, target_y)  # update advisor object
            if current_y == 8:
                if target_y != 9 and target_y != 7:
                    return False
                elif target_x != 3 and target_x != 5:
                    return False
                else:
                    if not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves black advisor
                        piece[0].set_piece(target_x, target_y)  # updates advisor object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures red piece
                        self._board[target_y][target_x] = piece  # moves black advisor
                        piece[0].set_piece(target_x, target_y)  # update advisor object
            if current_y == 7:
                if target_y != 8 or target_x != 4:
                    return False
                else:
                    if not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves black advisor
                        piece[0].set_piece(target_x, target_y)  # updates advisor object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures red piece
                        self._board[target_y][target_x] = piece  # moves black advisor
                        piece[0].set_piece(target_x, target_y)  # update advisor object


    def horse_moves(self, player, current_x, current_y, target_x, target_y, piece):
        """Returns True and updates self._board if horse move is legal. Otherwise, returns False."""
        if current_x == target_x and current_y == target_y:
            return False
        if player == 'red':
            move_x = target_x - current_x
            move_y = target_y - current_y
            if move_x == 2:
                if move_y != 1 and move_y != -1:
                    return False
                else:
                    if self._board[current_y][target_x - 1]:  # if there is a piece blocking the horse
                        return False
                    elif not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves red horse
                        piece[0].set_piece(target_x, target_y)  # updates horse object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures black piece
                        self._board[target_y][target_x] = piece  # moves red horse
                        piece[0].set_piece(target_x, target_y)  # update horse object
            elif move_x == -2:
                if move_y != 1 and move_y != -1:
                    return False
                else:
                    if self._board[current_y][target_x + 1]:  # if there is a piece blocking the horse
                        return False
                    elif not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves red horse
                        piece[0].set_piece(target_x, target_y)  # updates horse object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures black piece
                        self._board[target_y][target_x] = piece  # moves red horse
                        piece[0].set_piece(target_x, target_y)  # update horse object
            elif move_y == 2:
                if move_x != 1 and move_x != -1:
                    return False
                else:
                    if self._board[target_y-1][current_x]:  # if there is a piece blocking the horse
                        return False
                    elif not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves red horse
                        piece[0].set_piece(target_x, target_y)  # updates horse object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures black piece
                        self._board[target_y][target_x] = piece  # moves red horse
                        piece[0].set_piece(target_x, target_y)  # update horse object
            elif move_y == -2:
                if move_x != 1 and move_x != -1:
                    return False
                else:
                    if self._board[target_y+1][current_x]:  # if there is a piece blocking the horse
                        return False
                    elif not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves red horse
                        piece[0].set_piece(target_x, target_y)  # updates horse object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures black piece
                        self._board[target_y][target_x] = piece  # moves red horse
                        piece[0].set_piece(target_x, target_y)  # update horse object
        if player == 'black':
            move_x = target_x - current_x
            move_y = current_y - target_y
            if move_x == 2:
                if move_y != 1 and move_y != -1:
                    return False
                else:
                    if self._board[current_y][target_x - 1]:  # if there is a piece blocking the horse
                        return False
                    elif not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves black horse
                        piece[0].set_piece(target_x, target_y)  # updates horse object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures red piece
                        self._board[target_y][target_x] = piece  # moves black horse
                        piece[0].set_piece(target_x, target_y)  # update horse object
            elif move_x == -2:
                if move_y != 1 and move_y != -1:
                    return False
                else:
                    if self._board[current_y][target_x + 1]:  # if there is a piece blocking the horse
                        return False
                    elif not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves black horse
                        piece[0].set_piece(target_x, target_y)  # updates horse object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures red piece
                        self._board[target_y][target_x] = piece  # moves black horse
                        piece[0].set_piece(target_x, target_y)  # update horse object
            elif move_y == 2:
                if move_x != 1 and move_x != -1:
                    return False
                else:
                    if self._board[target_y+1][current_x]:  # if there is a piece blocking the horse
                        return False
                    elif not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves black horse
                        piece[0].set_piece(target_x, target_y)  # updates horse object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures red piece
                        self._board[target_y][target_x] = piece  # moves black horse
                        piece[0].set_piece(target_x, target_y)  # update horse object
            elif move_y == -2:
                if move_x != 1 and move_x != -1:
                    return False
                else:
                    if self._board[target_y-1][current_x]:  # if there is a piece blocking the horse
                        return False
                    elif not self._board[target_y][target_x]:  # if space is empty
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x] = piece  # moves black horse
                        piece[0].set_piece(target_x, target_y)  # updates horse object
                    elif self._board[target_y][target_x][0].get_player() == player:
                        # if space is occupied by own piece already
                        return False
                    else:
                        self._board[current_y][current_x].clear()
                        self._board[target_y][target_x].clear()  # captures red piece
                        self._board[target_y][target_x] = piece  # moves black horse
                        piece[0].set_piece(target_x, target_y)  # update horse object


    def chariot_moves(self, player, current_x, current_y, target_x, target_y, piece):
        """Returns True and updates self._board if chariot move is legal. Otherwise, returns False."""
        if current_x == target_x and current_y == target_y:
            return False
        if player == 'red':
            move_x = target_x - current_x
            move_y = target_y - current_y
            if move_y != 0 and move_x == 0:
                if move_y > 0:
                    val_lst = []
                    if move_y == 1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red chariot
                            piece[0].set_piece(target_x, target_y)  # updates chariot object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red chariot
                            piece[0].set_piece(target_x, target_y)  # update chariot object
                            return
                    else:
                        for row in range(current_y+1, target_y):
                            val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                        for val in val_lst:
                            if self._board[val][target_x]:
                                # if there is a piece in between initial and designated spot
                                return False
                            else:
                                if not self._board[target_y][target_x]:  # if space is empty
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x] = piece  # moves red chariot
                                    piece[0].set_piece(target_x, target_y)  # updates chariot object
                                    return
                                elif self._board[target_y][target_x][0].get_player() == player:
                                    # if space is occupied by own piece already
                                    return False
                                else:
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x].clear()  # captures black piece
                                    self._board[target_y][target_x] = piece  # moves red chariot
                                    piece[0].set_piece(target_x, target_y)  # update chariot object
                                    return
                if move_y < 0:
                    val_lst = []
                    if move_y == -1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red chariot
                            piece[0].set_piece(target_x, target_y)  # updates chariot object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red chariot
                            piece[0].set_piece(target_x, target_y)  # update chariot object
                            return
                    else:
                        for row in range(target_y+1, current_y):
                            val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                        for val in val_lst:
                            if self._board[val][target_x]:
                                # if there is a piece in between initial and designated spot
                                return False
                            else:
                                if not self._board[target_y][target_x]:  # if space is empty
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x] = piece  # moves red chariot
                                    piece[0].set_piece(target_x, target_y)  # updates chariot object
                                    return
                                elif self._board[target_y][target_x][0].get_player() == player:
                                    # if space is occupied by own piece already
                                    return False
                                else:
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x].clear()  # captures black piece
                                    self._board[target_y][target_x] = piece  # moves red chariot
                                    piece[0].set_piece(target_x, target_y)  # update chariot object
                                    return
            if move_y == 0 and move_x != 0:
                if move_x > 0:
                    val_lst = []
                    if move_x == 1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red chariot
                            piece[0].set_piece(target_x, target_y)  # updates chariot object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red chariot
                            piece[0].set_piece(target_x, target_y)  # update chariot object
                            return
                    else:
                        for col in range(current_x+1, target_x):
                            val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                        for val in val_lst:
                            if self._board[target_y][val]:
                                # if there is a piece in between initial and designated spot
                                return False
                            else:
                                if not self._board[target_y][target_x]:  # if space is empty
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x] = piece  # moves red chariot
                                    piece[0].set_piece(target_x, target_y)  # updates chariot object
                                    return
                                elif self._board[target_y][target_x][0].get_player() == player:
                                    # if space is occupied by own piece already
                                    return False
                                else:
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x].clear()  # captures black piece
                                    self._board[target_y][target_x] = piece  # moves red chariot
                                    piece[0].set_piece(target_x, target_y)  # update chariot object
                                    return
                if move_x < 0:
                    val_lst = []
                    if move_x == -1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red chariot
                            piece[0].set_piece(target_x, target_y)  # updates chariot object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures black piece
                            self._board[target_y][target_x] = piece  # moves red chariot
                            piece[0].set_piece(target_x, target_y)  # update chariot object
                            return
                    else:
                        for col in range(target_x+1, current_x):
                            val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                        for val in val_lst:
                            if self._board[target_y][val]:
                                # if there is a piece in between initial and designated spot
                                return False
                            else:
                                if not self._board[target_y][target_x]:  # if space is empty
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x] = piece  # moves red chariot
                                    piece[0].set_piece(target_x, target_y)  # updates chariot object
                                    return
                                elif self._board[target_y][target_x][0].get_player() == player:
                                    # if space is occupied by own piece already
                                    return False
                                else:
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x].clear()  # captures black piece
                                    self._board[target_y][target_x] = piece  # moves red chariot
                                    piece[0].set_piece(target_x, target_y)  # update chariot object
                                    return
            if move_x != 0 and move_y != 0:
                return False
        if player == 'black':
            move_x = target_x - current_x
            move_y = current_y - target_y
            if move_y != 0 and move_x == 0:
                if move_y > 0:
                    val_lst = []
                    if move_y == 1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black chariot
                            piece[0].set_piece(target_x, target_y)  # updates chariot object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures red piece
                            self._board[target_y][target_x] = piece  # moves black chariot
                            piece[0].set_piece(target_x, target_y)  # update chariot object
                            return
                    else:
                        for row in range(target_y+1, current_y):
                            val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                        for val in val_lst:
                            if self._board[val][target_x]:
                                # if there is a piece in between initial and designated spot
                                return False
                            else:
                                if not self._board[target_y][target_x]:  # if space is empty
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x] = piece  # moves black chariot
                                    piece[0].set_piece(target_x, target_y)  # updates chariot object
                                    return
                                elif self._board[target_y][target_x][0].get_player() == player:
                                    # if space is occupied by own piece already
                                    return False
                                else:
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x].clear()  # captures red piece
                                    self._board[target_y][target_x] = piece  # moves black chariot
                                    piece[0].set_piece(target_x, target_y)  # update chariot object
                                    return
                if move_y < 0:
                    val_lst = []
                    if move_y == -1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black chariot
                            piece[0].set_piece(target_x, target_y)  # updates chariot object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures red piece
                            self._board[target_y][target_x] = piece  # moves black chariot
                            piece[0].set_piece(target_x, target_y)  # update chariot object
                            return
                    else:
                        for row in range(current_y+1, target_y):
                            val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                        for val in val_lst:
                            if self._board[val][target_x]:
                                # if there is a piece in between initial and designated spot
                                return False
                            else:
                                if not self._board[target_y][target_x]:  # if space is empty
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x] = piece  # moves black chariot
                                    piece[0].set_piece(target_x, target_y)  # updates chariot object
                                    return
                                elif self._board[target_y][target_x][0].get_player() == player:
                                    # if space is occupied by own piece already
                                    return False
                                else:
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x].clear()  # captures red piece
                                    self._board[target_y][target_x] = piece  # moves black chariot
                                    piece[0].set_piece(target_x, target_y)  # update chariot object
                                    return
            if move_y == 0 and move_x != 0:
                if move_x > 0:
                    val_lst = []
                    if move_x == 1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black chariot
                            piece[0].set_piece(target_x, target_y)  # updates chariot object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures red piece
                            self._board[target_y][target_x] = piece  # moves black chariot
                            piece[0].set_piece(target_x, target_y)  # update chariot object
                            return
                    else:
                        for col in range(current_x+1, target_x):
                            val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                        for val in val_lst:
                            if self._board[target_y][val]:
                                # if there is a piece in between initial and designated spot
                                return False
                            else:
                                if not self._board[target_y][target_x]:  # if space is empty
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x] = piece  # moves black chariot
                                    piece[0].set_piece(target_x, target_y)  # updates chariot object
                                    return
                                elif self._board[target_y][target_x][0].get_player() == player:
                                    # if space is occupied by own piece already
                                    return False
                                else:
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x].clear()  # captures red piece
                                    self._board[target_y][target_x] = piece  # moves black chariot
                                    piece[0].set_piece(target_x, target_y)  # update chariot object
                                    return
                if move_x < 0:
                    val_lst = []
                    if move_x == -1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves block chariot
                            piece[0].set_piece(target_x, target_y)  # updates chariot object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x].clear()  # captures red piece
                            self._board[target_y][target_x] = piece  # moves black chariot
                            piece[0].set_piece(target_x, target_y)  # update chariot object
                            return
                    else:
                        for col in range(target_x+1, current_x):
                            val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                        for val in val_lst:
                            if self._board[target_y][val]:
                                # if there is a piece in between initial and designated spot
                                return False
                            else:
                                if not self._board[target_y][target_x]:  # if space is empty
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x] = piece  # moves black chariot
                                    piece[0].set_piece(target_x, target_y)  # updates chariot object
                                    return
                                elif self._board[target_y][target_x][0].get_player() == player:
                                    # if space is occupied by own piece already
                                    return False
                                else:
                                    self._board[current_y][current_x].clear()
                                    self._board[target_y][target_x].clear()  # captures red piece
                                    self._board[target_y][target_x] = piece  # moves black chariot
                                    piece[0].set_piece(target_x, target_y)  # update chariot object
                                    return
            if move_x != 0 and move_y != 0:
                return False

    def cannon_moves(self,player, current_x, current_y, target_x, target_y, piece):
        if player == 'red':
            move_x = target_x - current_x
            move_y = target_y - current_y
            if move_y != 0 and move_x == 0:
                if move_y > 0:
                    val_lst = []
                    if move_y == 1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        if self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            for row in range(current_y + 1, target_y):
                                val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[val][target_x]:
                                    # if there is a piece in between initial and designated spot
                                    return False
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            count = 0
                            for row in range(current_y + 1, target_y):
                                val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[val][target_x]:
                                    # if there is a piece in between initial and designated spot
                                    count += 1
                            if count == 1:
                                # if legal capture move
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures black piece
                                self._board[target_y][target_x] = piece  # moves red cannon
                                piece[0].set_piece(target_x, target_y)  # update cannon object
                            else:
                                return False
                if move_y < 0:
                    val_lst = []
                    if move_y == -1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            for row in range(target_y + 1, current_y):
                                val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[val][target_x]:
                                    # if there is a piece in between initial and designated spot
                                    return False
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            count = 0
                            for row in range(target_y + 1, current_y):
                                val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[val][target_x]:
                                    # if there is a piece in between initial and designated spot
                                    count += 1
                            if count == 1:
                                # if legal capture move
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures black piece
                                self._board[target_y][target_x] = piece  # moves red cannon
                                piece[0].set_piece(target_x, target_y)  # update cannon object
                                return
                            else:
                                return False
            if move_y == 0 and move_x != 0:
                if move_x > 0:
                    val_lst = []
                    if move_x == 1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            for col in range(current_x + 1, target_x):
                                val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[target_y][val]:
                                    # if there is a piece in between initial and designated spot
                                    return False
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            count = 0
                            for col in range(current_x + 1, target_x):
                                val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[target_y][val]:
                                    # if there is a piece in between initial and designated spot
                                    count += 1
                            if count == 1:
                                # if legal capture move
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures black piece
                                self._board[target_y][target_x] = piece  # moves red cannon
                                piece[0].set_piece(target_x, target_y)  # update cannon object
                                return
                            else:
                                return False
                if move_x < 0:
                    val_lst = []
                    if move_x == -1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            for col in range(target_x + 1, current_x):
                                val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[target_y][val]:
                                    # if there is a piece in between initial and designated spot
                                    return False
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves red cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            count = 0
                            for row in range(target_x + 1, current_x):
                                val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[target_y][val]:
                                    # if there is a piece in between initial and designated spot
                                    count += 1
                            if count == 1:
                                # if capture move is legal
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures black piece
                                self._board[target_y][target_x] = piece  # moves red cannon
                                piece[0].set_piece(target_x, target_y)  # update cannon object
                                return
                            else:
                                return False
            if move_x != 0 and move_y != 0:
                return False
        if player == 'black':
            move_x = target_x - current_x
            move_y = current_y - target_y
            if move_y != 0 and move_x == 0:
                if move_y > 0:
                    val_lst = []
                    if move_y == 1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            for row in range(target_y + 1, current_y):
                                val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[val][target_x]:
                                    # if there is a piece in between initial and designated spot
                                    return False
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            count = 0
                            for row in range(target_y + 1, current_y):
                                val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[val][target_x]:
                                    # if there is a piece in between initial and designated spot
                                    count += 1
                            if count == 1:
                                # if capture move is legal
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black cannon
                                piece[0].set_piece(target_x, target_y)  # update cannon object
                                return
                            else:
                                return False
                if move_y < 0:
                    val_lst = []
                    if move_y == -1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            for row in range(current_y + 1, target_y):
                                val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[val][target_x]:
                                    # if there is a piece in between initial and designated spot
                                    return False
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            count = 0
                            for row in range(current_y + 1, target_y):
                                val_lst.append(row)  # adds rows between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[val][target_x]:
                                    # if there is a piece in between initial and designated spot
                                    count += 1
                            if count == 1:
                                # if capture move is legal
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black cannon
                                piece[0].set_piece(target_x, target_y)  # update cannon object
                                return
                            else:
                                return False
            if move_y == 0 and move_x != 0:
                if move_x > 0:
                    val_lst = []
                    if move_x == 1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            for col in range(current_x + 1, target_x):
                                val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[target_y][val]:
                                    # if there is a piece in between initial and designated spot
                                    return False
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            count = 0
                            for col in range(current_x + 1, target_x):
                                val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[target_y][val]:
                                    # if there is a piece in between initial and designated spot
                                    count += 1
                            if count == 1:
                                # if capture move is legal
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black cannon
                                piece[0].set_piece(target_x, target_y)  # update cannon object
                                return
                            else:
                                return False
                if move_x < 0:
                    val_lst = []
                    if move_x == -1:
                        if not self._board[target_y][target_x]:  # if space is empty
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            return False
                    else:
                        if not self._board[target_y][target_x]:  # if space is empty
                            for col in range(target_x + 1, current_x):
                                val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[target_y][val]:
                                    # if there is a piece in between initial and designated spot
                                    return False
                            self._board[current_y][current_x].clear()
                            self._board[target_y][target_x] = piece  # moves black cannon
                            piece[0].set_piece(target_x, target_y)  # updates cannon object
                            return
                        elif self._board[target_y][target_x][0].get_player() == player:
                            # if space is occupied by own piece already
                            return False
                        else:
                            count = 0
                            for col in range(target_x + 1, current_x):
                                val_lst.append(col)  # adds columns between initial spot and designated spot to a list
                            for val in val_lst:
                                if self._board[target_y][val]:
                                    # if there is a piece in between initial and designated spot
                                    count += 1
                            if count == 1:
                                # if capture move is legal
                                self._board[current_y][current_x].clear()
                                self._board[target_y][target_x].clear()  # captures red piece
                                self._board[target_y][target_x] = piece  # moves black cannon
                                piece[0].set_piece(target_x, target_y)  # update cannon object
                                return
                            else:
                                return False
            if move_x != 0 and move_y != 0:
                return False


class Soldier:
    """Represents a soldier piece"""

    def __init__(self, player, current_x, current_y, piece_id):
        self._current_x = current_x
        self._current_y = current_y
        self._player = player
        self._piece_id = piece_id

    def set_piece(self, current_x, current_y):
        """Updates current_x and current_y"""
        self._current_x = current_x
        self._current_y = current_y

    def get_player(self):
        """Returns player that piece belongs to"""
        return self._player

    def fly_general(self, board, current_x, current_y, target_x):
        """Returns False if moving soldier would cause the flying general rule"""
        if current_x == 3 or current_x == 4 or current_x == 5:
            if target_x != current_x:
                val_lst = []
                count = 0
                for col in range(0, current_y):
                    val_lst.append(col)  # adds all columns between piece and end of board to a list
                val_lst.reverse()
                for val in val_lst:
                    if board[val][current_x]:  # if there is a piece there
                        count += 1
                        piece = board[val][current_x]
                        if isinstance(piece[0], General):  # if piece is a general
                            if count == 1:  # if there is only the general behind it
                                val_lst_2 = []
                                for col in range(current_y+1, 10):
                                    val_lst_2.append(col)  # adds all columns between piece and end of board to a list
                                for val in val_lst_2:
                                    if board[val][current_x]: # if there is a piece there
                                        count += 1
                                        piece = board[val][current_x]
                                        if isinstance(piece[0], General):  # if piece is a general
                                            if count == 2:  # if soldier is the only piece between both generals
                                                return False

    def check_general(self, gen_x, gen_y):
        """Returns True if soldier move put general in check"""
        if gen_y == self._current_y:
            if gen_x-1 == self._current_x:
                return True
            if gen_x+1 == self._current_x:
                return True
        if gen_x == self._current_x:
            if gen_y-1 == self._current_y:
                return True
            if gen_y+1 == self._current_y:
                return True


class Elelphant:
    """Represents a elephant piece"""

    def __init__(self, player, current_x, current_y, piece_id):
        self._current_x = current_x
        self._current_y = current_y
        self._player = player
        self._piece_id = piece_id

    def set_piece(self, current_x, current_y):
        """Updates current_x and current_y"""
        self._current_x = current_x
        self._current_y = current_y

    def get_player(self):
        """Returns player that piece belongs to"""
        return self._player

    def fly_general(self, board, current_x, current_y, target_x):
        """Returns False if moving Elephant would cause the flying general rule"""
        if current_x == 3 or current_x == 4 or current_x == 5:
            if target_x != current_x:
                val_lst = []
                count = 0
                for col in range(0, current_y):
                    val_lst.append(col)  # adds all columns between piece and end of board to a list
                val_lst.reverse()
                for val in val_lst:
                    if board[val][current_x]:  # if there is a piece there
                        count += 1
                        piece = board[val][current_x]
                        if isinstance(piece[0], General):  # if piece is a general
                            if count == 1:  # if there is only the general behind it
                                val_lst_2 = []
                                for col in range(current_y+1, 10):
                                    val_lst_2.append(col)  # adds all columns between piece and end of board to a list
                                for val in val_lst_2:
                                    if board[val][current_x]: # if there is a piece there
                                        count += 1
                                        piece = board[val][current_x]
                                        if isinstance(piece[0], General):  # if piece is a general
                                            if count == 2:  # if soldier is the only piece between both generals
                                                return False


class Advisor:
    """Represents an advisor piece"""

    def __init__(self, player, current_x, current_y, piece_id):
        self._current_x = current_x
        self._current_y = current_y
        self._player = player
        self._piece_id = piece_id

    def set_piece(self, current_x, current_y):
        """Updates current_x and current_y"""
        self._current_x = current_x
        self._current_y = current_y

    def get_player(self):
        """Returns player that piece belongs to"""
        return self._player

    def fly_general(self, board, current_x, current_y, target_x):
        """Returns False if moving advisor would cause the flying general rule"""
        if current_x == 3 or current_x == 4 or current_x == 5:
            if target_x != current_x:
                val_lst = []
                count = 0
                for col in range(0, current_y):
                    val_lst.append(col)  # adds all columns between piece and end of board to a list
                val_lst.reverse()
                for val in val_lst:
                    if board[val][current_x]:  # if there is a piece there
                        count += 1
                        piece = board[val][current_x]
                        if isinstance(piece[0], General):  # if piece is a general
                            if count == 1:  # if there is only the general behind it
                                val_lst_2 = []
                                for col in range(current_y+1, 10):
                                    val_lst_2.append(col)  # adds all columns between piece and end of board to a list
                                for val in val_lst_2:
                                    if board[val][current_x]: # if there is a piece there
                                        count += 1
                                        piece = board[val][current_x]
                                        if isinstance(piece[0], General):  # if piece is a general
                                            if count == 2:  # if soldier is the only piece between both generals
                                                return False


class Horse:
    """Represents a horse piece"""

    def __init__(self, player, current_x, current_y, piece_id):
        self._current_x = current_x
        self._current_y = current_y
        self._player = player
        self._piece_id = piece_id

    def set_piece(self, current_x, current_y):
        """Updates current_x and current_y"""
        self._current_x = current_x
        self._current_y = current_y

    def get_player(self):
        """Returns player that piece belongs to"""
        return self._player

    def fly_general(self, board, current_x, current_y, target_x):
        """Returns False if moving horse would cause the flying general rule"""
        if current_x == 3 or current_x == 4 or current_x == 5:
            if target_x != current_x:
                val_lst = []
                count = 0
                for col in range(0, current_y):
                    val_lst.append(col)  # adds all columns between piece and end of board to a list
                val_lst.reverse()
                for val in val_lst:
                    if board[val][current_x]:  # if there is a piece there
                        count += 1
                        piece = board[val][current_x]
                        if isinstance(piece[0], General):  # if piece is a general
                            if count == 1:  # if there is only the general behind it
                                val_lst_2 = []
                                for col in range(current_y+1, 10):
                                    val_lst_2.append(col)  # adds all columns between piece and end of board to a list
                                for val in val_lst_2:
                                    if board[val][current_x]: # if there is a piece there
                                        count += 1
                                        piece = board[val][current_x]
                                        if isinstance(piece[0], General):  # if piece is a general
                                            if count == 2:  # if soldier is the only piece between both generals
                                                return False


class Chariot:
    """Represents a chariot piece"""

    def __init__(self, player, current_x, current_y, piece_id):
        self._current_x = current_x
        self._current_y = current_y
        self._player = player
        self._piece_id = piece_id

    def set_piece(self, current_x, current_y):
        """Updates current_x and current_y"""
        self._current_x = current_x
        self._current_y = current_y

    def get_player(self):
        """Returns player that piece belongs to"""
        return self._player

    def fly_general(self, board, current_x, current_y, target_x):
        """Returns False if moving chariot would cause the flying general rule"""
        if current_x == 3 or current_x == 4 or current_x == 5:
            if target_x != current_x:
                val_lst = []
                count = 0
                for col in range(0, current_y):
                    val_lst.append(col)  # adds all columns between piece and end of board to a list
                val_lst.reverse()
                for val in val_lst:
                    if board[val][current_x]:  # if there is a piece there
                        count += 1
                        piece = board[val][current_x]
                        if isinstance(piece[0], General):  # if piece is a general
                            if count == 1:  # if there is only the general behind it
                                val_lst_2 = []
                                for col in range(current_y+1, 10):
                                    val_lst_2.append(col)  # adds all columns between piece and end of board to a list
                                for val in val_lst_2:
                                    if board[val][current_x]: # if there is a piece there
                                        count += 1
                                        piece = board[val][current_x]
                                        if isinstance(piece[0], General):  # if piece is a general
                                            if count == 2:  # if soldier is the only piece between both generals
                                                return False


class Cannon:
    """Represents a cannon piece"""

    def __init__(self, player, current_x, current_y, piece_id):
        self._current_x = current_x
        self._current_y = current_y
        self._player = player
        self._piece_id = piece_id

    def set_piece(self, current_x, current_y):
        """Updates current_x and current_y"""
        self._current_x = current_x
        self._current_y = current_y

    def get_player(self):
        """Returns player that piece belongs to"""
        return self._player

    def fly_general(self, board, current_x, current_y, target_x):
        """Returns False if moving cannon would cause the flying general rule"""
        if current_x == 3 or current_x == 4 or current_x == 5:
            if target_x != current_x:
                val_lst = []
                count = 0
                for col in range(0, current_y):
                    val_lst.append(col)  # adds all columns between piece and end of board to a list
                val_lst.reverse()
                for val in val_lst:
                    if board[val][current_x]:  # if there is a piece there
                        count += 1
                        piece = board[val][current_x]
                        if isinstance(piece[0], General):  # if piece is a general
                            if count == 1:  # if there is only the general behind it
                                val_lst_2 = []
                                for col in range(current_y+1, 10):
                                    val_lst_2.append(col)  # adds all columns between piece and end of board to a list
                                for val in val_lst_2:
                                    if board[val][current_x]: # if there is a piece there
                                        count += 1
                                        piece = board[val][current_x]
                                        if isinstance(piece[0], General):  # if piece is a general
                                            if count == 2:  # if soldier is the only piece between both generals
                                                return False


class General:
    """Represents a general piece"""

    def __init__(self, player, current_x, current_y, piece_id):
        self._current_x = current_x
        self._current_y = current_y
        self._player = player
        self._piece_id = piece_id
        self._status = False

    def set_piece(self, current_x, current_y):
        """Updates current_x and current_y"""
        self._current_x = current_x
        self._current_y = current_y

    def get_player(self):
        """Returns player that piece belongs to"""
        return self._player

    def get_current_x(self):
        """Returns current_x"""
        return self._current_x

    def get_current_y(self):
        """Returns current_y"""
        return self._current_y

    def get_status(self):
        """Returns general status"""
        return self._status

    def set_status(self, status):
        """Sets general status"""
        self._status = status

    def fly_general(self, board, current_x, current_y, target_x):
        """Returns False if moving general would cause the flying general rule"""
        if target_x != current_x:
            val_lst = []
            if self._player == 'red':
                count = 0
                for col in range(current_y + 1, 10):
                    val_lst.append(col)  # adds all columns between piece and end of board to a list
                for val in val_lst:
                    if board[val][target_x]:  # if there is a piece there
                        count += 1
                        piece = board[val][current_x]
                        if isinstance(piece[0], General):  # if piece is a general
                            if count == 1:  # if soldier is the only piece between both generals
                                return False
            if self._player == 'black':
                count = 0
                val_lst_2 = []
                for col in range(0, current_y):
                    val_lst_2.append(col)  # adds all columns between piece and end of board to a list
                for val in val_lst_2:
                    if board[val][target_x]:  # if there is a piece there
                        count += 1
                        piece = board[val][target_x]
                        if isinstance(piece[0], General):  # if piece is a general
                            if count == 1:  # if soldier is the only piece between both generals
                                return False











