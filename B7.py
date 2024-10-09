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
if __name__ == "__main__":
    date = Date(27, 11, 2024)
    print("Ngày  hiện tại: ")
    date.display()
    date.next()
    print("Ngày tiếp theo:")
    date.display()
    
        