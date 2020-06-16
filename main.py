import random, pygame

pygame.init()
win = pygame.display.set_mode((1500, 750))
pygame.display.set_caption("Village")
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
musicstop = False

def music_load():
    if not musicstop:
        music = random.randint(1, 7)
        if music == 1:
            pygame.mixer.music.load('music/Kevin_Macleod_-_Angevin_70.mp3')
        elif music == 2:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_Bushwick_Tarentella.mp3')
        elif music == 3:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_Cattails.mp3')
        elif music == 4:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_Miris_Magic_Dance.mp3')
        elif music == 5:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_Pippin_the_Hunchback.mp3')
        elif music == 6:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_Temple_of_the_Manes.mp3')
        elif music == 7:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_Thatched_Villagers.mp3')
        pygame.mixer.music.play()

def music_night_load():
    if not musicstop:
        music = random.randint(1, 4)
        if music == 1:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_For_Originz.mp3')
        elif music == 2:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_Rites.mp3')
        elif music == 3:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_Ritual.mp3')
        elif music == 4:
            pygame.mixer.music.load('music/Kevin_MacLeod_-_Unanswered_Questions.mp3')
        pygame.mixer.music.play()

music_load()

scaffolds = []
farms = []
villagers = []
giants = []

destroyed = 0
day = True
sky = (128,206,255)
run = False
time = 3000
fail = 0

class scaffold:
    def __init__(self, cen_x, cen_y, override=''):
        self.cen_x = cen_x
        self.cen_y = cen_y
        self.override = override
        self.height = 180
        self.width = 20
        self.colour = (136, 140, 141)
        self.random_factor = random.randint(1, 40)
        self.random_factor_2 = random.randint(1, 20)
        self.state = 1
        self.build_time = 500 + random.randint(-150, 150)
        self.collapse = 0
        self.ruined = False
        if override == "True":
            self.cen_x = 750 - 15
            self.height = 300
            self.width = 30
            self.random_factor = 100

    def ruin_check(self):
        if self.ruined:
            self.state = 4
            self.build_time = 1000
            self.colour = (47, 79, 79)

    def draw(self):
        if self.state < 5:
            pygame.draw.rect(win, (150, 75, 0), (self.cen_x - 30 - self.random_factor, 650 - self.height, self.width, self.height))
            pygame.draw.rect(win, (150, 75, 0), (self.cen_x + 30 + self.random_factor, 650 - self.height, self.width, self.height))
            pygame.draw.rect(win, (150, 75, 0), (self.cen_x - 30 - self.random_factor, round(650 - self.height / 2), 60 + self.random_factor * 2, self.width))
            pygame.draw.rect(win, (150, 75, 0), (self.cen_x - 30 - self.random_factor, 650 - self.height + 20, 60 + self.random_factor * 2, self.width))
        if self.state > 1:
            pygame.draw.rect(win, self.colour, (self.cen_x - 30 - self.random_factor, 650 - round(self.height / 3), (self.random_factor * 2) + 60 + self.width, round(self.height / 3)))
        if self.state > 3:
            pygame.draw.rect(win, self.colour, (self.cen_x - 30 - self.random_factor, 650 - round(2 * (self.height / 3)) - round(self.height / 5), (self.random_factor * 2) + 60 + self.width, round(self.height / 5)))
        if self.state > 2:
            pygame.draw.rect(win, self.colour, (self.cen_x - 30 - self.random_factor, 650 - round(2 * (self.height / 3)), (self.random_factor * 2) + 60 + self.width, round(self.height / 3)))
            if self.override == "True":
                pygame.draw.rect(win, (0, 0, 0), (self.cen_x - 10, 650 - 100, 50, 100))
            else:
                pygame.draw.rect(win, (0, 0, 0), (self.cen_x - 5, 650 - 70, 35, 70))
        if self.state > 4:
            if self.override == "True":
                pygame.draw.line(win, (151, 80, 22), (self.cen_x - 20 - self.random_factor - 100, 650 - self.height + 70), (self.cen_x + 10, 650 - self.height + 30), 70)
                pygame.draw.line(win, (161, 90, 30), (self.cen_x + 10, 650 - self.height + 30), (self.cen_x + 40 + self.random_factor + 100, 650 - self.height + 70), 70)
            else:
                pygame.draw.line(win, (151, 80, 22), (self.cen_x - 20 - self.random_factor - 40, 650 - self.height + 70), (self.cen_x + 10, 650 - self.height + 30), 70)
                pygame.draw.line(win, (161, 90, 30), (self.cen_x + 10, 650 - self.height + 30), (self.cen_x + 40 + self.random_factor + 40, 650 - self.height + 70), 70)


