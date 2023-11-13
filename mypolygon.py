import turtle
import math

# 1. square fonksiyonu
def square(t, length):
    for _ in range(4):
        t.forward(length)
        t.left(90)

# Bob adında bir turtle oluşturun
bob = turtle.Turtle()

# square fonksiyonunu çağırın
square(bob, 100)

# Ek olarak "length" için farklı değerlerle programı test edebilirsiniz.

# 2. square fonksiyonuna "length" parametresi eklendi.

# 3. polygon fonksiyonu
def polygon(t, n, length):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.left(angle)

# 4. circle fonksiyonu
def circle(t, r):
    circumference = 2 * math.pi * r
    length = circumference / 360  # Her derece için gerekli uzunluk
    n = 360  # Daireyi yaklaşık olarak 360 kenarla çiziyoruz
    polygon(t, n, length)

# "circle" fonksiyonunu farklı "r" değerleriyle test edin.
circle(bob, 50)

# 5. arc fonksiyonu
def arc(t, r, angle):
    circumference = 2 * math.pi * r
    length = circumference / 360  # Her derece için gerekli uzunluk
    n = int(360 * angle / 360)  # Belirtilen açıya göre kenar sayısı
    polygon(t, n, length)

# "arc" fonksiyonunu farklı "r" ve "angle" değerleriyle test edin.
arc(bob, 50, 90)  # 90 derecelik bir kesit çizin

turtle.done()  # Pencereyi kapatmak için

