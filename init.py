class JSS:
    def __init__(self):
        self.name = input('이름: ')
        self.age = input('나이: ')
        # print("JSS 클래스 선언! ")
    def show(self):
        print("나의 이름은 {}, 나이는 {}세 입니다.".format(self.name, self.age))

# a = JSS()
# a.show()

class JSS2(JSS):
    def __init__(self):
        super().__init__()
        self.gender = input('성별: ')
    def show(self):
        print("나의 이름은 {}, 나이는 {}, 성별은 {} 입니다.".format(self.name, self.age, self.gender))
        
b = JSS2()
b.show()