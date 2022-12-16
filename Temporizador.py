import time

t = input("Digite o tempo (em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada Invalida!")
    quit()

while t:
    minutes, seconds = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer)
    time.sleep(1)
    t = t - 1

print("Tempo acabou!")