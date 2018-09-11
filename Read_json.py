import json
import sys
fil1 = sys.argv[1]
fil2 = sys.argv[2]
data = []
with open(fil1) as f1:
    for line in f1:
        data.append(json.loads(line))
new_info = []
with open(fil2) as f2:
    for line in f2:
        d1 = {}
        geneInfo = line.strip("\n").split("\t")
        d1["基因名称"] = geneInfo[0]
        d1["NM号"] = geneInfo[1]
        d1["外显子数"] = geneInfo[2]
        d1["内含子数"] = geneInfo[3]
        new_info.append(d1)
#print(new_info)
for each_array in data:
    s1 = json.dumps(each_array)
    d1 = json.loads(s1)
    gene = d1["基因检测产品"]
#        print(type(d1["基因检测产品"]))
    for a in gene:
        if "," in a:
            new_gene = a.split(",")
            d1["基因检测产品"] = new_gene
#    print(d1["基因检测产品"])
    for b in new_info:
        if b["基因名称"] == d1["基因名称"]:
            d1["NM号"] = b["NM号"]
            d1["外显子数"] = b["外显子数"]
            d1["内含子数"] = b["内含子数"]
    if len(d1["外显子数"]) == 0:
        pass
    else:
        print(d1)
#        print(d1['基因名称'])
#        print(d1["相关疾病"])
