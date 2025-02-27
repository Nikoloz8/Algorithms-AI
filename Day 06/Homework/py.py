# ⌉  ან  ¬   -   "არა", უარყოფა.

#  ⌉ A - ეს წარმოადგენს ფორმულას და იკითხება, როგორც "არა A"

# თუ A ჭეშმარიტია, მაშინ ⌉ A - არის მცდარი გამონათქვამი.

# ქვემოთ არის ცხრილი, რომელშიც 1 აღნიშნავს ჭეშმარიტ, ხოლო 0 მცდარ გამონათქვამს.

                            # | ----------|
                            # | A  | ⌉ A  |
                            # | ----------|
                            # | 0  |  1   |         -     უარყოფა
                            # | 1  |  0   |
                            # | ----------|

# "და" კავშირი აღინიშნება ”∧” ან ”&” სიმბოლოებით ”სიმბოლოებით და მისი გამოყენება ხდება შემდეგნაირად: თუ A და B ორი ფორმულაა, მაშინ ფორმულაა ჩანაწერი A&B, იკითხება ”A და B”. ფორმულას რომელიც შექმნილია ”და”კავშირის გამოყენებით ეწოდება კონიუქცია და ჭეშმარიტია, როდესაც ჭეშმარიტია ორივე ფორმულა A და B.

# ქვემოთ არის დამადასტურებელი ცხრილი
                            #   |--------------------|        
                            #   | A  |  B  |  A & B  |
                            #   |--------------------|
                            #   | 0  |  0  |    0    |       
                            #   | 0  |  1  |    0    |             -    კონიუქცია
                            #   | 1  |  0  |    0    |
                            #   | 1  |  1  |    1    |
                            #   |--------------------|
                                    
# ”ან” კავშირი აღინიშნება ” ∨ ” სიმბოლოთი და მისი გამოყენება ხდება შემდეგნაირად: თუ თუ A და B ორი ფორმულაა, მაშინ ფორმულაა ჩანაწერი A ∨ B, იკითხება ”A ან B”. ფორმულას, რომელიც შექმნილია ” ან ” კავშირის გამოყენებით ეწოდება დიზიუნქცია და ჭეშმარიტია როდესაც ჭეშმარიტია ერთერთი ფორმულა A ან B


                            #   |--------------------|        
                            #   | A  |  B  |  A ∨ B  |
                            #   |--------------------|
                            #   | 0  |  0  |    0    |
                            #   | 0  |  1  |    1    |       -    დიზიუნქცია
                            #   | 1  |  0  |    1    |
                            #   | 1  |  1  |    1    |
                            #   |--------------------|



# ”გამომდინარეობს”კავშირი აღინიშნება ” ⇒ ”და მისი გამოყენება ხდება შემდეგნაირად: თუ A და B ორი ფორმულაა, მაშინ ფორმულაა ჩანაწერი A ⇒ B, იკითხება ”თუ A მაშინ B” ან ”თუ A-დან გამომდინარეობს B” ან ”როდესაც A მაშინ B”. ფორმულას, რომელიც შექმნილია ”გამომდინარეობს”კავშირის გამოყენებით ეწოდება იმპლიკაცია და მცდარია მხოლოდ მაშინ, როდესაც ჭეშმარიტია პირველი ფორმულა და მცდარია მეორე


                            #   |---------------------|        
                            #   | A  |  B  |  A ⇒ B  |
                            #   |--------------------|
                            #   | 0  |  0  |    1    |
                            #   | 0  |  1  |    0    |       -    იმპლიკაცია
                            #   | 1  |  0  |    1    |
                            #   | 1  |  1  |    1    |
                            #   |--------------------|
                                    
                                    
# ჩანაწერი ”p ⇔ q” წარმოადგენს ”(p ⇒ q)&(q ⇒ p)” ჩანაწერის შემოკლებულ აღნიშვნას. სიმბოლოს ”⇔” ეწოდება ”ექვივალენტობა” და ფორმულებს p და q ეწოდება ექვივალენტური ფორმულები როდესაც p ⇔ q ჭეშმარიტი ფორმულაა. ადვილი შესამჩნევია, რომ p ⇔ q ჭეშმარიტია, როდესაც p და q ფორმულებს ერთნაირი ჭეშმარიტული მნიშვნელობა აქვთ.


