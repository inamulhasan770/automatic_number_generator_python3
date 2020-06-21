import threading


def m1():
    with open ('list.txt','a') as f:
        for i in range(0, 9999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')
        
def m2():
    with open ('list.txt','a') as f:
        for i in range(10000000, 19999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')

def m3():  
    with open ('list.txt','a') as f:
        for i in range(20000000, 29999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')

def m4():
    with open ('list.txt','a') as f:
        for i in range(30000000, 39999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')

def m5():
    with open ('list.txt','a') as f:
        for i in range(40000000, 49999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')

def m6():
    with open ('list.txt','a') as f:
        for i in range(50000000, 59999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')

def m7():
    with open ('list.txt','a') as f:
        for i in range(60000000, 69999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')

def m8():
    with open ('list.txt','a') as f:
        for i in range(70000000, 79999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')

def m9():
    with open ('list.txt','a') as f:
        for i in range(80000000, 89999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')

def m10():
    with open ('list.txt','a') as f:
        for i in range(90000000, 99999999):
            k = str(i)
            dig = k.zfill(8)
            f.write(str(dig)+'\n')


if __name__ == "__main__":
     t1 = threading.Thread(target=m1)
     t2 = threading.Thread(target=m2)
     t3 = threading.Thread(target=m3)
     t4 = threading.Thread(target=m4)
     t5 = threading.Thread(target=m5)
     t6 = threading.Thread(target=m6)
     t7 = threading.Thread(target=m7)
     t8 = threading.Thread(target=m8)
     t9 = threading.Thread(target=m9)
     t10 = threading.Thread(target=m10)


     t1.start()
     t2.start()
     t3.start()
     t4.start()
     t5.start()
     t6.start()
     t7.start()
     t8.start()
     t9.start()
     t10.start()

     t1.join()
     t2.join()
     t3.join()
     t4.join()
     t5.join()
     t6.join()
     t7.join()
     t8.join()
     t9.join()
     t10.join()

     print("Completed")
