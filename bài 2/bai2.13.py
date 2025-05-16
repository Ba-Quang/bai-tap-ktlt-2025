print("sinh vien: Nguyễn Bá Quảng")
print("Mssv: 235752020710045")
import math

# Nhập hệ số a, b, c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Kiểm tra nếu a = 0
if a == 0:
    if b != 0:
        # Giải phương trình bậc nhất bx + c = 0
        x = -c / b
        print(f"Phương trình là bậc nhất. Nghiệm là: x = {x:.2f}")
    else:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
else:
    # Tính delta
    delta = b**2 - 4*a*c
    print(f"Delta = {delta:.2f}")

    # Phân loại nghiệm dựa trên giá trị của delta
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép: x = {x:.2f}")
    else:
        print("Phương trình vô nghiệm.")

