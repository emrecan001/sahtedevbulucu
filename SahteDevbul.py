import os
#bu bir sahte dev bulucu programdır
#kodlama Emrecan Ayas 
#fikir Borosmozroklo 

def sahtedev():
    s1 = input("Daha önce hiç sosyal medyada IDE resmi atıp sahte devler nerde diye sordunuzmu ?[E/H] ")
    if (s1=="E") or (s1=="e"):
        print("Siz çok taşaklı bir devsiniz tebrikler")
    elif(s1=="H") or (s1 =="h"):
        print("Siz bir dev değilsiniz ve asla olamayacaksınz!!!!!!")


sahtedev()
os.system("pause")
