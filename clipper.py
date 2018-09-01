import re
__all__ = ("BM",)


cn_dict = {"2": [], "3": [], "4": [], "5": []}

for index in range(2, 6):
    with open(f"./dict/daily/dict_{index}.txt", "r", encoding="utf-8") as f:
        cn_dict[str(index)] = f.read().split("\n")


def fmm(input, maxlen=5):
    """
    left cut
    """
    res = []
    cur = 0
    while cur < len(input):
        temp = input[cur:cur + maxlen]
        for i in range(len(temp)):
            if len(temp) == 1:
                res.append(temp)
                cur += 1
                break
            if temp in cn_dict[str(len(temp))]:
                res.append(temp)
                cur += len(temp)
                break
            temp = temp[:-1]
    return res


def bmm(input, maxlen=5):
    """
    right cut
    """
    res = []
    cur = 0
    while cur < len(input):
        temp = input[- (cur + maxlen): len(input) - cur]
        for i in range(len(temp)):
            if len(temp) == 1:
                res.append(temp)
                cur += 1
                break
            if temp in cn_dict[str(len(temp))]:
                res.append(temp)
                cur += len(temp)
                break
            temp = temp[1:]
    return res[::-1]


split_pattern = re.compile(
    r"[,.;:'\"?!@#$%^&*()~`<>\{\}\[\]\\|，。：；“”、？！￥…（）《》【】·]")


def BM(input, maxlen=5):
    """
    调用两种算法当结果完全相同则返回
    不同则选择词数少的一个
    若词数相同，选择单字最少
    """
    if split_pattern.search(input):
        res = []
        seqs = re.split(split_pattern, input)
        for seq in seqs:
            if len(seq) == 0:
                continue
            res += BM(seq)
        return res
    _fm = fmm(input, maxlen)
    fm_one = 0
    for w in _fm:
        if len(w) == 1:
            fm_one += 1
    _bm = bmm(input, maxlen)
    bm_one = 0
    for w in _bm:
        if len(w) == 1:
            bm_one += 1
    if len(_fm) == len(_bm):
        if bm_one == fm_one:
            return _bm
        else:
            if bm_one > fm_one:
                return _fm
            else:
                return _bm
    else:
        if len(_fm) > len(_bm):
            return _bm
        else:
            return _fm
