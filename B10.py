class Diem:
    def __init__(self, x, y):
        self.x = x  # Tọa độ x
        self.y = y  # Tọa độ y
class Elip(Diem):
    def __init__(self, x, y, ban_kinh_a, ban_kinh_b):
        Diem.__init__(self, x, y)
        self.ban_kinh_a = ban_kinh_a  # Bán kính theo chiều dài
        self.ban_kinh_b = ban_kinh_b  # Bán kính theo chiều rộng
    def tinh_dien_tich(self):
        return 3.14 * self.ban_kinh_a * self.ban_kinh_b
class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        Elip.__init__(self, x, y, ban_kinh, ban_kinh)  # Bán kính a và b bằng nhau
# Ví dụ sử dụng
diem = Diem(0, 0)
print(f"Tọa độ điểm: ({diem.x}, {diem.y})")
elip = Elip(0, 0, 5, 3)
print(f"Diện tích elip: {elip.tinh_dien_tich()}")
duong_tron = DuongTron(0, 0, 4)
print(f"Diện tích đường tròn: {duong_tron.tinh_dien_tich()}")