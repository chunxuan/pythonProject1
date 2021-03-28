class Bicycle:
    def run(self,miles):
        print(f"骑行了{miles}米，好累啊")

class EBicycle(Bicycle):
    def __init__(self,valume):
        self.valume =valume

    def fill_charge(self,add_valume):
        self.valume = self.valume + add_valume

    def run_e(self,miles):
        erun_miles = self.valume * 10
        if miles - erun_miles>0:
            res_mile = miles - erun_miles
            print(f"电动车骑行了{erun_miles}米")
            super().run(res_mile)
        else:
            print(f"电动车骑行了{miles}米")

ebile = EBicycle(100)
ebile.fill_charge(20)
ebile.run_e(2000)




