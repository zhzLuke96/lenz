# 求邻接信息熵
# 传入邻接列表，返回信息熵
from util import entropy, P, eMax, getSeq, cleanStopWord


def wordRank(seq, text):
    """
    词的灵活程度又它的左临集合和右临集合判定
    """
    LeftSet, RightSet = [], []
    cur = text.find(seq)
    wl = len(seq)
    while cur != -1:
        if cur != 0:
            LeftSet.append(text[cur - 1:cur])
        RightSet.append(text[cur + wl:cur + wl + 1])
        cur = text.find(seq, cur + len(seq))
    entr = min(entropy(LeftSet), entropy(RightSet))
    if entr == 0:
        return 0
    return 1 / entr


# def C(n, m):
#     return math.factorial(n) / (math.factorial(m) * math.factorial(n - m))

# def wordLen(text):
#     """出现字符个数"""
#     count = 0
#     temp = []
#     for s in text:
#         if (s not in temp):
#             count += 1
#             temp.append(s)
#     return count


def wordCohesion(seq, text):
    """
    词的内聚程度由
    """
    Pseq = P(seq, text)
    subPairs = [[seq[:i], seq[i:]] for i in range(1, len(seq))]
    pPair = map(lambda pair: Pseq / (P(pair[0], text) * P(pair[1], text)),
                subPairs)
    return min(pPair)


def seqsScore(text, maxlen=4, normalization=True):
    assert maxlen >= 2
    seqs = []
    for i in range(2, maxlen + 1):
        seqs += getSeq(text, i)
    scores = []
    fmax, fmin = 0, 0
    cmax, cmin = 0, 0
    rmax, rmin = 0, 0
    for word in seqs:
        ws = {
            "self": word,
            "freq": text.count(word),
            "cohes": wordCohesion(word, text),
            "rank": wordRank(word, text)
        }
        if ws["rank"] == 0:
            continue
        scores.append(ws)
        if ws["freq"] > fmax:
            fmax = ws["freq"]
        if ws["freq"] < fmin:
            fmin = ws["freq"]
        if ws["cohes"] > cmax:
            cmax = ws["cohes"]
        if ws["cohes"] < cmin:
            cmin = ws["cohes"]
        if ws["rank"] > rmax:
            rmax = ws["rank"]
        if ws["rank"] < rmin:
            rmin = ws["rank"]
    if not normalization:
        return scores
    # normalization
    for ws in scores:
        ws["freq"] = eMax(ws["freq"], fmin, fmax)
        ws["cohes"] = eMax(ws["cohes"], cmin, cmax)
        ws["rank"] = eMax(ws["rank"], rmin, rmax)
        ws["score"] = ws["freq"] * ws["cohes"] * ws["rank"]
    return scores


def shift(words):
    clened = []
    words = sorted(words, key=lambda x: len(x))
    for w in words:
        w = cleanStopWord(w)
        # if len(w) == 1:
        #     continue
        while True:
            if w == "":
                break
            canQuit = True
            for c in clened:
                if w.find(c) != -1:
                    w = w.replace(c, "")
                    canQuit = False
                    break
            if canQuit:
                break
        if w != "":
            clened.append(w)
    return clened


def dig(text, maxlen=4):
    assert maxlen >= 2
    scores = seqsScore(text, maxlen)
    scores = sorted(scores, key=lambda x: x["score"])
    return [s["self"] for s in scores[::-1]]


def dictPart(text, wd, maxl):
    src = text
    ts = []
    while len(text) != 0:
        seqs = getSeq(text, maxl) + [i for i in text]
        hit = False
        for s in seqs:
            if s in wd:
                ts.append(s)
                text = text.replace(s, "", 1)
                hit = True
                break
        if not hit:
            ts += [text]
            break
    return sorted(ts, key=lambda x: src.find(x))


def autoParticiple(text, maxlen=5):
    words = dig(text, maxlen)
    words = shift(words)
    words = sorted(words, key=lambda x: -len(x))
    wMax = max([len(x) for x in words])
    tokens = []
    seq = ""
    for s in text:
        seq += s
        if len(seq) >= wMax:
            tokens += dictPart(seq, words, wMax)
            seq = ""
        if seq in words:
            tokens.append(seq)
            seq = ""
    return tokens


if __name__ == "__main__":
    from pprint import pprint
    # res = entropy(["哈", "哈", "a", "this"])
    # res = entropy(["哈", "哈", "哈", "哈"])
    # print(res)
    text = ""
    text1 = "四是四十是十十四是十四四十是四十"
    text2 = "十四是十四四十是四十，十四不是四十，四十不是十四"
    # print(wordCohesion("信息", text))
    # print(wordRank("信息", text))
    # print(wordLen(text))
    # print(C(wordLen(text), 2))
    # print(getSeq(text, 1))
    # ss = seqsScore(text1)
    # top = [x["self"] for
    #  x in sorted(ss, lambda x: x["score"])[::-1][:10]]
    # print(top)
    # print(dig(text1))
    print(shift(dig(text, 5)))
    # print(shift(dig(text2)))
    # print(" ".join(autoParticiple(text)))
    # print(" ".join(autoParticiple(text2)))
    # print(" ".join(autoParticiple(text1)))
    # print(autoParticiple(text1,maxlen=2))
    # pprint(seqsScore(text,4,False))
    # print(wordRank("四是",text1))
