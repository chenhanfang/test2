import math
from io import StringIO
def show_tree(tree,total_width = 36,fill=' '):
    output = StringIO()
    last_raw = -1
    for i , n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1,2)))
        else:
            row = 0
        if row != last_raw:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0)/ columns))
        output.write(str(n).center(col_width,fill))
        last_raw = row
    print(output.getvalue())
    print('-' *total_width)
    return