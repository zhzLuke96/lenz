# 论词
大佬论语，这里就谈谈词

# lenz
- [x] bm分词
- [x] 机械情感分析
- [x] 无字典分词，hmm
- [ ] 情感字典加权重
- [ ] rnn

# usage
#### 分词
```python
bm1 = BM("./dict/dict.txt")
print(bm1("与魔鬼战斗的人，应当小心自己不要成为魔鬼。当你凝视深渊时，深渊也在凝视着你。"))

# ['与', '魔鬼', '战斗', '的人', '应当', '小心', '自己', '不要', '成为',
# '魔鬼', '当你', '凝视', '深渊', '时', '深渊', '也在', '凝视着', '你']
```

#### word mining
```python
def box(favor_obj, BM_obj, text):
    import re
    text = re.sub(re.compile(r"[a-zA-Z0-9]"), ";", text)
    words = BM_obj(text)
    return favor_obj(words)
```
挖词需要简单的包装一道(主要为了复用，之前就一脚本)

挖掘效果很明显，但是缺点也很明显，任意把词语拆成多个

以下是挖`rnn.txt`文本之后的结果:
> \['神经网络', 'RNN', 'LSTM', '神经网', 'LST', 'STM', '经网络', '网络', '梯度', '神经', 'RN', '单元', '问题', '输入', '权重', '算法', '可以', '智能', 'LS', 'TM', 'ST', '人工', '经网', '一个'\]

# declare
大部分来自网络，能查明出处的数据我会尽量标注
