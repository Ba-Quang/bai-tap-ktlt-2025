print("sinh vien: Nguyễn Bá Quảng")
print("Mssv: 235752020710045")
str=input ("Enter a String:")
dict={}
for n in str:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
        print(dict)
