def TinhVAT(giagoc):
    vat = int(giagoc) / 1.1
    return int(vat)

giagoc=input('Nhập số tiền vào đây em: ')
print(TinhVAT(giagoc))
