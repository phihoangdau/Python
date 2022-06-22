import re
from gethtmlfunction import gethtmlcontent

data = gethtmlcontent("http://www.pythonchallenge.com/pc/def/equality.html",0)
# this [A-Z][A-Z][A-Z] can replace with this [A-Z]{3} also need this + to , [^A-Z] <-> [a-z]
partten = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data, re.DOTALL)

print("".join(partten))



