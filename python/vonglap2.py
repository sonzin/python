def TongTien(target):
    total = 0
    next = 1
    while next <= target:
        total = total + next
        next = next + 1
    return total
answer = input('Nhập số vào đi em: ')
answer = int(answer)
print(TongTien(answer))
