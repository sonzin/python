price = input('Nhập giá sản phẩm vào đây em: ')
paid=input('Nhập vào đây số tiền khách trả: ')
change = float(paid)-float(price)
print('Trả lại khách hàng số tiền là: ', change)
if (change < 0):
    print('Khách trả thiếu tiền rồi em')
elif (change >500):
    print('Anh trả thừa nhiều quá, em ko có tiền trả lại')
elif(change <=500 and change >=100):
    print('Chờ tí em trả lại cho')
