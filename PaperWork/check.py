def is_num(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def is_nvalue(str, n):
    if str.count(" ")!=(n-1):
        return True
    flag = False
    for i in range(0,n):
        if not(is_num(str.split()[i])) or float(str.split()[i])<0:
            flag = True
    if flag:
        return True
    return False

