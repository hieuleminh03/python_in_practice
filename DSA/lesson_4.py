
class menu:
    mon_xh_nhieu_nhat = None
    
    def __init__(self) -> None:
        self.so_mon = 0
        self.ds_mon_an = []
        
    def them_mon(self, mon_moi):
        self.so_mon += 1
        self.ds_mon_an.append(mon_moi)
        
    def tim_mon(self, mon_can_tim):
        '''
        tra ve 1 neu tim thay, 0 neu ko tim thay
        '''
        for mon in self.ds_mon_an:
            if mon.ten == mon_can_tim.ten:
                return mon
            
        return None
        
    def xoa_mon_an(self, mon_can_xoa):
        '''
        neu co mon can xoa thi xoa mon do, in ra "xoa thanh cong"
        khong thi in ra "xoa that bai"
        '''
        if self.tim_mon(mon_can_xoa):
            self.ds_mon_an.remove(self.tim_mon(mon_can_xoa))
            print("xoa thanh cong")
        else:
            print("xoa that bai")
            
        
        
class mon_an:
    
    gia_trubg_binh = None
    gia_dat_nhat = None
    
    def __init__(self, ten) -> None:
        self.ten = ten
        self.size = None
        self.gia = None
        
if __name__ == "__main__":
    mon_1 = mon_an("tra sua")
    mon_2 = mon_an("tra chanh")
    mon_3 = mon_an("kem")
    mon_4 = mon_an("tra dao")
    mon_5 = mon_an("sua chua")
    mon_6 = mon_an("tra o long")
    
    
    menu_1 = menu()
    menu_1.them_mon(mon_1)
    menu_1.them_mon(mon_2)
    menu_1.them_mon(mon_3)
    menu_1.them_mon(mon_4)
    menu_1.them_mon(mon_5)
    menu_1.them_mon(mon_6)
    
    # mon_7 = mon_an("kem")
    
    # if menu_1.tim_mon(mon_7):
    #     print(menu_1.tim_mon(mon_7).ten)
    # else:
    #     print("ko tim dc")
    
    
    mon_8 = mon_an("tra chanh")
    menu_1.xoa_mon_an(mon_8)
    
x = 1
y = 2
z = 3

l = [x,y,z]

del x

print(l)