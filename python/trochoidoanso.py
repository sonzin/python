import random
songaunhien = random.randrange(0,10)
solandoan = 0
while solandoan < 5:
    khachdudoan = int(input('Nhập số dự đoán đi anh: '))
    if songaunhien == khachdudoan:
        print('Anh đoán chuẩn quá')
        break
    else:
        print('Sai rồi gõ lại đi anh')
        solandoan = solandoan + 1
