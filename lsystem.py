import math
import pygame
from configparser import ConfigParser

# config
config = ConfigParser()
config.read("config/lsystem_deafult.ini")
graphic = config["GRAPHIC"]
WIDTH = int(graphic["width"])
HEIGHT = int(graphic["height"])
OFFSET = int(graphic["offset"])

class LSystem:

    def __init__(self, sentence, rules, start, length, ratio, dthetha):
        self.sentence = sentence
        self.rules = rules
        self.save_positions = []
        self.start = start
        self.lenght = length
        self.ratio = ratio
        self.dthetha = dthetha
        self.alpha = math.pi/2
        self.x, self.y = start

    def __str__(self):
        return self.sentence

    def generate(self):
        self.sentence = "".join([c if c not in self.rules.keys() else self.rules[c] for c in self.sentence])

    def draw(self):
        screen = pygame.display.get_surface()
        self.restart()
        for c in self.sentence:
            if c == "F" or c == "G":
                x2 = self.x - self.lenght * math.cos(self.alpha)
                y2 = self.y - self.lenght * math.sin(self.alpha)
                pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (x2, y2))
                self.x, self.y = x2, y2
            elif c == "+":
                self.alpha += self.dthetha
            elif c == "-":
                self.alpha -= self.dthetha
            elif c == "[":
                self.save_positions.append({"position": (self.x, self.y), "angle": self.alpha})
            elif c == "]":
                last_position = self.save_positions.pop()
                self.x, self.y = last_position["position"]
                self.alpha = last_position["angle"]

    def restart(self):
        self.x, self.y = self.start
        self.alpha = math.pi/2
        self.lenght *= self.ratio

def choose_starting_point(expresion: list[str]) -> list[int]:
    start = [0, 0]
    if expresion[0] == "bottom":
        start[1] = HEIGHT-OFFSET
    elif expresion[0] == "top":
        start[1] = OFFSET
    elif expresion[0] == "center":
        start[1] = HEIGHT//2
    else:
        raise Exception("Invalide position argument")

    if expresion[1] == "right":
        start[0] = WIDTH-OFFSET
    elif expresion[1] == "left":
        start[0] = OFFSET
    elif expresion[1] == "center":
        start[0] = WIDTH//2
    else:
        raise Exception("Invalide position argument")
    return start

def load_lsystem_from_file(path: str) -> LSystem:
    with open(path) as f:
        data = f.read().split("\n")
        starting_sentence = data[0]
        rules = {a: b  for a, b in [c.split(":") for c in data[1].split(" ")]}
        lenght = int(data[2])
        dthetha = math.radians(int(data[3]))
        ratio = 1/float(data[4])
        starting_pos = data[5].split(" ")
    return LSystem(
        sentence=starting_sentence,
        rules=rules,
        start = choose_starting_point(starting_pos),
        length = lenght,
        ratio=ratio,
        dthetha=dthetha
    )
