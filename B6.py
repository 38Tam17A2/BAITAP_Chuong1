class Stack:
    def __init__(self, dung_luong):
        self.dung_luong = dung_luong
        self.stack = []
        self.top = -1 
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top >= self.dung_luong - 1
    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử!")
        else:
            self.stack.append(value)
            self.top += 1
            print(f"Đã thêm {value} vào ngăn xếp.")
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử!")
            return None 
        else:
            value = self.stack.pop() 
            self.top -= 1 
            return value
    def count(self):
        return self.top + 1  
    def print_stack(self):
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung của ngăn xếp (từ đỉnh xuống đáy):")
            for i in range(self.top, -1, -1):
                print(self.stack[i])
    def __del__(self):
        print("Đối tượng Stack đã bị huỷ.")
dung_luong = 16
ngam_xep = Stack(dung_luong)
for i in range(dung_luong):
    ngam_xep.push(float(i))
ngam_xep.print_stack()
for i in range(dung_luong + 1):
    print(f"Phần tử lấy ra: {ngam_xep.pop()}")
ngam_xep.print_stack()