import random
MAX_GUESS = 5
RANGE = 20

print('Bạn có tổng cộng ',MAX_GUESS,' lần dự đoán')
print('Chọn các số từ 1 đến',RANGE)

target = random.randrange(1,MAX_GUESS + 1)
khachdudoan = 0
solandoan = 0
while True:
    khachdoan = int(input('Nhập vào số dự đoán đi anh: '))
    if target == int(khachdoan):
        print('Anh đoán chuẩn đấy ạ')
        break
    elif target < khachdoan:
        solandoan = solandoan + 1
        print('Anh chọn hơi cao')
    elif target > khachdoan:
        solandoan = solandoan + 1
        print('Anh chọn hơi thấp')
    if solandoan == MAX_GUESS:
        print('hết lượt chơi rồi a')
        break
print('cám ơn anh đã chơi')
