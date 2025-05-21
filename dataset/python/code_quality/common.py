
def doTask(x, y=100, resultList=[]):  # Poor naming + magic number + mutable default
    temp = 3.14 * x  # magic number
    unused = "debug"  # Unused variable
    resultList.append(temp + y)
    return resultList
