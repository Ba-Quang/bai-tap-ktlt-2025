print("Nguyễn Bá Quảng")
print("MSSV:235752020710045")

class Nguoi(object):
    def getGender(self):
        return "Unknown"
class Nam(Nguoi):
    def getGender(self):
        return("Nam")
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())
