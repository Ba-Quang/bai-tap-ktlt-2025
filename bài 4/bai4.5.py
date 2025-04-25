# Nhập danh sách các từ từ bàn phím
S = input("Nhập danh sách các từ (các từ cách nhau bởi dấu cách): ")

# Tách các từ thành danh sách
words = S.split()

# Đảo ngược thứ tự của danh sách
reversed_words = words[::-1]

# In ra các từ theo thứ tự ngược lại
print("Các từ theo thứ tự ngược lại:")
print(" ".join(reversed_words))
