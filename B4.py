class Stack:
    def __init__(self, dung_luong):
        self.dung_luong=dung_luong
        self.stack= []
        self.top =-1 
    def isEmpty(self):
        return self.top ==-1
    def isFull(self):
        return self.top >= self.dung_luong- 1
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
    def __del__(self):
        print("Đối tượng Stack đã bị huỷ.")
dung_luong= 9
ngam_xep= Stack(dung_luong)
for i in range(dung_luong+1): 
    ngam_xep.push(float(i))
for i in range(dung_luong+1): 
    print(f"Phần tử lấy ra: {ngam_xep.pop()}")