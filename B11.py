class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  # Cạnh a
        self.b = b  # Cạnh b
        self.c = c  # Cạnh c
    def tinh_chu_vi(self):
        return self.a + self.b + self.c
    def tinh_dien_tich(self):
        # Sử dụng công thức Heron để tính diện tích
        p = self.tinh_chu_vi() / 2  # Nửa chu vi
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
class TamGiacCan(TamGiac):
    def __init__(self, canh_bang, canh_khac):
        # Giả sử cạnh b và c bằng nhau
        TamGiac.__init__(self, canh_bang, canh_khac, canh_khac)
    def tinh_dien_tich(self):
        return (self.b * self.c) / 2  # Diện tích tam giác cân
class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        # Tất cả các cạnh đều bằng nhau
        TamGiacCan.__init__(self, canh, canh)
# Ví dụ sử dụng
tam_giac = TamGiac(3, 4, 5)
print(f"Chu vi tam giác: {tam_giac.tinh_chu_vi()}")
print(f"Diện tích tam giác: {tam_giac.tinh_dien_tich()}")
tam_giac_can = TamGiacCan(5, 6)
print(f"Chu vi tam giác cân: {tam_giac_can.tinh_chu_vi()}")
print(f"Diện tích tam giác cân: {tam_giac_can.tinh_dien_tich()}")
tam_giac_deu = TamGiacDeu(6)
print(f"Chu vi tam giác đều: {tam_giac_deu.tinh_chu_vi()}")
print(f"Diện tích tam giác đều: {tam_giac_deu.tinh_dien_tich()}")