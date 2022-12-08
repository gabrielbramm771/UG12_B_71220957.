print("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG")
a =int(input("Masukan Angka:"))
b=1
c=8
for i in reversed(range(10)):
    for j in range(i+1):
        print(' ', end='')
    for k in range(b+1):
        if k==1:
            print('*', end='')
        else:
            print(' ', end='')
    for l in range(b):
        if l==c:
            print('*', end='')
            c+=8
        else:
            print(' ', end='')
    b+=1
    print()
for i in range(11):
    print('* ', end='')