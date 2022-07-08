
#!/usr/bin/env python

import os
import shutil
from datetime import datetime

os.system("cls")

print("Cantidad:")
q = int(input())

def my_function(q):
    now = datetime.now()
    formato = now.strftime('%m%d')
    rt_org = r"C:\Users\jhong\Desktop\IDLICITACION"
    for i in range(q):
        try:
            rt_dst = r"C:\Users\jhong\Documents\IDLICITACION{}-{}".format(formato, str(i+1))
            shutil.copytree(rt_org, rt_dst)
            print("Directorio Creado: {}".format(i+1))
        except:
            print("Directorio existe: {}".format(i+1))

if __name__ == "__main__":
    my_function(q)
