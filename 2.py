seconds = int(input('Введите целое число: '))
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print('{:d}:{:02d}:{:02d}'.format(h, m, s))
print(f'{h:d}:{m:02d}:{s:02d}')
########################################################
time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")