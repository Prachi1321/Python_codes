class kovid:
    def display(self):
        print("mai hu dadaji")
class keesu(kovid):
    def poma(self):
        print("Mai apne papa jesa hu")
class peesu(keesu):
    def show(self):
        print("nahi nahi mai hu apne dadaji jesa")
p=peesu()
p.display()
p.poma()
p.show()