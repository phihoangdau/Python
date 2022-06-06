import re
import string
from gethtmlfunction import *

data1 = "aAAAbCCCdDDD"
data = gethtmlcontent("http://www.pythonchallenge.com/pc/def/equality.html",0)
partten = re.findall("[^A-Z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][^A-Z]", data, re.DOTALL)

print("".join(partten))



