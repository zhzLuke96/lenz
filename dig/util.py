import math
import re

pattern = re.compile(
    u'[\\s\\d,.<>/?:;\'\"[\\]{}()\\|~!@#$%^&*\\-_=+a-zA-Z，。《》、？：；“”‘’｛｝【】（）…￥！—┄－]+'
)


def cleanStopWord(text):
    return pattern.sub('', text)


def entropy(ls):
    length = len(ls)
    if length == 0 or length == 1:
        return 0
    frequence = {}
    for w in ls:
        frequence[w] = frequence.get(w, 0) + 1
    return sum(
        map(lambda x: -x / length * math.log(x / length), frequence.values()))


def P(seq, text):
    """片段在整体文本中的概率"""
    # return text.count(seq) / C(wordLen(text), len(seq))
    return text.count(seq) / len(text)


def eMax(n, low=1, up=10, bias=1):
    return bias + (n - low) / (up - low)


def getSeq(text, wlen=2):
    if wlen == 1:
        return list(set([s for s in text]))
    length = len(text)
    return list(
        set([text[i:i + wlen] for i in range(length) if i + wlen <= length]))
