# 数据挖掘
本来吧，这里搞搞分词、情感分析就差不多了，没想到绕来绕去又发现一个math的东西，数据挖掘，从语料中挖出新词，或者直接脱词

> 关键词: 信息论，信息熵，互信息，左右熵

[参考1:Matrix67](http://www.matrix67.com/blog/archives/5044)
[参考1:Matrix67](http://www.matrix67.com/blog/archives/5044)

# 大致思路
出现多的组合就是词，比如 `就是` 这个词，就是一个很容易出现在中文句子中的词，且它的左右词字都是非常不固定的。那么他与其余二元词相比更有可能就是一个值得关注的词语。

这里我随机找了一个来自[知乎](https://zhuanlan.zhihu.com/p/27812604)的大段文本作为基本的测试数据，当然无监督挖掘是可以胜任小段文本的单词挖掘的，只是...

# 概念
#### 自信息
I(x) = -log(p(x))

p(x)为x发生的概率，根据log函数的分布，自信息的定义就是`概率越小的事件，发生的时候带有的自信息越大`

#### 熵
公式一眼有点吓人，其实很简单

事件自信息的数学期望，就是熵

#### 互信息
互信息就是求的，条件熵：每个条件的子事件的组合事件信息熵的期望，有点拗口...不过弄清道理其实很简单

还是`就是`这个例子，我们定义它的互信息很大，即互信息表示了这个词中子词(字)的凝聚力很大。

> 可以想象为在一个语法烧杯中，如果有 `是 值 思 数 巴拉巴拉 就` 这几个词在做布朗运动，那么`是`和`就`非常有可能发生化学反应（不知道信息熵在自然科学上有没有什么发展？）

定义：<br>
log a (片段概率 除以 子序列概率的积)
<br>其实这里的a可以取任意值，通常为2

对于多序列的片段，子序列互信息累加就是片段的凝聚度

#### 左右熵
