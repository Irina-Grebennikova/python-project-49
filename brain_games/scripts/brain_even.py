from brain_games.cli import welcome_user
from brain_games.games.brain_even import brain_even_game


def main():
    name = welcome_user()
    brain_even_game(name)


if __name__ == '__main__':
    main()