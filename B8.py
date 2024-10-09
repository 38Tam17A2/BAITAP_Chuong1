class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day=day
        self.month=month
        self.year=year
    def display(self):
        print(f"Ngày: {self.day}/{self.month}/{self.year}")
    def next(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day +=1
class Employee:
    def __init__(self, name, ngay_sinh, ngay_vao_cty):
        self.name = name
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cty = ngay_vao_cty
    def display(self):
        print(f"Họ tên: {self.name}")
        print("Ngay sinh:", end="")
        self.ngay_sinh.display()
        print("Ngày vào công ty: ", end="")
        self.ngay_vao_cty.display()
if __name__ == "__main__":
    ngay_sinh = Date(16, 4, 2005)
    ngay_vao_cty = Date(11, 9, 2018)
    Employee = Employee("Tăng Đức Hải", ngay_sinh, ngay_vao_cty)
    Employee.display()