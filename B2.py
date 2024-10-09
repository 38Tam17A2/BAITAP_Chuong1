class thisinh:
    def __init__(self, ho_ten="",diem_toan=0,diem_ly=0, diem_hoa=0):
        self.ho_ten=ho_ten
        self.diem_toan=diem_toan
        self.diem_ly=diem_ly
        self.diem_hoa=diem_hoa
    def nhap_thong_tin(self):
        self.ho_ten =input("nhập họ tên thí sinh: ")
        self.diem_toan=float(input("nhập điểm Toán: "))
        self.diem_ly =float(input("nhập điểm Lý: "))
        self.diem_hoa= float(input("nhập điểm Hoá: "))
    def tinh_tong_diem(self):
        return self.diem_toan +self.diem_ly +self.diem_hoa
    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán:{self.diem_toan}")
        print(f"Điểm Lý:{self.diem_ly}")
        print(f"Điểm Hoá: {self.diem_hoa}")
        print(f"Tổng điểm:{self.tinh_tong_diem()}")
danh_sach_thi_sinh = []
so_luong =int(input("nhập số lượng thí sinh: "))
for i in range(so_luong):
    thi_sinh= thisinh()
    thi_sinh.nhap_thong_tin()
    danh_sach_thi_sinh.append(thi_sinh)