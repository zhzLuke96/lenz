# 预处理

with open("dict.txt", "r", encoding="utf-8") as f:
    cn_dict = f.read().split("\n")

# dict_cut = {"2": [], "3": [], "4": [], "5": []}
# lenMore = []
#
# for term in cn_dict:
#     t_len = len(term)
#     if t_len <= 5:
#         dict_cut[str(t_len)].append(term)
#     else:
#         lenMore.append(term)
#
# for k, v in dict_cut.items():
#     with open(f"./Daily/dict_{k}.txt", "w", encoding="utf-8") as f:
#         f.write("\n".join(v))
#
# with open("./Daily/dict_more.text", "w", encoding="utf-8") as f:
#     f.write("\n".join(lenMore))

with open("./Daily/prefix.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(list(set([w[:-1] for w in cn_dict]))))
