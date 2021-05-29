
def str_to_hash(st):
    new = st.replace('=', ':')
    lst = new.split(",")
    return lst 


print(str_to_hash("a=1, b=2, c=3, d=4"))
print(str_to_hash(""))