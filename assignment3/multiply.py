import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    value = record[3]
    
    for i in range(0, 5):
        if record[0] == "a":
            mr.emit_intermediate((record[1], i), (record[2], value))
        else:
            mr.emit_intermediate((i, record[2]), (record[1], value))
            

def reducer(key, list_of_values):
    valSet = {}
    sum = 0
    for v in list_of_values:
        if v[0] not in valSet:
            valSet[v[0]] = v[1]
        else:
            sum += valSet[v[0]] * v[1]
    mr.emit((key[0], key[1], sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
