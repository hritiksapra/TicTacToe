import random
class GAME:
    def __init__(self):
        self.board = ['-' for x in range(0, 9)]
        self.lastMoves = []
        self.winner = None

    def mark(self, marker, pos):
        self.board[pos] = marker
        self.lastMoves.append(pos)

    def get_free_positions(self):
        moves = []
        for i,v in enumerate(self.board):
            if v=='-':
                moves.append(i)
        return moves

    def revert_last_move(self):
        self.board[self.lastMoves.pop()] = '-'
        self.winner = None

    def is_game_over(self):
        win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8), (2,4,6)]

        for (i,j,k) in win_positions:
            if self.board[i] == self.board[j] == self.board[k] and self.board[i] != '-':
                self.winner = self.board[i]
                return True

        if '-' not in self.board:
            self.winner = '-'
            return True

        return False

    def print_board(self):
        print('   |   |')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
        print('   |   |')

    def play(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        for i in range(9):
            self.print_board()
            if i%2 == 0:
                if self.p1.type == 'H':
                    print("\t\t[Human's Move]")
                else:
                    print("\t\t[Computer's Move]")
                self.p1.move(self)
            else:
                if self.p2.type == 'H':
                    print("\t\t[Human's Move]")
                else:
                    print("\t\t[Computer's Move]")
                self.p2.move(self)

            if self.is_game_over():
                self.print_board()
                if self.winner == '-':
                    print("Tie Game!")
                else:
                    print("\nWinner : %s" %self.winner)
                return

class Human:
    def __init__(self, marker):
        self.marker = marker
        self.type = 'H'

    def move(self, gameinstance):

        while True:
            m = input("Input position:")

            try:
                m =  int(m)
                m = m - 1
            except:
                print("Input Number")

            if m not in gameinstance.get_free_positions():
                print("Inavlid Move")
            else:
                break
        gameinstance.mark(self.marker, m)

class AI:
    def __init__(self, marker):
        self.marker = marker
        self.type = 'C'
        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'

    def move(self, gameinstance):
        move_position, score = self.maximized_move(gameinstance)
        gameinstance.mark(self.marker, move_position)

    def maximized_move(self, gameinstance):
        bestscore = None
        bestMove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.marker, m)

            if gameinstance.is_game_over():
                score = self.get_score(gameinstance)
            else:
                move_position, score = self.minimized_move(gameinstance)

            gameinstance.revert_last_move()

            if bestscore == None or bestscore < score:
                bestscore = score
                bestMove = m

        return bestMove, bestscore

    def minimized_move(self, gameinstance):
        bestscore = None
        bestMove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.opponentmarker, m)

            if gameinstance.is_game_over():
                score = self.get_score(gameinstance)
            else:
                move_position, score = self.maximized_move(gameinstance)

            gameinstance.revert_last_move()

            if bestscore == None or bestscore > score:
                bestscore = score
                bestMove = m

        return bestMove, bestscore

    def get_score(self, gameinstance):
        if gameinstance.is_game_over():
            if gameinstance.winner == self.marker:
                return 1

            elif gameinstance.winner == self.opponentmarker:
                return -1

        return 0

if __name__ == '__main__':
    game=GAME()     
    player1 = Human("X")
    player2 = AI("O")
    players = [player1, player2]
    n = random.randint(0,2)
    if n == 1:    
        game.play(player2, player1)
    else:
        game.play(player1, player2)
















