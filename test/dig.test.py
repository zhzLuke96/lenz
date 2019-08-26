# coding:utf-8
import sys
sys.path.append("../lenz")
from lenz import dig_words,clear_knowWord

need_log = True

def TEST_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
        d_w = dig_words(text, max_size=4, min_entropy=2,
                        min_count=5, fest_mode=False, cleared=True)
        return d_w

def TEST():
    words1 = TEST_file("./test/lstm.txt")
    if need_log:print(words1[:50])
    # print(clear_knowWord(words1[:10], "./dict/dict.txt"))

    assert "神经网络" in words1
    assert "LSTM" in words1
    assert "RNN" in words1

    words2 = TEST_file("./test/dream.txt")
    # print(clear_knowWord(words2[:10], "./dict/dict.txt"))
    if need_log:print(words2[:50])

    assert "黑人" in words2

    words3 = TEST_file("./test/freedom.txt")
    if need_log:print(words3[:50])
    # print(clear_knowWord(words3[:10], "./dict/dict.txt"))

    # assert "黑人" in words1

    
    words4 = TEST_file("./test/jobs.txt")
    if need_log:print(words4[:50])
    # print(clear_knowWord(words4[:10], "./dict/dict.txt"))

if __name__ == "__main__":
    TEST()
    print("dig.test.py success all")
