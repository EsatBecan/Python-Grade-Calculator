yil = 2025
dogumyili = int(input("Hangi yılda doğdunuz?:\n"))
gelecek = int(input("Kaç yıl sonrasını hesaplamak istersiniz:?\n"))

yas = yil - dogumyili
sinif = yas - 5
baslangicyili = dogumyili + 6
unisinif = yas - 17
geleceksinif = sinif + gelecek
gelecekyas = yas + gelecek
gelecekunisinif = gelecekyas - 17

print("Şuanki yaşınız", yas ,"." , gelecek , "Yıl sonra", gelecekyas, "Yaşında olacaksınız\n")

if 0 < sinif <= 12:
	print("Şuanda" , sinif , ". Sınıftasınız, Okula" , baslangicyili , "yılında başladınız\n")
elif 1 > sinif:
	kalanyil = 6 - yas
	print("Okula başlamamışsınız, Okula başlamanıza" , kalanyil, "Kadar yıl var\n")
elif 18 >= sinif > 12:
	unisinif = yas - 17
	print("Üniversite", unisinif, ". sınıftasınız\n")
elif sinif > 18:
	gecenyil = unisinif - 6
	print("Üniversiteden mezun olalı" , gecenyil , "sene olmuş\n")


if 0 < geleceksinif <= 12:
	print(gelecek, "Yıl sonra" , geleceksinif , ". Sınıfta olacaksınız, Okula" , baslangicyili , "yılında başladınız\n")
elif 1 > geleceksinif:
	gelecekkalanyil = 6 - gelecekyas
	print("Okula başlamamışsınız, Okula başlamanıza" , gelecekkalanyil, "Kadar yıl var\n")
elif 18 >= geleceksinif > 12:
	gelecekunisinif = gelecekyas - 17
	print(gelecek, "Yıl sonra Üniversite", gelecekunisinif, ". sınıfta olacaksınız\n")
elif geleceksinif > 18:
	gelecekgecenyil = gelecekunisinif - 6
	print(gelecek, "Yıl sonra Üniversiteden mezun olalı" , gelecekgecenyil , "sene olmuş olacak\n")
  
