from os import rename

for i in range(50):
    oldname = "RDG1src-"+str(i)+'.txt'
    newname = "DAG-"+str(i)+'.txt'
    rename(oldname, newname)