# სპეციალურ სიმბოლოს ”=”ეწოდება ”ტოლობა”და მისი დაწერისას ხელმძღვანელობენ შემდეგი წესით: თუ ორ ობიექტს შორის წერია ”=”სიმბოლო, მაშინ ფორმულაში პირველი ობიექტის ნაცვლად მეორე ობიექტის ჩაწერა გვაძლევს საწყისი ფორმულის ექვივალენტურ ფორმულას. ხშირად ექვივალენტურ ფორმულებს შორის წერენ ”=”სიმბოლოს.


                            #   |--------------------------------|        
                            #   | p  |  q  |  [p & (p ⇒ q)]⇒ q  |
                            #   |--------------------------------|
                            #   | 0  |  0  |        1            |
                            #   | 0  |  1  |        1            |       -    დამატებითი ჰიპოთეზის მეთოდი
                            #   | 1  |  0  |        1            |
                            #   | 1  |  1  |        1            |
                            #   |--------------------------------|
                                    
                                    
# ფორმულას ეწოდება ”ტავტოლოგია”(იგივურად ჭეშმარიტი ფორმულა), თუ მისი ჭეშმარიტული მნიშვნელობა ყოველთვის არის 1.


# 1. A ⇒ B = ⌉ A ∨ B 

# A ⇒ B ტოლია ⌜A ∨ B-ს. ამ ტოლობაში ყველაფერი დამოკიდებულია B - ზე, თუ იგი მცდარია, მაშინ გამოსახულების მარცხენა ნაწილის ტოლობისთვის A - ც მცდარი უნდა იყოს, მაგრამ ტოლობის მეორე მხარეს თუ ერთ-ერთი განცხადება მაინც ჭეშმარიტია, მაშინ იგი ჭეშმარიტია. გამომდინარეობის ცხრილის მიხედვით მარცხენა ტოლობის არაჭეშმარიტება მხოლოდ მაშინ შეიძლება მოხდეს, როცა B ჭეშმარიტია, ხოლო A მცდარი. თუ ასე მოხდა მაშინ ტოლობის მარჯვენა მხარე ჭეშმარიტია და მთლიანი გამოსახულება არაჭეშმარიტი გამოდის, რადგან 0 != 1.

# 2. A & B = B & A (კონიუქციის კომუტაციურობა)

# A & B ტოლია B & A. კონიუქციის ცხრილის მიხედვით ამ განცხადებებთა გადანაცვლებით არაფერი იცვლება.

# 3. A ∨ B = B ∨ A (დიზიუნქციის კომუტაციურობა)

# A ∨ B = B ∨ A. დიზიუნქციის ცხრილის მიხედვით ამ განცხადებებთა გადანაცვლებით არაფერი იცვლება.

# 4. (A & B) & C = A & (B & C) (კონიუქციის ასოციაციურობა)

# ეს ტოლობა ყველა შემთხვევაში ჭეშმარიტია, რადგან აქ ერთი განცხადებაც რომ იყოს მცდარი ტოლობის მარცხენა და მარჯვენა გამოსახულებაც არაჭეშმარიტი, ტოლობის დახმარებით კი ჭეშმარიტი გამოდის. მაგალითად, თუ A მცდარია, მაშინ A & B მცდარია, შესაბამისად False & C ყველა შემთხვევაში მცდარია. ამავე დროს განვიხილოთ იგივე შემთხვევისთვის ტოლობის მეორე მხარე, თუ A მცდარია, B & C - ს რა მნიშვნელობაც არ უნდა ჰქონდეს მთელი გამოსახულება მცდარია. ეს ასე იმუშავებს თითოეული წევრის ჭეშმარიტობა/არაჭეშმარიტობისათვის.

# 5. (A ∨ B) ∨ C = A ∨ (B ∨ C) (დიზიუნქციის ასოციაციურობა )

# ეს ტოლობა ჭეშმარიტია, რადგან აქ ჭეშმარიტობისთვის ერთი პირობის ჭეშმარიტობაც საკმარისია, ხოლო არაჭეშმარიტობისთვის კი ყველა განცხადება მცდარი უნდა იყოს. მაგალითად: თუ A მცდარია, მაშინ A V B ჭეშმარიტია და True V C    C - ს ნებისმიერი მნიშვნელობისთვის ჭეშმარიტია. ტოლობის მარჯვენა მხარესაც შესრულდება ზუსტად იგივე მოქმედებები, რაც მთლიან გამოსახულებას აქცევს ჭეშმარიტად.

