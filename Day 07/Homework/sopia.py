# 3) ამოხსენით ამოცანა: კუნძულზე ცხოვრობს 2 კატეგოორის ხალხი: ზარმაცები და ბეჯითები. ბეჯითები თავს თვითონ იპარსავენ, ზარმაცებს კი თმას პარსავს პარიკმახერი. დაადგინეთ ვინ არის პარიკმახერი ბეჯითი თუ ზარმაცი.

# ამის პასუხი არ არსებობს, რადგან ბეჯითები თვითონ იპარსავენ თავს, ზარმაცები კი პარიკმახერებს აპარსინებენ. არის გამორიცხული, რომ პარიკმახერი ან ზარმაცი იყოს ან თუნდაც ბეჯითი? არა. შესაბამისად პასუხი არ არსებობს.





# 1) შექმენით პროგრამა, რომელიც მიიღებს ნებისმიერ პოზიციურ სისტემაში მყოფ რიცხვსა და სასურველ პოზიციურ სისტემას, რომელშიც გადაიყვანს მიღებულ რიცხვს

def funct(str):
    str = str.replace(".", " ")
    strlist = str.split(" ")
    list = []
    for i in range(len(strlist)):
        list.append(int(strlist[i], 2))
    str2 = ""
    for i in range(len(list)):
        str2 += chr(list[i] + 96)
    return str2

print(funct("11101.1.1110 11001.1111.10101 10010.101.1.100 10100.1000.1001.10011.110101"))

print(funct("100011.110 11001.1111.10101 11.1.1110 10010.101.1.100 10100.1000.1001.10011.110111 10100.1000.1.10100 1101.101.1.1110.10011 11001.1111.10101 1.1100.10010.101.1.100.11001 111.1111.10100 110.1111.10101.10010 111.10010.101.101.1110 11.1.10010.100.10011.110110"))

print(funct("100110.1001.110.101 1001.10011 1100.1001.1011.101 10010.1001.100.1001.1110.111 1 10.1001.11.11001.11.1100.101.110110 101110.1111 1011.101.101.10000 11001.1111.10101.10010 10.1.1100.1.1110.11.101.110111 11001.1111.10101 1101.10101.10011.10100 1011.101.101.10000 1101.1111.10110.1001.1110.111.110110"))

print(funct("101110.10010.10101.10011.10100 1101.101.110111 100.1111.1110.111001.10100 10010.101.1.100 10100.1000.101 1100.1.10011.10100 10011.101.1110.10100.101.1110.11.101.110110"))

print(funct("100011.110 11001.1111.10101 1101.1.100.101 10100.1000.1001.10011 110.1.10010.110111 100001.101001.11011.111001.10011 100110.101.1.100.101.10010.111001.10011 11101.1111.1110.10100.10010.1111.1100.1100 11110.101.10000.1.10010.10100.1.1101.101.1110.10100 10111.1001.1100.1100 111.1001.10110.101 11001.1111.10101 10100.101.1110 111.10010.101.101.1110 11.1.10010.100.10011 1.110.10100.101.10010 11001.1111.10101 10011.101.1110.100 1.1100.1100 1111.110 10100.1000.1001.10011 10100.101.11000.10100.10011 10100.1111 11110.1.10100.1 11110.1001.1.10011.1.1101.1001.100.11010.101 1001.1110 100111.101.10011.10011.101.1110.111.101.10010 1.1110.100 10100.1000.101.10010.101 10111.1111.1110.111001.10100 10.101 1.1110.11001 1101.1001.10011.10100.1.1011.101.10011.110110"))