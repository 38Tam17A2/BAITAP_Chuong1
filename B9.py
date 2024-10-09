class DaGiac:
    def __init__(self, so_dinh, canh):
        self.so_dinh = so_dinh
        self.canh = canh  # Danh sách các cạnh
    def tinh_chu_vi(self):
        chu_vi = 0
        chu_vi += self.canh[0] * (self.so_dinh > 0)
        chu_vi += self.canh[1] * (self.so_dinh > 1)
        chu_vi += self.canh[2] * (self.so_dinh > 2)
        chu_vi += self.canh[3] * (self.so_dinh > 3)
        return chu_vi
    def tinh_dien_tich(self):
        return 0  
class HinhBinhHanh(DaGiac):
    def __init__(self, canh_a, canh_b, chieu_cao):
        DaGiac.__init__(self, 4, [canh_a, canh_a, canh_b, canh_b])
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.chieu_cao = chieu_cao
    def tinh_dien_tich(self):
        return self.canh_a * self.chieu_cao
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        HinhBinhHanh.__init__(self, chieu_dai, chieu_rong, chieu_rong)
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        HinhChuNhat.__init__(self, canh, canh)
# Ví dụ sử dụng
hinh_vuong = HinhVuong(4)
print(f"Chu vi hình vuông: {hinh_vuong.tinh_chu_vi()}")
print(f"Diện tích hình vuông: {hinh_vuong.tinh_dien_tich()}")
hinh_binh_hanh = HinhBinhHanh(5, 10, 4)
print(f"Chu vi hình bình hành: {hinh_binh_hanh.tinh_chu_vi()}")
print(f"Diện tích hình bình hành: {hinh_binh_hanh.tinh_dien_tich()}")
hinh_chu_nhat = HinhChuNhat(5, 3)
print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.tinh_chu_vi()}")
print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.tinh_dien_tich()}")