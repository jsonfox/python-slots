import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_multipliers = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def generate_board(rows, columns, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    board = []
    for _ in range(columns):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        board.append(column)
        
    return board

def print_board(board):
    for row in range(len(board[0])):
        for i, column in enumerate(board):
            if i != len(board) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def check_winning_lines(board, lines, bet, multipliers):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = board[0][line]
        for column in board:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += bet * multipliers[symbol]
            winning_lines.append(line + 1)
            
    return winnings, winning_lines

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than $0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"How many lines would you like to bet on (1 - {MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.") 
        else:
            print("Please enter a number.")
            
    return lines

def get_bet_amount():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a number between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return bet

def spin(balance):
    lines = get_number_of_lines()
    
    while True: 
        bet = get_bet_amount()
        total_bet = bet * lines
        if total_bet > balance:
            print("Insufficient funds. Please enter a lower bet amount.")
        else:
            balance -= total_bet
            print("Balance: $" + str(balance))
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    board = generate_board(ROWS, COLUMNS, symbol_count)
    print_board(board)
    
    winnings, winning_lines = check_winning_lines(board, lines, bet, symbol_multipliers)
    if winnings > 0:
        balance += winnings
        print(f"You won ${winnings}!")
        print(f"You won on lines:", *winning_lines)
    else:
        print("You did not win this round.")
        
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Balance: ${balance}")
        play = input("Press enter to play (q to quit): ")
        if play.lower() == "q":
            break
        balance += spin(balance)
    
    print(f"Thank you for playing! Your final balance is: ${balance}")
            
main()