# Solitaire
Solitaire game in Python, using pygame library!

[How to play!](https://www.bicyclecards.com/how-to-play/solitaire/)

## Requirements
You will need Python 3 on your machine to run this project. You can download it on the official website link: https://www.python.org/downloads/

You will also need pygame, which can be installed using the command:
```
python3 -m pip install -U pygame --user
```

To check if it works, you can run one of the included examples:
```
python3 -m pygame.examples.aliens
```

## Running
To run this project, just open a terminal on the root folder and run:
```
python3 main.py
```
## Configuration
Currently, there are no interfaces for game configuration. It is possible to change the game settings by editing the parameters passed to Solitaire object on ```main.py```:
```python
# these are layout options
game = Solitaire(10, 20)
```
There will be more options in the future.

## Credits
Thanks to Kenney.nl for card assets!

## License
This project is licensed under the MIT License.
