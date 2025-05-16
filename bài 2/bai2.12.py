print("sinh vien: Nguyễn Bá Quảng")
print("Mssv: 235752020710045")
import re

# Hàm kiểm tra tính hợp lệ của mật khẩu
def kiem_tra_mat_khau(mk):
    if (6 <= len(mk) <= 12 and
        re.search(r'[a-z]', mk) and
        re.search(r'[A-Z]', mk) and
        re.search(r'\d', mk) and
        re.search(r'[$#@]', mk)):
        return True
    return False

# Nhập vào các mật khẩu
nhap_mk = input("Nhập các mật khẩu, phân tách bởi dấu phẩy: ")
ds_mat_khau = nhap_mk.split(',')

# Kiểm tra và in các mật khẩu hợp lệ
mat_khau_hop_le = [mk for mk in ds_mat_khau if kiem_tra_mat_khau(mk)]
print("Mật khẩu hợp lệ:", ",".join(mat_khau_hop_le))
