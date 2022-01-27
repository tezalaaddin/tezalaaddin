#O(N) Complexity
def reverse_string(word):
    #Word degiskeni bittiyse
    if  word == "":
        return word
    #Hala word degiskeni dolu ise
    else:
        return reverse_string(word[1:]) + word[0]

#Programın main kısmı
if __name__ == "__main__":
    #Kullanıcıdan veri alma
    word2 = input('Bir metin giriniz:')
    #Alınan veriyi işleme ve ekrana yazdırma
    print('Çıktı:', reverse_string(word2))
