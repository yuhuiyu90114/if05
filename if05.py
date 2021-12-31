pwd = 'a123456'
i =3
while i>0:
    user = input ('請輸入密碼: ')
    i =i-1
    if user == pwd :
        print ('登入成功')
        break
    else:
        
        print('密碼錯誤! ')
        if i> 0:
            print(' 還有' ,i,'次機會! ')
        else:
            print(' 沒有機會! ')