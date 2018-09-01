import math
import re
from clipper import BM

__all__ = ("favor",)

no_dict = []
neg_dict = []
pos_dict = []
improve_dict = []

with open("./dict/neg.txt", "r", encoding="utf-8") as f:
    neg_dict = f.read().split("\n")
with open("./dict/no.txt", "r", encoding="utf-8") as f:
    no_dict = f.read().split("\n")
with open("./dict/pos.txt", "r", encoding="utf-8") as f:
    pos_dict = f.read().split("\n")
with open("./dict/improve.txt", "r", encoding="utf-8") as f:
    improve_dict = f.read().split("\n")


def judge(input):
    score = 1
    for wi in range(len(input)):
        w = input[wi]
        if w in pos_dict:
            if wi != 0:
                front = input[wi - 1]
                if front in improve_dict:
                    score += 2
                elif front in no_dict + neg_dict:
                    score -= 1
                elif wi + 1 < len(input) and input[wi + 1] in neg_dict:
                    score -= 1
                else:
                    score += 1
            else:
                score += 1
        elif w in neg_dict:
            if wi != 0:
                front = input[wi - 1]
                if front in improve_dict:
                    score -= 2
                elif front in no_dict:
                    score += 1
                else:
                    score -= 2
            else:
                score -= 2
        elif w in no_dict:
            score -= 1
    return score


def mapped_zero2one(num):
    return round(math.atan(num) / math.pi + 0.5, 3)


def favor(input):
    input = re.sub(re.compile(r"[a-zA-Z0-9]"), ";", input)
    words = BM(input)
    print(words)
    score = judge(words)
    print(score)
    return mapped_zero2one(score)
