# coding:utf-8
from lenz import BM, favor, dig_words


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
    # seq1 = bm1("与魔鬼战斗的人，应当小心自己不要成为魔鬼。当你凝视深渊时，深渊也在凝视着你。")
    # print(seq1)
    # f1 = favor("./dict/no.txt", "./dict/neg.txt",
    #            "./dict/pos.txt", "./dict/improve.txt")
    # print(tbox(f1, bm1, "无论刷 star 还是卖 star 的，我都不会责备，因为问题不在他们，而在于企业素质低下的 HR 和面试官"))
    # print(tbox(f1, bm1, "恋爱小白陪大哥逛了一夜的场子，被几个小姐姐撩的春心荡漾，十年左右没有这种心动的感觉了。回家冲个澡抽根烟，冷静下来想到她们的热情从来都是对钱不对人，这辈子就好好当根么得感情的韭菜吧，FML"))

    # with open("./test/lstm.txt", "r", encoding="utf-8") as f:
    #     d_w = dig_words(f.read(), max_size=10, min_entropy=1, min_count=10)
    #     print(len(d_w), d_w[:10])
    #     print(claer_prefix(d_w))
    #
    # with open("./test/t6.txt", "r", encoding="utf-8") as f:
    #     d_w = dig_words(f.read(), max_size=10, min_entropy=1, min_count=10)
    #     print(len(d_w), d_w[:10])
    #     print(claer_prefix(d_w)[:10])

    # with open("./test/lstm.txt", "r", encoding="utf-8") as f:
    #     text = f.read()
    #     d_w = dig_words(text, max_size=5, min_entropy=2,
    #                     min_count=5, fest_mode=False)
    #     print(len(d_w), d_w[:10])
    #     print(claer_prefix(d_w)[:50])

    content = """ 孤独的美食家第01-06季.更多免费资源关注微信公众号 ：lydysc2017
 孤独的美食家第01季.更多免费资源关注微信公众号 ：lydysc2017
 孤独的美食家.EP01.kodokunogurume.ep01.深夜劇バー.字幕组.mkv301 MB
 孤独的美食家.EP02.kodokunogurume.ep02.深夜劇バー.字幕组.mkv314 MB
 孤独的美食家.EP03.kodokunogurume.ep03.深夜劇バー.字幕组.mkv319 MB
 孤独的美食家.EP04.kodokunogurume.ep04.深夜劇バー.字幕组.mkv317 MB
 孤独的美食家.EP05.kodokunogurume.ep05.深夜劇バー.字幕组.mkv315 MB
 孤独的美食家.EP06.kodokunogurume.ep06.深夜劇バー.字幕组.mkv310 MB
 孤独的美食家.EP07.kodokunogurume.ep07.深夜劇バー.字幕组.mkv313 MB
 孤独的美食家.EP08.kodokunogurume.ep08.深夜劇バー.字幕组.mkv308 MB
 孤独的美食家.EP09.kodokunogurume.ep09.深夜劇バー.字幕组.mkv316 MB
 孤独的美食家.EP10.kodokunogurume.ep10.深夜劇バー.字幕组.v2.mkv310 MB
 孤独的美食家.EP11.kodokunogurume.ep11.深夜劇バー.字幕组.mkv311 MB
 孤独的美食家.EP12.kodokunogurume.ep12.深夜劇バー.字幕组.mkv298 MB
 孤独的美食家第02季.更多免费资源关注微信公众号 ：lydysc2017
 孤独的美食家 第二季.EP01.kodokunogurume2.ep01.深夜劇バー.字幕组.mkv451 MB
 孤独的美食家 第二季.EP02.kodokunogurume2.ep02.深夜劇バー.字幕组(1).mkv443 MB
 孤独的美食家 第二季.EP03.kodokunogurume2.ep03.深夜劇バー.字幕组.mkv443 MB
 孤独的美食家 第二季.EP04.kodokunogurume2.ep04.深夜劇バー.字幕组.mkv443 MB
 孤独的美食家 第二季.EP05.kodokunogurume2.ep05.深夜劇バー.字幕组.mkv443 MB
 孤独的美食家 第二季.EP06.kodokunogurume2.ep06.深夜劇バー.字幕组.mkv443 MB
 孤独的美食家 第二季.EP07.kodokunogurume2.ep07.深夜劇バー.字幕组.mkv443 MB
 孤独的美食家 第二季.EP08.kodokunogurume2.ep08.深夜劇バー.字幕组.mkv443 MB
 孤独的美食家 第二季.EP09.kodokunogurume2.ep09.深夜劇バー.字幕组.mkv443 MB
 孤独的美食家 第二季.EP10.kodokunogurume2.ep10.深夜劇バー.字幕组(1).mkv443 MB
 孤独的美食家 第二季.EP11.kodokunogurume2.ep11.深夜劇バー.字幕组.mkv443 MB
 孤独的美食家 第二季.EP12.kodokunogurume2.ep12.END.深夜劇バー.字幕组.mkv441 MB
 孤独的美食家第03季.更多免费资源关注微信公众号 ：lydysc2017
 孤独的美食家 第三季.EP01.kodoku.no.gurume3.Chi_Jap.深夜剧バー.字幕组.mkv495 MB
 孤独的美食家 第三季.EP02.修复版.kodoku.no.gurume3.Chi_Jap.深夜剧バー.字幕组.mkv321 MB
 孤独的美食家 第三季.EP03.kodoku.no.gurume3.Chi_Jap.修复版.深夜剧バー.字幕组.mkv536 MB
 孤独的美食家 第三季.EP04.kodoku.no.gurume4.Chi_Jap.深夜剧バー.字幕组.mkv443 MB
 孤独的美食家 第三季.EP05.kodoku.no.gurume4.Chi_Jap.深夜剧バー.字幕组.V2.mkv428 MB
 孤独的美食家 第三季.EP06.kodoku.no.gurume3.Chi_Jap.深夜剧バー.字幕组.mkv539 MB
 孤独的美食家 第三季.EP07.kodoku.no.gurume3.Chi_Jap.深夜剧バー.字幕组.mkv534 MB
 孤独的美食家 第三季.EP08.kodoku.no.gurume3.Chi_Jap.深夜剧バー.字幕组.mkv540 MB
 孤独的美食家 第三季.EP09.kodoku.no.gurume3.Chi_Jap.深夜剧バー.字幕组.mkv538 MB
 孤独的美食家 第三季.EP10.kodoku.no.gurume3.Chi_Jap.深夜剧バー.字幕组.mkv537 MB
 孤独的美食家 第三季.EP11.kodoku.no.gurume3.Chi_Jap.深夜剧バー.字幕组.mkv540 MB
 孤独的美食家 第三季.EP12.kodoku.no.gurume3.Chi_Jap.深夜剧バー.字幕组V2.mkv539 MB
 孤独的美食家第04季.更多免费资源关注微信公众号 ：lydysc2017
 [迅雷下载www.2tu.cc]孤独的美食家4-EP08.rmvb201 MB
 [迅雷下载www.2tu.cc]孤独的美食家4-EP11.mp470 MB
 [迅雷下载www.2tu.cc]孤独的美食家4-EP12.mp470 MB
 kodokunogurum S4.EP01.深夜剧バー.字幕组.mkv412 MB
 kodokunogurume S4.EP02.双语.深夜剧バー.字幕组.mkv414 MB
 kodokunogurume S4.EP03.双语.深夜剧バー.字幕组.mkv414 MB
 kodokunogurume S4.EP04.双语.深夜剧バー.字幕组.mkv414 MB
 kodokunogurume S4.EP05.双语.深夜剧バー.字幕组.mkv411 MB
 kodokunogurume S4.EP06.双语.深夜剧バー.字幕组.mkv414 MB
 kodokunogurume S4.EP07.双语.深夜剧バー.字幕组.mkv413 MB
 kodokunogurume S4.EP09.双语.深夜剧バー.字幕组.mkv452 MB
 kodokunogurume S4.EP10.双语.深夜剧バー.字幕组.mkv451 MB
"""
    # print(bm1(content))
    # from collections import Counter
    # print(Counter(bm1(content)))
    print(dig_words(content, max_size=6,
                    min_entropy=.5, min_count=3, fest_mode=True)[:10])
