# 论词
一个简陋的分词脚本

# lenz
- [x] bm分词
- [x] 机械情感分析
- [x] 无字典分词，hmm
- [x] 英文单词分词，挖掘增加单词
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
#### 情感判断
> favor([...])

输出-1到1的值，负数表示消极，反正积极

#### word dig
挖掘效果还行，但是缺点也很明显，内部聚合度的判断有一点小问题

以下是挖`./test/lstm.txt`文本之后的结果:
> \['神经网络', 'RNN', 'LSTM', '人工智能', '梯度下降', '反向传播', '短期记忆', '消失问题', '梯度消失', '度消失问', '深度学习', 'RNN网', '损失函数', 'NN网络', '下降算法', '人造神经', '度下降算', '单元', '训练', '输入', '权重', '调整', '可以', '字符', '它们的', '突破', '公司', '研究', 'BP', '的权重', '分配', '的算法', '通过', '计算', '涉及', '发展', '时间', '网络的', '能力', '输出'\]

显然
> \['神经网络', 'RNN', 'LSTM', '人工智能', '梯度下降', '反向传播', '短期记忆'\]

这些词均是挖掘出来的新词，效果基本与文本长度正相关，越长效果越好

# declare
大部分来自网络，能查明出处的数据我会尽量标注

# updata log
- 加了一点测试
- 现在仍然是很简陋的版本...

# todo
- 如果能找到更详细的比如词性词典，应该可以更好的分词
- dict对象应该独立出来
- dockerfile

