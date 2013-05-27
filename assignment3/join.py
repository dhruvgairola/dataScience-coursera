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
    key = record[0]
    value = record[1]
#    words = value.split()
    mr.emit_intermediate(value, (key, record))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for v in list_of_values:
        if v[0] == "order":
            for v2 in list_of_values:
                if v2[0] == "line_item":
                    mr.emit(v[1]+v2[1])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
