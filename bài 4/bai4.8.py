# Nhập một dãy các từ từ bàn phím
S = input("Nhập dãy các từ (các từ cách nhau bởi khoảng trắng): ")

# Tách các từ thành danh sách
words = S.split()

# Tìm độ dài lớn nhất trong danh sách các từ
max_length = max(len(word) for word in words)

# Lọc ra các từ có độ dài lớn nhất
longest_words = [word for word in words if len(word) == max_length]

# In kết quả
print("Từ dài nhất:")
print(" ".join(longest_words))
