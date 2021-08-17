def groceries(product1,product2):
    vegetables=[]
    fruits=[]
    salad=[]
        
    prod=[product1,product2]
    if product1=="Mango" or product2=="Mango":
        fruits.append(product1)
        print(fruits)
    elif product1=="Potato" or product2=="Potato":
        vegetables.append(product1)
        print(vegetables)
    elif product1=="Potato":
        elif product2=="Mango":
        salad.extend(product1,product2)
        print(salad)
    # elif product1=="Mango" and product2=="Potato":
    #     salad.extend(product1,product2)
    #     print(salad)
groceries("Mango","Potato")
groceries("Mango","Mango")








    
        
    



