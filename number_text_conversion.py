numbers_dict = {0:"",1:" one ",2:" two ",3:" three ",
                4:" Four ",5:" five ",6:" six ",7:" seven ",
                8:" eight ",9:" nine "}
sindex_dict = {1:" ten ",2:" twenty ",3:" thirteen ",
                4:" Forty ",5:" fifty ",6:" sixty ",7:" seventy ",
                8:" eighty ",9:" ninty "}
place_dict = {-3:"Hundred", -4:"thousand"}

number = int(input("Enter your number : "))
digits = []
while number>0:
    digits.append(number%10)
    number=int(number/10)

digits= digits[::-1]
print(numbers_dict[digits[-4]]+place_dict[-4]+
      numbers_dict[digits[-3]]+place_dict[-3]+
      sindex_dict[digits[-2]]+
      numbers_dict[digits[-1]])


