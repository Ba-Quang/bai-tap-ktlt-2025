print("Nguyễn Bá Quảng")
print("MSSV:235752020710045")

chuoi = input('Nhập chuỗi cac tu tieng anh: ')
ds_list = chuoi.split()
ds_list.sort()
print('cac tu theo thu tu tu dien:')
for tu in ds_list:
    print(tu)
