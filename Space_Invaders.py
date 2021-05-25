from pyb import SPI, Pin, LED, delay, UART




class Starship_S:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin

class Aliens_Pnj:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin

class Bullet_B:
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin

    def erase(self):
        move(self.x,self.y)
        uart.write(" "*len(self.skin))

    def move_up(self):
        self.erase()
        self.y -= 1
        if self.y>0:
            self.y-=1
            move(self.x, self.y)
            uart.write(self.skin)
            
        else :
            bullet_group.remove(self)
        
precision = 300
led1 = LED(1)
led2 = LED(2)
led3 = LED(3)
led4 = LED(4)
monstres = []
uart = UART(2, 115200)
size_width = 300
size_height = 50
xcoo=60
starship = Starship_S(x=size_width//2-5, y=50, skin="I_/A\\_I")
alien1 = Aliens_Pnj(x = xcoo, y=9, skin="[-0-]")
alien2 = Aliens_Pnj(x = 65, y=15, skin="!\\U/!")
alien3 = Aliens_Pnj(x = xcoo, y=21, skin=".-0-.")
push_button = pyb.Pin("PA0", pyb.Pin.IN, pyb.Pin.PULL_DOWN)
bullet = Bullet_B(x = starship.x+3, y = starship.y+1, skin = ":")
bullet_group = []
CS = Pin("PE3", Pin.OUT_PP)

SPI_1 = SPI(
    1,  # PA5, PA6, PA7
    SPI.MASTER,
    baudrate=50000,
    polarity=0,
    phase=0,
    # firstbit=SPI.MSB,
    # crc=None,
)
def read_reg(addr):
    CS.low()
    SPI_1.send(addr | 0x80)  # 0x80 pour mettre le R/W à 1
    tab_values = SPI_1.recv(1)  # je lis une liste de 1 octet
    CS.high()
    return tab_values[0]


def write_reg(addr, value):
    CS.low()
    SPI_1.send(addr | 0x00)  # write
    SPI_1.send(value)
    CS.high()


def convert_value(high, low):
    value = (high << 8) | low
    if value & (1 << 15):
        # negative number
        value = value - (1 << 16)
    return value * 2000 / 32768


def read_acceleration(base_addr):
    low = read_reg(base_addr)
    high = read_reg(base_addr + 1)
    return convert_value(high, low)

def clear_screen():
    uart.write("\x1b[2J\x1b[?25l")

def move(x, y):
    uart.write("\x1b[{};{}H".format(y, x))

def xpos():
    x_accel = read_acceleration(0x28)
    return x_accel >= precision

       
def xneg():
    x_accel = read_acceleration(0x28)
    return x_accel <= -precision

def add_bullet():
    bullet_group.append(Bullet_B(x=starship.x+3, y=starship.y+1, skin=":"))



 


if __name__ == "__main__":

    addr_who_am_i = 0x0F
    print(read_reg(addr_who_am_i))
    addr_ctrl_reg4 = 0x20
    write_reg(addr_ctrl_reg4, 0x77)
clear_screen()

#for i in range(10):
#        invaders.append(alien1.skin)
#        invaders.append("     ")
#uart.write(invaders)
led3.on()
compteur = 0 

while alien1.x < 270:
    move(alien1.x, alien1.y)
    uart.write(" "+alien1.skin+" ")
    alien1.x += 10

while alien2.x < 265:
    move(alien2.x, alien2.y)
    uart.write(" "+alien2.skin+" ")
    alien2.x += 10

while alien3.x < 270:
    move(alien3.x, alien3.y)
    uart.write(" "+alien3.skin+" ")
    alien3.x += 10

while(True):

    compteur += 1
    #print(starship.x, starship.y)

    

    if compteur % 1000 == 0:
        led4.toggle()

   
    

    

    if xpos() == True and starship.x < 290:
        led2.off()
        led3.off()
        led1.on()
        starship.x+=1
        move(starship.x, starship.y)
        
        uart.write(" "+starship.skin+" ")
        delay(30)

    elif xneg() == True and starship.x > 50:
        led2.on()
        led1.off()
        led3.off()
        starship.x-=1
        move(starship.x, starship.y)
        
        uart.write(" "+starship.skin+" ")
        delay(30)

    while(True):       
        for bullet in bullet_group:
                bullet.move_up()  
    
        if push_button.value() == 1 and len(bullet_group) < 15 :
            add_bullet()
            delay(20)
        break
        
        


