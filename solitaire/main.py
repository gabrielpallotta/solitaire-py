from solitaire import Solitaire

def main():
    game = Solitaire()
    while not game.should_quit:
        game.update()
        game.render()

if __name__ == '__main__':
    main()