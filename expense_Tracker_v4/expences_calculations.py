def tl_expences(expences_dic) :
    if expences_dic :

        total_expences = sum(item['price'] for item in expences_dic.values())

        return {"total price" :total_expences}
    
def tl_per_category(expences_dic) :
    total_category = {}

    if expences_dic :
        for item,info in expences_dic.items() :

            cat_egory = info["category"]
            pri_ce    = info["price"]

            if cat_egory not in total_category :

                total_category[cat_egory]  = pri_ce

            else :
                total_category[cat_egory] += pri_ce

        return total_category
    
def top_low_product(expence_dic):
    if expence_dic:
        top = max(expence_dic, key=lambda p: expence_dic[p]["price"])
        low = min(expence_dic, key=lambda p: expence_dic[p]["price"])

        return {
            "most_expensive_product": top,
            "price_of_most_expensive": expence_dic[top]['price'],
            "cheapest_product": low,
            "price_of_cheapest": expence_dic[low]['price']
        }

def budget_limit(expense_dic, budget=50000): # monthly budget
    if not expense_dic:
        return None

    total_expenses = sum(item['price'] for item in expense_dic.values())

    if total_expenses <= budget:
        return f"Within the budget. Total expenses: {total_expenses} yen."
    else:
        over_amount = total_expenses - budget
        return f"Over the budget by {over_amount} yen. Total expenses: {total_expenses} yen."
