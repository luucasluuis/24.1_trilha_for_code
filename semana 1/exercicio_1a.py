import random

def bot_move():
    moves = ['Rock', 'Paper', 'Scissors']

    return random.choice(moves)

def rock_paper_scissors():
    score_player = score_bot = 0
    outcomes = {
            'Rock': {'Scissors': 'Player', 'Paper': 'Bot'},
            'Paper': {'Rock': 'Player', 'Scissors': 'Bot'},
            'Scissors': {'Paper': 'Player', 'Rock': 'Bot'}
        }

    while score_player < 3 and score_bot < 3:
        player = 'empty_hand'
        bot = bot_move()

        while outcomes.get(player) is None:
            print('Rock Paper Scissors?')
            player = input('Choose your movement: ').strip().capitalize()
            print()
            
        print(f'{player = }, {bot = }')

        if player == bot:
            print('Draw\n')
            continue

        winner = outcomes[player][bot]

        if winner == 'Player':
            score_player += 1
        else:
            score_bot += 1
        
        print(f'Score: {score_player} x {score_bot}\n')

    print('You win' if score_player == 3 else 'Bot wins')

if __name__ == '__main__':
    rock_paper_scissors()