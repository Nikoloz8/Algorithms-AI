#დაამტკიცეთ, რომ min(f) <= E(f) <= max(f);

#შევქმნათ 4 წევრიანი სია, რომლის მიხედვითაც დავამტკიცებთ ზემოთ მოცემულ პირობას.


list = [1, 2, 3, 4]

#ვიპოვოთ მინიმალური მნიშვნელობა ამ სიიდან

def min(list): #აქ შევქმენი მარტივი min ფუნქცია forloop - ის დახმარებით
    min = list[0]
    for i in range(len(list)):
        if min > list[i]:
            min = list[i]
    return min

print(min(list))


def max(list): #აქ შევქმენი მარტივი max ფუნქცია forloop - ის დახმარებით
    min = list[0]
    for i in range(len(list)):
        if min < list[i]:
            min = list[i]
    return min

print(max(list))

def excepted(list): #აქ შევქმენი მარტივი excepted ფუნქცია forloop - ის დახმარებით, რომელიც პოულობს საშუალოს
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum / len(list)

print(excepted(list))

print(min(list) <= excepted(list) <= max(list)) #True

#სიაში რა მნიშვნელობებიც არ უნდა შევიტანოთ, ზემოთ მოცემული პირობა ყოველთვის True იქნება, რადგან სიაში მინიმალური რიცხვი ყოველთვის ნაკლები იქნება მაქსიმალურ რიცხვზე (რასაც სიტყვა გვეუბნება). რაც შეეხება საშუალოს, იგი არის სიაში რიცხვთა ჯამის შეფარდება მათ რაოდენობასთან, სიაში ფაქტობრივად შუა რიცხვის როლი აქვს, შესაბამისად იგი ყოველთვის მეტი იქნება სიაში მინიმალურ რიცხვზე და ნაკლები იქნება მაქსიმალურ რიცხვზე.