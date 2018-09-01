
from clipper import BM, fmm, bmm
from favor import favor

text1 = "调用两种算法当结果完全相同则返回"
text2 = "南京市长江大桥"
text3 = "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
text4 = "正向最大匹配指的是从左到右对一个字符串进行匹配"
print(fmm(text1))
print(bmm(text1))
print(BM(text1))
print()
print(fmm(text2))
print(bmm(text2))
print(BM(text2))
print()
print(fmm(text3))
print(bmm(text3))
print(BM(text3))
print()
print(fmm(text4))
print(bmm(text4))
print(BM(text4))

print()
print(BM("所谓词典正向最大匹配就是将一段字符串进行分隔，其中分隔的长度有限制，然后将分隔的子字符串与字典中的词进行匹配，如果匹配成功则进行下一轮匹配，直到所有字符串处理完毕，否则将子字符串从末尾去除一个字，再进行匹配，如此反复。"))

text1 = "有一个角色叫酱爆，他的梦想，是成为一个伟大的作曲家"
text2 = "python真是一门糟糕透顶语言"
text3 = "python虐我千百遍,我待python如初恋"
text4 = "看哭了。难看哭了。"
text5 = "我觉得这部电影唯一的正能量就是揭示了当代中国影业的乱象,不是电影中描述的,而是这部电影本身,就是一个搞笑的,无可救药的,荒诞的,具有历史性,纪实性,值得作为极端案例加以分析的,充满丑态的现实刻画"
from clipper import BM
print(favor(text1))
print(favor(text2))
print(favor(text3))
print(favor(text4))
print(favor(text5))

print(favor("看这书就一个字，爽。难以置信居然是教材。 虽然现在MIT已经不教lisp了，但是看这书学lisp绝对不吃亏。 程序员就是新世纪的魔法师！"))
