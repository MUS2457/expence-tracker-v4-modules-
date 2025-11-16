def input_data() :

    expences = {}

    while True :

        name = input(" name of the product,'done' to calaculate or 'exit' to quit : ")

        if name.lower().strip() == 'exit' :
            print(" the program has been stopped .")
            break
        if name.lower().strip() == 'done' :
            break
        if name == "" :
            print("enter a name .")
            continue
                
        category = input(f"the category of {name} : ").strip()

        if category == "" :
            print("enter a valid category name.")
            continue
           
        try :
            price = int(input(f"the price of {name} from the category {category} : "))
            
            if price < 0 :
                print("the price can't be negative .")
                continue
        except ValueError :
            print("enter a valid price !")
            continue

        expences[name] = {"category" : category, "price" : price}

    return expences