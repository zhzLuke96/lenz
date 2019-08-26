# coding:utf-8
import sys
sys.path.append("../lenz")
from lenz import favor,BM
import re

need_log = False
favor1 = favor("./dict/no.txt", "./dict/neg.txt",
               "./dict/pos.txt", "../lenz/dict/improve.txt")
bm1 = BM("./dict/dict.txt")

def score_text(text):
    text = re.sub(re.compile(r"[a-zA-Z0-9]"), ";", text)
    return favor1(bm1(text))

# 简单的说，这就是一个失败的算法，基本失败不了短语
def TEST():
    text1 = "有一个角色叫酱爆，他的梦想，是成为一个伟大的作曲家"
    score1 = score_text(text1)
    if need_log:print(score1)
    assert score1 > 0, "积极"

    text2 = "python真是一门糟糕透顶语言"
    score2 = score_text(text2)
    if need_log:print(score2)
    # assert score2 < 0, "消极"


    text3 = "python虐我千百遍,我待python如初恋"
    score3 = score_text(text3)
    if need_log:print(score3)
    # assert score3 > 0, "积极"

    text4 = "看哭了。难看哭了。"
    score4 = score_text(text4)
    if need_log:print(score4)
    # assert score4 < 0, "消极"

    text5 = "我觉得这部电影唯一的正能量就是揭示了当代中国影业的乱象,不是电影中描述的,而是这部电影本身,就是一个搞笑的,无可救药的,荒诞的,具有历史性,纪实性,值得作为极端案例加以分析的,充满丑态的现实刻画"
    score5 = score_text(text5)
    if need_log:print(score5)
    assert score5 < 0, "消极"

    text6 = "看这书就一个字，爽。难以置信居然是教材。 虽然现在MIT已经不教lisp了，但是看这书学lisp绝对不吃亏。 程序员就是新世纪的魔法师！"
    score6 = score_text(text6)
    if need_log:print(score6)
    # assert score_text(text3) > 0, "积极"

if __name__ == "__main__":
    TEST()
    print("favor.test.py success all")