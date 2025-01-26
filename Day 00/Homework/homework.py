
# 1. მოცემული 3 მთელი a, b, c ̸= 0 რიცხვებისთვის მოძებნეთ a და b რიცხვებს შორის მოხვედრილი c რიცხვის ჯერადი რიცხვების რაოდენობა ყველა შესაძლო ვარიანტისთვის. თუ რომელიმე a, b-დან ჯერადია c-ს, მაშინ ჩათვალეთ შესაბამისი საზღვარი. მოიფიქრეთ ამოცანის ამოხსნის ალგორითმი, დაწერეთ და გაუშვით პროგრამა ციკლის და რეკურსიის (აგრეთვე range) კონსტრუქციის გამოყენების გარეშე.

def count_multiples(a, b, c):
    if c == 0:
        return 0 
    if a <= b:
        start = a
        end = b
    else:
        start = b
        end = a
    multiples_up_to_end = end // c
    multiples_up_to_start = (start - 1) // c
    count = multiples_up_to_end - multiples_up_to_start
    return count

print(count_multiples(6, 30, 3))


