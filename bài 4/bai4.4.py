S = input("Nhap danh sach (cac phan tu cach nhau boi dau trong hoac tab): ")
elements = S.split()  # Tách các phần tử bằng khoảng trắng hoặc dấu tab
print("Danh sach vua nhap:")
for element in elements:
    print(element)
