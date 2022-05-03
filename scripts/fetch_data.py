set_name = set()
f = open("correctsample_100.metadata", 'r')
for line in f:
    fields = line.split()
    set_name.add(fields[0])
f.close()
print(len(set_name))

f = open("covid19/sample_headers_10k.fasta", 'r')
fo = open("covid19/real_10k.fasta", 'w')
name = f.readline().split('|')[1]
seq = ""
set_use = set()
for line in f:
    if line[0] == '>':
        if name in set_name:
            fo.write('>' + name + '\n')
            fo.write(seq)
            set_use.add(name)
        name = line.split('|')[1]
        seq  = ""
    else:
        seq += line
if name in set_name:
    fo.write('>' + name + '\n')
    fo.write(seq)
    set_use.add(name)
f.close()
fo.close()
print(set_name-set_use)
