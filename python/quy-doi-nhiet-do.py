f=int(input('Nhập độ F vào đây: '))
def convert(tempf):
    c = (f-32) * (5/9)
    return c
print('Nhiệt độ quy đổi là: ',convert(f))
