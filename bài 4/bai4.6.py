# Nhập họ và tên từ bàn phím
full_name = input("Nhập họ và tên (chỉ gồm một âm cho họ và tên riêng): ")

# Tách phần họ và tên riêng
parts = full_name.split()
if len(parts) == 2:
    ho = parts[0]       # Phần họ
    ten_rieng = parts[1]  # Phần tên riêng

    # In kết quả
    print("Họ:", ho)
    print("Tên riêng:", ten_rieng)
else:
    print("Hãy nhập đúng định dạng: một họ và một tên riêng, ví dụ: 'Nguyen Van'")