class farm:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 30
        self.width = 200
        self.stored = 1
        self.life = 100

    def feed(self):
        for vill in villagers:
            if self.stored > 0:
                if not vill.fed:
                    vill.fed = True
                    vill.food_time = 800
                    self.stored -= 1
            make = random.randint(1, 4000)
            if make == 7:
                if vill.fed:
                    print("FEED")
                    vill.fed = True
                    vill.food_time = 800
                else:
                    print("Stored")
                    self.stored += 1

    def draw(self):
        pygame.draw.rect(win, (228, 204, 104), (self.x, 650 - self.height, self.width, self.height))


class villager:
    def __init__(self, x, y, knight=''):
        self.x = x
        self.y = y
        self.height = 65
        self.width = 30
        self.size = random.randint(1, 20)
        self.redness = 90
        self.colour = (90, 50, 0)
        self.face = random.randint(-1, 2)
        self.knight = knight
        self.start = False
        if self.knight == "True":
            self.life = 4000
        else:
            self.life = 2000
        self.fed = True
        self.food_time = 500
        self.knight = knight
        if self.face < 1:
            self.face = -1
        else:
            self.face = 1
        self.dir_amount = 650 + random.randint(-200, 200)
        self.direction = self.dir_amount * self.face

    def move(self):
        #Checking for end of screen collision
        if self.knight == "True" and len(giants) > 0:
            if not self.start:
                self.attack = random.randint(0, len(giants) - 1)
                self.start = True
            try:
                test = giants.index(giants[self.attack])
            except IndexError:
                print("ERROR")
                self.attack = random.randint(0, len(giants) - 1)
            if self.x < giants[self.attack].x + giants[self.attack].width / 2:
                self.x += random.randint(1, 2)
            if self.x > giants[self.attack].x + giants[self.attack].width / 2:
                self.x -= random.randint(1, 2)
            if self.x == giants[self.attack].x + giants[self.attack].width / 2:
                giants[self.attack].life -= 1
            if giants[self.attack].life < 1:
                giants.remove(giants[self.attack])
                if len(giants) > 1:
                    self.attack = random.randint(0, len(giants) - 1)
                else:
                    self.attack = 0
        else:
            if self.x <= 0:
                self.face = self.face * -1
                self.direction = self.dir_amount * self.face
            if self.x + self.width >= 1500:
                self.face = self.face * -1
                self.dir_amount = 650 + random.randint(-200, 200)
                self.direction = self.dir_amount * self.face
            #Going left
            if self.face == 1:
                if self.direction > 0:
                    move = random.randint(1, 3)
                    self.x -= move
                    self.direction -= move
                else:
                    self.face = self.face * -1
                    self.direction = self.dir_amount * self.face
            #Going right
            else:
                if self.direction < 0:
                    move = random.randint(1, 3)
                    self.x += move
                    self.direction += move
                else:
                    self.face = self.face * -1
                    self.dir_amount = 650 + random.randint(-200, 200)
                    self.direction = self.dir_amount * self.face
            #Bugfix
                if self.x < 5:
                    self.x += 10
                if self.x + self.width >= 1505:
                    self.x -= 10

    def die(self):
        if self.fed:
            self.food_time -= 1
            if self.knight != "True":
                if self.life < 2000:
                    self.life += 0.3
                    if self.redness > 90:
                        self.redness -= 0.1
            else:
                if self.life < 4000:
                    self.life += 0.5
                    if self.redness > 90:
                        self.redness -= 0.1
        if self.food_time < 1:
            print(self.life)
            self.fed = False
            self.life -= 1
            if self.redness < 255:
                self.redness += 0.1
        if self.life < 1:
            villagers.remove(self)



    def draw(self):
        if self.knight != "True":
            self.colour = (self.redness, 50, 0)
        else:
            self.colour = (110, 110, 110)
        if day or self.knight == "True":
            pygame.draw.rect(win, self.colour, (self.x, 650 - self.height, self.width, self.height))
            pygame.draw.circle(win, (255, 229, 204), (round(self.x + self.width / 2), 650 - self.height - 30), 20)
        if self.knight == "True":
            pygame.draw.polygon(win, self.colour, ((self.x - 20, 650 - self.height - 35), (self.x - 20, 650 - self.height - 45), (self.x + round(self.width / 5), 650 - self.height - 60), (self.x + 4 * round(self.width / 5), 650 - self.height - 60), (self.x + self.width + 20, 650 - self.height - 45), (self.x + self.width + 20, 650 - self.height - 35)))


