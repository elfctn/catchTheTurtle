import turtle
import random
import time # Zaman modülünü ekledim (ileride gerekebilir, şu an kullanılmıyor ama hazır bulunsun)

# Ekranı ayarla
screen = turtle.Screen()
screen.bgcolor('light blue')
screen.title('Catch the Turtle')
screen.setup(width=800, height=800) # Ekran boyutunu belirle
screen.tracer(0) # Animasyonları kapat (manuel güncelleme için)

# Font ayarı
FONT = ('Arial', 20, 'normal') # Font boyutunu biraz küçülttüm, ekrana daha iyi sığar

# Oyun değişkenleri
score = 0
game_over = False

# Kaplumbağa listesi
turtle_list = []

# Skor ve Geri Sayım Kaplumbağaları (objeleri oluşturuyoruz)
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()

# Izgara boyutu (kaplumbağaların yerleşeceği alan için)
grid_size = 15 # Izgara boyutunu biraz artırdım, kaplumbağalar daha ayrık durur

# Skor kaplumbağasını ayarla
def setup_score_turtle():
    score_turtle.hideturtle() # Görünmez yap
    score_turtle.color('dark blue') # Rengini ayarla
    score_turtle.penup() # Çizim yapmamasını sağla

    # Ekranın üst kısmına yerleştir
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setposition(0, y)
    score_turtle.write(arg=f'Score: {score}', move=False, align='center', font=FONT) # F-string ile formatlama

# Tek bir kaplumbağa oluştur ve tıklama olayını bağla
def make_turtle(x, y):
    t = turtle.Turtle() # Yeni bir Turtle objesi oluştur

    # Kaplumbağaya tıklandığında çalışacak fonksiyon
    def handle_click(click_x, click_y): # Tıklama koordinatları argüman olarak gelir
        global score
        # Eğer oyun bitmediyse skoru artır
        if not game_over:
            score += 1
            score_turtle.clear() # Önceki skoru temizle
            score_turtle.write(arg=f'Score: {score}', move=False, align='center', font=FONT) # Yeni skoru yaz

    t.onclick(handle_click) # Tıklama olayını handle_click fonksiyonuna bağla
    t.penup() # Çizim yapmamasını sağla
    t.shape('turtle') # Şeklini kaplumbağa yap
    t.shapesize(2, 2) # Boyutunu ayarla
    t.color('green') # Rengini ayarla
    # Belirtilen koordinatlara git (ızgara boyutunu kullanarak)
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t) # Oluşturulan kaplumbağayı listeye ekle

# Kaplumbağaların yerleşeceği olası koordinatlar.ekran büyüklüğüne oranşadım

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -20]

# Tüm kaplumbağaları ayarla (oluştur)
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

# Tüm kaplumbağaları gizle
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

# Rastgele bir kaplumbağayı göster ve bir süre sonra tekrar gizleyip yenisini göster
def show_turtles_randomly():
    global game_over
    # Eğer oyun bitmediyse devam et
    if not game_over:
        hide_turtles() # Tüm kaplumbağaları gizle
        # Kaplumbağa listesi boş değilse rastgele birini göster
        if turtle_list:
            random.choice(turtle_list).showturtle()
        # Belirli bir süre sonra (500 milisaniye = 0.5 saniye) bu fonksiyonu tekrar çağır
        screen.ontimer(show_turtles_randomly, 500) # Görünme süresini ayarlayabilirim

# Geri sayım fonksiyonu
def countdown(time_left): # Argüman adını 'time_left' olarak değiştirdim, daha açıklayıcı
    global game_over
    countdown_turtle.hideturtle() # Görünmez yap
    countdown_turtle.penup() # Çizim yapmamasını sağla

    # Geri sayım yazısının konumunu ayarla
    top_height = screen.window_height() / 2
    # Skorun biraz altına yerleştirelim
    y = top_height * 0.9 - 40
    countdown_turtle.setposition(0, y)

    # Önceki geri sayım yazısını temizle
    countdown_turtle.clear() # <-- Buradaki argümanı kaldırdık, sadece clear()

    if time_left > 0:
        # Kalan süreyi yaz
        countdown_turtle.write(arg=f'Time: {time_left}', move=False, align='center', font=FONT) # F-string ile formatlama
        # 1 saniye sonra countdown fonksiyonunu kalan süre ile tekrar çağır
        screen.ontimer(lambda: countdown(time_left - 1), 1000)
    else:
        # Süre bitti, oyunu bitir
        game_over = True
        countdown_turtle.clear() # Son geri sayım yazısını temizle
        hide_turtles() # Tüm kaplumbağaları gizle
        # Oyun bitti yazısı
        countdown_turtle.write(arg='Game Over!', move=False, align='center', font=FONT)
        # Oyun bittikten sonra pencerenin kapanmaması için mainloop devam edecek.
        # İstersem burada ek bitiş işlemleri yaparım

# Oyunu başlatan ana fonksiyon
def start_game_up():
    # Oyun kurulumu
    setup_score_turtle() # Skor kaplumbağasını ayarla
    setup_turtles() # Kaplumbağaları oluştur ve ayarla
    hide_turtles() # Başlangıçta tüm kaplumbağaları gizle
    show_turtles_randomly() # Kaplumbağaları rastgele göstermeye başla
    countdown(10) # Geri sayımı başlat (10 saniye)

    # Animasyonları tekrar aç ve ekranı güncelle
    screen.update() # Ekranı bir kez güncelle
    turtle.tracer(1) # tracer'ı 1'e ayarla (normal animasyon hızına dön)


# Oyunu başlatmak için ana fonksiyonu çağır
start_game_up()

# Turtle grafik penceresini açık tut
turtle.mainloop()
