import codecs
import sys

strings = []
with codecs.open(sys.argv[1], 'rb', encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        sr, ur, other = line.split("\t")
        morphs = [x.split(":")[0] for x in other.split(" ")]
        string =  "\t".join([sr, ur, " ".join(morphs)])
        strings.append(string)

for string in strings:
    print string
    
