# coding:utf-8
from lenz import BM, favor, dig_words, dig_words_nostop


def tbox(favorObj, BMobj, text):
    import re
    text = re.sub(re.compile(r"[a-zA-Z0-9]"), ";", text)
    words = BMobj(text)
    return favorObj(words)


def claer_prefix(arr):
    res = []
    for i in arr:
        for r in res:
            if len(r) > len(i):
                if r[:len(i)] == i or r[-len(i):] == i:
                    break
        else:
            res.append(i)
    return res


if __name__ == '__main__':
    bm1 = BM("./dict/dict.txt")
    print(bm1("与魔鬼战斗的人，应当小心自己不要成为魔鬼。当你凝视深渊时，深渊也在凝视着你。"))
    f1 = favor("./dict/no.txt", "./dict/neg.txt",
               "./dict/pos.txt", "./dict/improve.txt")
    print(tbox(f1, bm1, "无论刷 star 还是卖 star 的，我都不会责备，因为问题不在他们，而在于企业素质低下的 HR 和面试官"))
    print(tbox(f1, bm1, "恋爱小白陪大哥逛了一夜的场子，被几个小姐姐撩的春心荡漾，十年左右没有这种心动的感觉了。回家冲个澡抽根烟，冷静下来想到她们的热情从来都是对钱不对人，这辈子就好好当根么得感情的韭菜吧，FML"))

    # with open("./test/lstm.txt", "r", encoding="utf-8") as f:
    #     d_w = dig_words(f.read(), max_size=10, min_entropy=1, min_count=10)
    #     print(len(d_w), d_w[:10])
    #     print(claer_prefix(d_w))
    #
    # with open("./test/t6.txt", "r", encoding="utf-8") as f:
    #     d_w = dig_words(f.read(), max_size=10, min_entropy=1, min_count=10)
    #     print(len(d_w), d_w[:10])
    #     print(claer_prefix(d_w)[:10])

    with open("./test/lstm.txt", "r", encoding="utf-8") as f:
        d_w = dig_words(f.read(), max_size=5, min_entropy=2,
                        min_count=5, fest_mode=False)
        print(len(d_w), d_w[:10])
        print(claer_prefix(d_w)[:50])
