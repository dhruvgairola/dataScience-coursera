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
    if not ((key == "Myriel" and value == "Valjean") or (value == "Myriel" and key == "Valjean") or (key == "Myriel" and value == "Champtercier") or (value == "Myriel" and key == "Champtercier")):
        mr.emit_intermediate(key, value)
        mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for v in list_of_values:
        mr.emit((key, v))
#        mr.emit(v2[1])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
