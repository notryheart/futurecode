f = open("%ПУТЬ К ФАЙЛУ%")

#Открываем файл
lines = [list(map(int, c.split(';'))) for c in f]

#Свои условия