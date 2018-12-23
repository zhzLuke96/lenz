import re
__all__ = ("BM", )


def judge_pure_english(keyword):
    return all(ord(c) < 128 for c in keyword)


def tans_n(seq):
    num_symbol = "1234567890一二两三四五六七八九十千百万亿"
    cur = 0
    while cur < len(seq):
        if seq[cur] in num_symbol:
            cur += 1
        else:
            break
    return seq[cur:], str(seq[:cur])


def fmm(_input, maxlen=5, _dict={}):
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
            if test_t in _dict[len(test_t)]:
                res.append(temp)
                cur += len(temp)
                break
            if _n == "一" and temp in _dict[len(temp)]:
                res.append(temp)
                cur += len(temp)
                break
            temp = temp[:-1]
    return res


def bmm(_input, maxlen=5, _dict={}):
    """
    right cut
    """
    res = []
    cur = 0
    while cur < len(_input):
        temp = _input[-(cur + maxlen):len(_input) - cur]
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
            if test_t in _dict[len(test_t)]:
                res.append(temp)
                cur += len(temp)
                break
            if _n == "一" and temp in _dict[len(temp)]:
                res.append(temp)
                cur += len(temp)
                break
            temp = temp[1:]
    return res[::-1]


split_pattern = re.compile(
    r"[,./;':\"'<>\?\\\/!@#\$%\^&\*()~`\|，。、《》；‘：’“”【】\{\}\[\]！~·￥（）？\n 」「…『』◆×•®«»➊　]"
)


class BM:
    def __init__(self, dictfile, maxlen=5):
        self.dict, self.maxlen = {}, maxlen
        self.pull_dict(dictfile)

    def pull_dict(self, dictfile):
        with open(dictfile, "r", encoding="utf-8") as f:
            dict_arr = f.read().split("\n")
        for seq in dict_arr:
            if (not len(seq) in self.dict.keys()):
                self.dict[len(seq)] = []
            self.dict[len(seq)].append(seq)

    def __call__(self, text):
        """
        调用两种算法当结果完全相同则返回
        不同则选择词数少的一个
        若词数相同，选择单字最少
        """
        if split_pattern.search(text):
            res = []
            seqs = re.split(split_pattern, text)
            for seq in seqs:
                if len(seq) == 0:
                    continue
                res += self(seq)
            return res
        if judge_pure_english(text):
            return [text]
        _fm = fmm(text, self.maxlen, self.dict)
        _bm = bmm(text, self.maxlen, self.dict)
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
