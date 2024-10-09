class PS:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
    def kiem_tra_hop_le(self):
        return self.mau_so !=0
    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
    def in_phan_so(self):
        print(f"Phân số:{self.tu_so}/{self.mau_so}")
Phan_so = PS()
Phan_so.nhap_phan_so()
Phan_so.in_phan_so()
    
        