# 6. A & (B ∨ C) = (A & B) ∨ (A & C) (კონიუქციის დისტრიბუციულობა)

# ეს გამოსახულება ჭეშმარიტია, რადგან რა მნიშვნელობებიც არ უნდა ავიღოთ ამ განცხადებების ადგილას, მარცხენა და მარჯვენა მხარე აუცილებლად ტოლი იქნება.

# 7. A ∨ (B & C) = (A ∨ B) & (A ∨ C) (დიზიუნქციის დისტრიბუციულობა)

# ეს გამოსახულებაც ჭეშმარიტია, რადგან რა მნიშვნელობებიც არ უნდა ავიღოთ ამ განცხადებების ადგილას, მარცხენა და მარჯვენა მხარე აუცილებლად ტოლი იქნება.

# 8. ⌉(A & B) = (⌉A) ∨ (⌉B) (კონიუქციის დე-მორგანის კანონი)

# ეს გამოსახულება ჭეშმარიტია A - სა და B - ს ნებისმიერი მნიშვნელობისთვის, რადგან ტოლობის პირველ ნაწილში თუ ერთი პირობა მაინც მცდარია, მაშინ მთლიანი მარცხენა ნაწილი ჭეშმარიტი გამოდის. იგივე ეხება მარჯვენასაც.

# 9. ⌉(A ∨ B) = (⌉A) & (⌉B) (დიზიუნქციის დე-მორგანის კანონი)

# ზუსტად იგივე, რაც ზემოთ (ოღონდ შებრუნებული)

# 10. ⌉(⌉A) = A

# ეს ტოლობა ჭეშმარიტია, რადგან გვაქვს ორი "არა" რომელიც A - ს ისევ ჩვეულებრივ სახეს უბრუნებს.

# 11. A ∨ A = A

# ეს ტოლობა ჭეშმარიტია, რადგან ორი A - ს "ან" ოპერატორით შედარება მოგვცემს იგივე შედეგს რაც თავად A არის.

# 12. A ∨ & A = A

# იგივე, რაც ზემოთ.

# 13. A & (⌉A) = 0 (წინააღმდეგობის კანონი)

# ტოლობა ჭეშმარიტია, რადგან A - სა და ⌉A - ს შორის ერთ-ერთი აუცილებლად უარყოფითია. "და" ოპერატორით შედარებისას მნიშვნელობა აუცილებლად იქნება 0 (მცდარი)

# 14. A ∨ (⌉A) = 1 (მესამეს გამორიცხვის კანონი)

# ტოლობა ისევ ჭეშმარიტია, რადგან A - სა და ⌉A - ს შორის ერთ-ერთი აუცილებლად ჭეშმარიტია, "ან" ოპერატორით შედარებისას კი მთლიანი ტოლობა გამოდის 1 (ჭეშმარიტი)

# 15. A & 0 = 0

# აქ 0 მცდარ პირობას აღნიშნავს, და ოპერატორით შედარებისას კი 1 - ი პირობაც რომ იყოს მცდარი მთელი გამოსახულება მცდარია.

# 16. A ∨ 0 = A

# გამოსახულება კვლავ ჭეშმარიტია, რადგან A - ს მნიშვნელობაზეა A v 0 გამოსახულების მნიშვნელობა, რომელიც აუცილებლად ისევ A - ს ტოლი იქნება, რადგან მას "ან" ოპერატორით ვადარებთ.

# 17. A & 1 = A

# გამოსახულება კვლავ ჭეშმარიტია, რადგან ისევ A - ს მნიშვნელობაზეა A & 1 გამოსახულების მნიშვნელობა, რომელიც აუცილებლად ისევ A - ს ტოლი იქნება, რადგან მას "და" ოპერატორით ვადარებთ.

# 18. A ∨ 1 = 1

# გამოსახულება კვლავ ჭეშმარიტია, რადგან A - ს რა მნიშვნელობაც არ უნდა ჰქონდეს, A v 1 მაინც = 1.

#დაამტკიცეთ, რომ შემდეგი ჩანაწერები ტავტოლოგიებია

