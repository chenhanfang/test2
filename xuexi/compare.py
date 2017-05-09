import difflib
from difflib_data import *

d = difflib.Differ()
diff =d.compare(text1_lines,text2_lines)
print('\n'.join(diff))

diff1= difflib.unified_diff(text1_lines,
                            text2_lines,
                            lineterm='',)
print('\n'.join(list(diff1)))