#倍数最靠近10000的数
a=0.000001

import time
time_start=time.time()

if a >=10000:
    print("your RawNumber is",a)
    print("数字超过一万了")
elif a<=0:
    print("your RawNumber is",a)
    print("不行哦")
else:
    print("your RawNumber is",a)
    b=1
    fir=1
    c=a*fir  
    while c<10000:
        fir=fir+1
        b=b+1
        c=a*fir
    if  c==10000:
            print("Luck Number!")
            print ("Gold multiple is:",b)
            print ("Gold result is:",c)
            print("ReportOver,&倍数最靠近10000的数")
    elif c>10000:
        xc=c-10000
        sed=fir-1
        d=sed*a
        xd=10000-d
        if xc>xd:
            b=b-1
            sed=fir
            c=d
            print("multiple:",b)
            print("result:",c)
            print("ReportOver,&倍数最靠近10000的数")
        elif xc<xd:
            print("multiple:",b)
            print("result:",c)
            print("ReportOver,&倍数最靠近10000的数")
        else:
            print("Fault,you MOTHEHFUVKRT!")
  
time_end=time.time()
time_c=time_end - time_start
print("运算时间：",time_c,"秒")
    





   


