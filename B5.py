class NgamXep:
    def __init__(self, dung_luong):
        """Hàm khởi tạo để thiết lập ngăn xếp với dung lượng tối đa"""
        self.dung_luong = dung_luong  # Dung lượng tối đa của ngăn xếp
        self.stack = []  # Mảng động để lưu trữ các phần tử
        self.top = -1  # Chỉ số của phần tử đỉnh, ban đầu là -1 (ngăn xếp trống)
    def isEmpty(self):
        """Kiểm tra ngăn xếp có rỗng không"""
        return self.top == -1
    def isFull(self):
        """Kiểm tra ngăn xếp đã đầy chưa"""
        return self.top >= self.dung_luong - 1
    def push(self, value):
        """Đưa một phần tử vào ngăn xếp"""
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử!")
        else:
            self.stack.append(value)  # Thêm phần tử vào ngăn xếp
            self.top += 1  # Cập nhật chỉ số đỉnh
            print(f"Đã thêm {value} vào ngăn xếp.")
    def pop(self):
        """Lấy một phần tử ra từ đỉnh ngăn xếp"""
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử!")
            return None
        else:
            value = self.stack.pop()  # Lấy phần tử từ đỉnh ngăn xếp
            self.top -= 1  # Cập nhật lại chỉ số đỉnh
            print(f"Đã lấy {value} ra khỏi ngăn xếp.")
            return value
    def count(self):
        """Trả về số phần tử hiện có trong ngăn xếp"""
        return self.top + 1  # Số phần tử là top + 1
    def __del__(self):
        """Hàm huỷ: giải phóng bộ nhớ khi đối tượng bị huỷ"""
        print("Đối tượng NgamXep đã bị huỷ.")
# Ví dụ sử dụng
dung_luong = 5
ngam_xep = NgamXep(dung_luong)    
# Thêm các phần tử vào ngăn xếp
for i in range(dung_luong):
    ngam_xep.push(float(i))
print(f"Số phần tử hiện có trong ngăn xếp: {ngam_xep.count()}")
# Thử lấy nhiều hơn số phần tử
for i in range(dung_luong + 1):
    print(f"Phần tử lấy ra: {ngam_xep.pop()}")
print(f"Số phần tử hiện có trong ngăn xếp: {ngam_xep.count()}")