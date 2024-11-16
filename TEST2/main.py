# import MYMATH.operations as MO

# if __name__=="__main__":
#     kind=input("請輸入使用的溫度類型, 1:攝氏, 2:華式")
#     if kind=="1":
#         nuM=int(input("請輸入攝式溫度:"))
#         print(f"{nuM}degree C即華式{MO.CC_to_FF(nuM):.2f}degree F")
#     else:
#         nuM=int(input("請輸入華式溫度:"))
#         print(f"{nuM}degree C即攝式{MO.FF_to_CC(nuM):.2f}degree C")

# import random
# import MYMATH.FOOD as MF

# random.choice(MF.food)

# import MYMATH
# with open("MYMATH/123.txt","r",encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())


import MYMATH
import random
def lunch():
    foods=[]

    with open("MYMATH/123.txt","r",encoding="utf-8") as file:
        for line in file:
            foods.append(line.strip())
          
    result=random.choice(foods)
    return result
    
print(lunch())


