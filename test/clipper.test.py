# coding:utf-8
import sys
sys.path.append("../lenz")
from lenz import BM
import re

need_log = False

bm1 = BM("./dict/dict.txt")
def clip_one(text):
    text = re.sub(re.compile(r"[a-zA-Z0-9]"), ";", text)
    seq = bm1(text)
    if need_log:
        print("src:")
        print(text)
        print("res:")
        print(seq)
    return seq

def TEST():
    text1 = "与魔鬼战斗的人，应当小心自己不要成为魔鬼。当你凝视深渊时，深渊也在凝视着你。"
    seq1 = clip_one(text1)

    assert "魔鬼" in seq1, "应该包含[魔鬼]"
    assert "深渊" in seq1, "应该包含[深渊]"

    text2 = ""
    seq2 = clip_one(text2)

    assert len(seq2) == 0 , "应该为空数组"

    text3 = "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
    seq3 = clip_one(text3)

    assert "亲口" in seq3, "应该包含[亲口]"
    assert "每月" in seq3, "应该包含[每月]"
    # assert "工信处" in seq3, "不应该分为处女"
    
    text4 = "调用两种算法当结果完全相同则返回"
    seq4 = clip_one(text4)

    assert "算法" in seq4, "应该包含[算法]"

    text5 = "南京市长江大桥"
    seq5 = clip_one(text5)

    assert "南京市" in seq5, "应该包含[南京市]"

    text6 = "正向最大匹配指的是从左到右对一个字符串进行匹配"
    seq6 = clip_one(text6)

    assert "字符串" in seq6, "应该包含[字符串]"


if __name__ == "__main__":
    TEST()
    print("chinese clipper success all")
