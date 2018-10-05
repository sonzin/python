import random
while True:
    giagoc = input("Vui lòng nhập giá: ")
    thitruong = input("Vui lòng nhập thị trường: ")
    if thitruong == "CN":
        giaban = int(giagoc) * 3600 + random.randrange(50000,90000)
    elif thitruong == "UK":
        giaban = int(giagoc) * 33500 + 20000 + random.randrange(3000,40000)
    elif thitruong == "ES":
        giaban = int(giagoc) * 30000 + random.randrange(3000,40000)
    print("Vậy giá bán hoặc đăng là ", giaban)
