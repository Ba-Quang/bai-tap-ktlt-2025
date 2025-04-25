# Nhập một chuỗi từ bàn phím
S = input("Nhập một chuỗi: ")

# Loại bỏ tất cả các chữ số khỏi chuỗi
result = ''.join(ch for ch in S if not ch.isdigit())

# In lại nội dung chuỗi mới
print("Chuỗi mới không có chữ số:")
print(result)
