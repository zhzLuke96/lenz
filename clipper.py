import re
__all__ = ("BM",)


cn_dict = {"2": [], "3": [], "4": [], "5": []}

for index in range(2, 6):
    with open(f"./dict/daily/dict_{index}.txt", "r", encoding="utf-8") as f:
        cn_dict[str(index)] = f.read().split("\n")


def tans_n(seq):
    num_symbol = "1234567890一二两三四五六七八九十千百万亿"
    num_ = ""
    cur = 0
    while cur < len(seq):
        if seq[cur] in num_symbol:
            cur += 1
        else:
            break
    return seq[cur:], str(seq[:cur])


def fmm(_input, maxlen=5):
    """
    left cut
    """
    res = []
    cur = 0
    while cur < len(_input):
        temp = _input[cur:cur + maxlen]
        for i in range(len(temp)):
            if len(temp) == 1:
                res.append(temp)
                cur += 1
                break
            test_t, _n = tans_n(temp)
            if len(_n) != 0:
                test_t = "n" + test_t
            if len(test_t) == 1:
                res.append(temp)
                cur += len(temp)
                break
            if test_t in cn_dict[str(len(test_t))]:
                res.append(temp)
                cur += len(temp)
                break
            if _n == "一" and temp in cn_dict[str(len(temp))]:
                res.append(temp)
                cur += len(temp)
                break
            temp = temp[:-1]
    return res


def bmm(_input, maxlen=5):
    """
    right cut
    """
    res = []
    cur = 0
    while cur < len(_input):
        temp = _input[- (cur + maxlen): len(_input) - cur]
        for i in range(len(temp)):
            if len(temp) == 1:
                res.append(temp)
                cur += 1
                break
            test_t, _n = tans_n(temp)
            if len(_n) != 0:
                test_t = "n" + test_t
            if len(test_t) == 1:
                res.append(temp)
                cur += len(temp)
                break
            if test_t in cn_dict[str(len(test_t))]:
                res.append(temp)
                cur += len(temp)
                break
            if _n == "一" and temp in cn_dict[str(len(temp))]:
                res.append(temp)
                cur += len(temp)
                break
            temp = temp[1:]
    return res[::-1]


split_pattern = re.compile(
    r"[,.;:'\"?!@#$%^&*()~`<>\{\}\[\]\\|，。：；“”、？！￥…（）《》【】·]")


def BM(_input, maxlen=5):
    """
    调用两种算法当结果完全相同则返回
    不同则选择词数少的一个
    若词数相同，选择单字最少
    """
    if split_pattern.search(_input):
        res = []
        seqs = re.split(split_pattern, _input)
        for seq in seqs:
            if len(seq) == 0:
                continue
            res += BM(seq)
        return res
    _fm = fmm(_input, maxlen)
    _bm = bmm(_input, maxlen)
    # print("fmm:", _fm)
    # print("bmm:", _bm)
    if len(_fm) == len(_bm):
        fm_avg = 0
        bm_avg = 0
        for w in _fm:
            fm_avg += len(w)
        for w in _bm:
            bm_avg += len(w)
        fm_avg = fm_avg / len(_fm)
        bm_avg = bm_avg / len(_bm)

        if fm_avg == bm_avg:
            # return _bm
            fm_var = 0
            bm_var = 0
            for w in _fm:
                fm_var += len(w) - fm_avg
            for w in _bm:
                bm_var += len(w) - bm_avg
            fm_var = fm_var * (1 / len(_fm))
            bm_var = bm_var * (1 / len(_bm))
            if fm_var == bm_var:
                return _bm
            elif fm_var > bm_var:
                return _bm
            else:
                return _fm
        else:
            if fm_avg > bm_avg:
                return _fm
            else:
                return _bm
    else:
        if len(_fm) > len(_bm):
            return _bm
        else:
            return _fm


if __name__ == '__main__':
    print(tans_n("九十一瓶哇哈哈哈"))
    print(tans_n("91瓶哇哈哈哈"))
    print(tans_n("哇哈哈哈"))
