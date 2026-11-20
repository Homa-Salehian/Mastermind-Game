import random #کتابخانه برای تولید عدد تصادفی


def ramz():#تابع برای تولید رمز تصادفی

    lst=[]
    while len(lst) < 4 :
        r = random.randrange(1,7)
        if r not in lst:
            lst.append(r)
          
    return lst

def hads_ramz():#تابع برای دریافت حدس رمز کاربر
    
    while True:
        number = input("چهار عدد بین 1 تا 6  وارد کنید")

        if len(number) != 4 :
            print("عدد 4 رقمی وارد کنید")
            continue

        flag = True
        for ch in number:
            if ch < '1' or ch > '6':
                flag = False
                break

        if not flag:
            print("ورودی نامعتبر: فقط ارقام 1 تا 6.")
            continue

        hads = []
        for ch in number:
            hads.append(int(ch))

        tekrar = False
        for i in range(4):
            for j in range(i + 1, 4):
                if hads[i] == hads[j]:
                    tekrar = True
                    break
        if tekrar:
            print("ارقام غیر تکراری وارد کنید")
            continue

        return hads
    


def compare(hads , lst ):

    wrong = 0
    right = 0

    for i in range(4):
        if hads[i]==lst[i]:
            right+=1
                
        elif hads[i] in lst:
            wrong+=1    
    return right, wrong


    

def main():#تابع اصلی بازی 

    print("Homa Salehian")# اطلاعات برنامه نوبس
    print("404130933")

    lst = ramz()

    chance = 10

    while chance > 0:
        print("فرصت باقی‌مانده:", chance)

        hads = hads_ramz()

        right , wrong = compare(hads, lst )
        print("تعداد ارقام درست در مکان درست:", right)
        print("تعداد ارقام درست در مکان اشتباه:", wrong)
        chance -= 1


        if right == 4:
            print("برنده شدی")
            print("فرصت باقی‌مانده:", chance)
            return
    
    if chance == 0 and right != 4:
        print("شما باختید")
        print("رمز:", lst)

main()