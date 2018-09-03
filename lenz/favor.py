import math
import re
from .clipper import BM

__all__ = ("favor",)


def mapped_zero2one(num):
    return round(math.atan(num) / math.pi + 0.5, 3)


class judge:
    def __init__(self, no_file, neg_file, pos_file, imp_file):
        self.no_dict = []
        self.neg_dict = []
        self.pos_dict = []
        self.improve_dict = []
        with open(neg_file, "r", encoding="utf-8") as f:
            self.neg_dict = f.read().split("\n")
        with open(no_file, "r", encoding="utf-8") as f:
            self.no_dict = f.read().split("\n")
        with open(pos_file, "r", encoding="utf-8") as f:
            self.pos_dict = f.read().split("\n")
        with open(imp_file, "r", encoding="utf-8") as f:
            self.improve_dict = f.read().split("\n")

    def __call__(self, text):
        score = 1
        for wi in range(len(text)):
            w = text[wi]
            if w in self.pos_dict:
                if wi != 0:
                    front = text[wi - 1]
                    if front in self.improve_dict:
                        score += 2
                    elif front in self.no_dict + self.neg_dict:
                        score -= 1
                    elif wi + 1 < len(text) and text[wi + 1] in self.neg_dict:
                        score -= 1
                    else:
                        score += 1
                else:
                    score += 1
            elif w in self.neg_dict:
                if wi != 0:
                    front = text[wi - 1]
                    if front in self.improve_dict:
                        score -= 2
                    elif front in self.no_dict:
                        score += 1
                    else:
                        score -= 2
                else:
                    score -= 2
            elif w in self.no_dict:
                score -= 1
        return score


class favor:
    def __init__(self, no_file, neg_file, pos_file, imp_file):
        self.judge = judge(no_file, neg_file, pos_file, imp_file)

    def __call__(self, words):
        score = self.judge(words)
        return mapped_zero2one(score)

# def favor(input):
#     input = re.sub(re.compile(r"[a-zA-Z0-9]"), ";", input)
#     words = BM(input)
#     # print(words)
#     score = judge(words)
#     # print(score)
#     return mapped_zero2one(score)
