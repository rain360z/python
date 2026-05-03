
age = 100
# проход в парк. до 4 беслпатно. с 4 до 18 цена 25$. С 18 40$

if age < 4:
    price  = 0
#    print("You admission coast is 0$")
elif age < 18:
#    print("you admission coast is 25$")
    price  =  25
else:
#    print(" You admission coast is 40$")
    price  = 40

print(f"You admission coast is ${price}") 

