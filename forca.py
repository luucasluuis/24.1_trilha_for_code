import pathlib
from random import choice


path_arquivo = pathlib.Path(__file__).parent / 'palavras_forca.txt'
def get_secret_word(path_arquivo=path_arquivo):
    with open(path_arquivo, 'r', encoding='utf8') as arquivo:
        secret_word = choice([word for word in arquivo]).strip().lower()
    
    return secret_word

def get_user_guess():
    return input('Chute uma letra ').strip().lower()

def correct_guesses(guess, formed_word, secret_word):
    if guess in formed_word:
        print('\nEsta letra já foi acertada, tente outra!')
        return formed_word
    
    for index, letter in enumerate(secret_word):
        if letter == guess:
            formed_word[index] = guess
    return formed_word
        
def display_guess_place(secret_word):
    return ['_' if letter not in ('-', ' ') else letter for letter in secret_word.strip()]

secret_word = get_secret_word()
def main():
    max_errors = int(len(secret_word) * 0.5) + 1
    formed_word = display_guess_place(secret_word)
    print(f'É possivel errar {max_errors} vezes nessa partida')
    hang = False
    win = False

    wrong_guesses = ''
    wrong_guesses_counter = 0
    
    while not hang and not win:
        print(f'Letras erradas:{wrong_guesses}\n')
        print(' '.join(formed_word))

        while True:
            try:
                user_guess = get_user_guess()
                if len(user_guess) > 1:
                    raise ValueError('\nDigite uma letra por vez')
                if not user_guess.isalpha():
                    raise ValueError('\nSomente letras são aceitas')
                break
            except ValueError as e:
                print(e)
                user_guess = get_user_guess

        if user_guess in secret_word:
            formed_word = correct_guesses(user_guess, formed_word, secret_word)
            if '_' not in formed_word:
                win = True            
        else:
            if user_guess in wrong_guesses:
                print("\nVocê já tentou essa. Pelo visto você realmente gosta"\
                      "de insistir nos mesmos erros, né? \n")
                continue
            wrong_guesses += f' {user_guess}'
            wrong_guesses_counter += 1

            if wrong_guesses_counter ==  max_errors:
                hang = True
        print()

    if win:
        print('Acertou!!')
    elif hang:
        print('Enforcou!!')

    print(f'A palavra secreta era: {secret_word}')

if __name__ == '__main__':
    main()