# 19. [p & (p ⇒ q)]⇒ q დასკვნის კანონი

# ეს არის ტავტოლოგია რადგან, თუ p ჭეშმარიტია, მაშინ p ⇒ q ითვალისწინებს, რომ q უნდა იყოს ჭეშმარიტი, რადგან p ⇒ q ნიშნავს, რომ p-ის ჭეშმარიტების შემთხვევაში q უნდა იყოს ჭეშმარიტი. თუ p მცდარია, მაშინ p ∧ (p ⇒ q) იქნებოდა მცდარი და არ არის აუცილებელი q-ის მნიშვნელობა. ასე რომ, საბოლოოდ ყოველთვის ხდება q-ის ჭეშმარიტი.

# 20. p & q ⇒ p “და“-ს მოხსნის კანონი

# ეს ტავტოლოგიაა, რადგან თუ p და q ორივე ჭეშმარიტია, მაშინ p ჭეშმარიტი იქნება, რაც თავად p-ის ჭეშმარიტობის მიხედვით ცხადია.

# 21. p ⇒ p ∨ q “ან“-ის შემოყვანის კანონი

# ეს ტავტოლოგიაა, რადგან თუ p ჭეშმარიტია, მაშინ p ∨ q ყოველთვის იქნება ჭეშმარიტი, რადგან p-ის ჭეშმარიტება საკმარისია p ∨ q-ის ჭეშმარიტებისთვის. თუ p მცდარია, მაშინ q-ის ჭეშმარიტებამ უნდა მოიტანოს p ∨ q-ის ჭეშმარიტება.

# 22. ⌉q & (p ∨ q) ⇒ p “ან“-ის მოხსნის კანონი

# ეს ტავტოლოგიაა, რადგან თუ ⌉q ჭეშმარიტია, p ∨ q მხოლოდ p-ში გადადის. ამრიგად, p უნდა იყოს ჭეშმარიტი.

# 23.  (p ⇒ q) ⇔ (⌉q ⇒⌉p) კონტრაპოზიციის კანონი

# ეს კანონი ავლენს, რომ p ⇒ q და ⌉q ⇒ ⌉p ლოგიკურად ტოლია.

# 24.  (⌉p ⇒ q) & (⌉p ⇒⌉q) ⇒ p საწინააღმდეგოს დაშვების კანონი (წინააღმდეგობამდე მიყვანის მეთოდი)

# ეს კანონი მტკიცედ ავლენს, რომ თუ ⌉p ⇒ q და ⌉p ⇒ ⌉q ჭეშმარიტია, მაშინ p უნდა იყოს ჭეშმარიტი, რადგან წინააღმდეგობა არ შეიძლება იყოს.

# 25. (p ⇒ q) & (q ⇒ r) ⇒ (p ⇒ r) სილლოგიზმი

# ეს ტავტოლოგიაა. თუ p ⇒ q და q ⇒ r, მაშინ p ⇒ r აუცილებლად იქნება ჭეშმარიტი.

# 26. (p ⇔ q) & (q ⇔ r) ⇒ (p ⇔ r) ექვივალენტობის ტრანზიტულობის კანონი

# ეს ტავტოლოგიაა, რადგან თუ p და q ეკვივალენტურია და q და r ეკვივალენტურია, მაშინ p და r აუცილებლად იქნება ეკვივალენტური.

# 27. (p ⇒ r) & (q ⇒ r) ⇒ (p ∨ q ⇒ r) წანამძღვრების შეკრების კანონი

# თუ p ⇒ r და q ⇒ r, მაშინ p ∨ q ⇒ r აუცილებლად იქნება ჭეშმარიტი.

# 28.  (p ⇒ q) & (p ⇒ r) ⇒ (p ⇒ q & r) დასკვნათა გადამრავლების კანონი

# თუ p ⇒ q და p ⇒ r, მაშინ p ⇒ (q & r) აუცილებლად იქნება ჭეშმარიტი.

# 29. p ⇒ (q ⇒ r) ⇔ q ⇒ (p ⇒ r) წანამძღვართა გადანაცვლების კანონი

# ეს ტავტოლოგიაა, რადგან ლოგიკური ურთიერთობა არ იცვლება მიუხედავად იმპლიკაციების გადანაცვლებისა.

