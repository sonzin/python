import random
SoLanQuay  = 0
SoLanNgua = 0
SoLanSap = 0

MaxLanQuay = int(input('Nhập số lần quay: '))
while SoLanQuay < MaxLanQuay:
    KetQua = random.randrange(0,2)
    if KetQua == 0:
        SoLanNgua = SoLanNgua + 1
    else: SoLanSap = SoLanSap + 1
    SoLanQuay = SoLanQuay + 1
print('Tổng số lần quay là ',SoLanQuay,'. SỐ lần ngửa là: ',SoLanNgua,'. Số lần sấp là: ',SoLanSap)