class giant():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 140
        self.width = 80
        self.life = 500
        if len(farms) > 0:
            self.attack = random.randint(0, len(farms) - 1)
        else:
            self.attack = -1

    def move(self):
        if len(farms) > 0:
            if self.attack == -1:
                self.attack = random.randint(0, len(farms) - 1)
            try:
                test = farms.index(farms[self.attack])
            except IndexError:
                print("ERROR")
                self.attack = random.randint(0, len(farms) - 1)
            if self.x < farms[self.attack].x - (self.width / 2) + farms[self.attack].width / 2:
                self.x += random.randint(1, 2)
            if self.x > farms[self.attack].x - (self.width / 2) + farms[self.attack].width / 2:
                self.x -= random.randint(1, 2)
            if self.x == farms[self.attack].x - (self.width / 2) + farms[self.attack].width / 2:
                farms[self.attack].life -= 1
            if farms[self.attack].life < 1:
                farms.remove(farms[self.attack])
                if len(farms) > 1:
                    self.attack = random.randint(0, len(farms) - 1)


    def draw(self):
        pygame.draw.rect(win, (0, 0, 0), (self.x, 650 - self.height, self.width, self.height))
        pygame.draw.circle(win, (255, 229, 204), (round(self.x + self.width / 2), 650 - self.height - 50), 42)


def build(plot):
    plot.build_time -= 1
    if plot.build_time == 0:
        plot.state += 1
        plot.build_time = 500 + random.randint(-150, 150)

def create():
    chance = random.randint(0, (2000 - (len(villagers) * 20)))
    if len(villagers) < 15:
        if len(villagers) > 0:
            if chance == 4:
                print("EGG")
                spot = random.randint(0, 1)
                if spot == 1:
                    scaffolds.append(scaffold(random.randint(10, 650), 0))
                else:
                    scaffolds.append(scaffold(random.randint(850, 1400), 0))
                milita = random.randint(1, 8)
                if milita == 3:
                    villagers.append(villager(740, 0, "True"))
                else:
                    villagers.append(villager(740, 0))

def build_farm():
    hungry = 0
    for vill in villagers:
        if not vill.fed:
            hungry += 1
    if random.randint(1, 3000) in range(1, hungry * 2):
        farms.append(farm(random.randint(100, 1300), 0))

def ruin():
    global destroyed, fail
    if len(scaffolds) - destroyed > len(villagers) - 1:
        choice = random.randint(0, len(scaffolds) - 1)
        if scaffolds[choice].override != "True" and not scaffolds[choice].ruined:
            scaffolds[choice].ruined = True
            destroyed += 1
        elif len(scaffolds) > 1:
            fail += 1
            if fail < 100:
                ruin()

def timer():
    global day, sky, run, time
    time -= 1
    if time < 0 and day:
        day = False
        music_night_load()
    if time < -3000:
        music_load()
        day = True
        time = 3000

    if day:
        sky = (128,206,255)
    else:
        sky = (12, 20, 69)
    print(time)

def giant_maker():
    if not day:
        spawn = random.randint(1, 10000)
        if spawn in range(1, 2 + len(villagers)):
            side = random.randint(1, 2)
            if side == 1:
                giants.append(giant(1500 + random.randint(10, 120), 0))
            else:
                giants.append(giant(-80 - random.randint(10, 100), 0))
    else:
        for gia in giants:
            giants.remove(gia)

def draw_window():
    global sky
    win.fill(sky)
    pygame.draw.rect(win, (37, 127, 25), (0, 650, 1500, 100))

    timer()
    create()
    giant_maker()
    build_farm()
    fail = 0
    ruin()
    for scaf in scaffolds:
        scaf.ruin_check()
        build(scaf)
        scaf.draw()
        #scaf.age()
    for gia in giants:
        gia.move()
        gia.draw()
    for vil in villagers:
        vil.die()
        vil.move()
        vil.draw()
    for farm in farms:
        farm.feed()
        farm.draw()

    pygame.display.update()

scaffolds.append(scaffold(100, 100, "True"))
villagers.append(villager(600, 0))
villagers.append(villager(950, 0))

timer()
run = True
while run:
    clock.tick(60)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            scaffolds.append(scaffold(mouse_x, mouse_y))
            if random.randint(1, 8) == 2:
                villagers.append(villager(mouse_x, mouse_y, "True"))
            else:
                villagers.append(villager(mouse_x, mouse_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        for i in farms:
            farms.remove(i)
    if keys[pygame.K_0]:
        for a in villagers:
            a.life = 2000
            a.fed = True
            a.food_time = 800
            a.redness = 90
    if keys[pygame.K_m]:
        musicstop = True
        pygame.mixer.music.stop()

    draw_window()

pygame.quit()