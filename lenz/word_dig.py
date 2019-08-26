# coding:utf-8

from collections import Counter
import math

__all__ = ("dig_words", "clear_knowWord")


def words_split(_input, size=2):
    res = []
    cur = 0
    while cur < len(_input):
        seq = _input[cur:cur + size]
        if len(seq) == size:
            res.append(seq if isinstance(seq, str) else "".join(seq))
        cur += 1
    return res


def split_Text(text, maxsize=4):
    res = {}
    for i in range(maxsize):
        s = words_split(text, i + 1)
        res[i + 1] = (Counter(s), s)
    return res


def sub_seq(text):
    """
    电影院 => [电影+院,电+影院]
    """
    res = []
    cur = 1
    while cur < len(text):
        res.append((text[:cur], text[cur:]))
        cur += 1
    return res


def info(_k, textObj):
    def _P(x):
        return textObj[len(x)][0][x] / len(textObj[len(x)][0])

    if len(_k) == 2:
        return math.log(_P(_k) / (_P(_k[0]) * _P(_k[1])), 2)
    subs = sub_seq(_k)
    p_above = _P(_k)
    res = 0
    for sub in subs:
        p2 = _P(sub[1])
        p1 = _P(sub[0])
        res += math.log(p_above / (p2 * p1), 2)
    return res


def entropy(_key, textObj):
    count, sarr = textObj[len(_key) + 1]
    count_len = len(count)
    re = 0
    le = 0
    for seq, c in count.items():
        if seq[:len(_key)] == _key:
            p = c / count_len
            re += (-p * math.log(p, 2))
        if seq[-len(_key):] == _key:
            p = c / count_len
            le += (-p * math.log(p, 2))
    return le, re


def default_stop_word(_input):
    import re
    return re.sub(
        re.compile(
            r"[,./;':\"'<>\?\\\/!@#\$%\^&\*()~`\|，。、《》；‘：’“”【】\{\}\[\]！~·￥（）？\n 」「…『』◆×•®«»➊　]"
        ), "", _input)

def dig_words(_input,
              max_size=2,
              min_entropy=1,
              min_count=10,
              fest_mode=False,
              stop_word=default_stop_word,
              cleared=False):
    _input = _input if stop_word is None else stop_word(_input)
    sp_o = split_Text(_input, max_size + 1)
    res = {}
    for i in range(2, max_size + 1):
        count, sarr = sp_o[i]
        for seq, c in count.items():
            if c < min_count:
                continue
            _info = info(seq, sp_o)
            if _info < min_entropy:
                continue
            if fest_mode:
                res[seq] = c * _info
            else:
                _l, _r = entropy(seq, sp_o)
                res[seq] = c * (_info + _l + _r)
    sorted_res = sorted(res.keys(), key=lambda x: res[x], reverse=True)
    if cleared:
        return claer_prefix(sorted_res)
    else:
        return sorted_res

def claer_prefix(arr):
    res = []
    for i in arr:
        for r in res:
            if len(r) > len(i):
                if r.find(i) != -1:
                    break
        else:
            res.append(i)
    return res

def clear_knowWord(arr,dict_path):
    ret = []
    with open(dict_path, "r", encoding="utf-8") as f:
        dict_arr = f.read().split("\n")
        for w in arr:
            if w not in dict_arr:
                ret.append(w)
    return ret

if __name__ == '__main__':
    text = "出现多的组合就是词比如就是这个词就是一个很容易出现在中文句子中的词且它的左右词字都是非常不固定的那么他与其余二元词相比更有可能就是一个值得关注的词语"

    # print(dig_words(text, 2)[:20])
    #
    # with open("dig_text.txt", "r", encoding="utf-8") as f:
    #     # print(stop_word(f.read()))
    #     print(dig_words(f.read(), 4)[:20])
    #
    # with open("dream.txt", "r", encoding="utf-8") as f:
    #     print(dig_words(f.read(), 4)[:20])

    with open("t1.txt", "r", encoding="utf-8") as f:
        d_t1 = dig_words(f.read(), 2)

    with open("t2.txt", "r", encoding="utf-8") as f:
        d_t2 = dig_words(f.read(), 2)

    res = []

    def p_t(x):
        return 1 / ((d_t1.index(x) + 1) * (d_t2.index(x) + 1))

    for d in d_t1:
        if d in d_t2:
            res.append((p_t(d), d))
    res.sort(key=lambda x: x[0])
    print([r[1] for r in res][::-1][:50])
