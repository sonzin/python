total= int(input('Tổng giá trị hợp đồng: '))
payment1 = int(input('Thanh toán lần 1: '))
payment2 = int(input('Thanh toán lần 2: '))
payment3 = int(input('Thanh toán lần 3: '))
rate = int(input('Nhập tỉ giá USD/VND: '))
checktrue= payment1+payment2+payment3
def tinhtoangiatricaclan(total):     
    print('Thanh toán lần 1 sẽ là: ',total*int(payment1)/100,'. Quy đổi VNĐ:',total*int(payment1)/100*rate)
    print('Thanh toán lần 2 sẽ là: ',total*int(payment2)/100,'. Quy đổi VNĐ:',total*int(payment2)/100*rate)
    print('Thanh toán lần 3 sẽ là: ',total*int(payment3)/100,'. Quy đổi VNĐ:',total*int(payment3)/100*rate)
    
if checktrue == 100:
    tinhtoangiatricaclan(total)
else: print('Vui lòng check lại số liệu phần trăm')


