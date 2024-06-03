class MyClass:

    def test(self):
        self.p1 = 'name1'
        self.p2 = 'name2'
        self.mesod(self.p1,self.p2)
        

    def mesod(self,p1,p2):
        print(f'{p1} and {p2}')

MyClass().test()
