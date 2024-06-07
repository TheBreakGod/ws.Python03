def calculate_change(fare, payment):
    if payment <= fare:
        return "จำนวนเงินที่ต้องจ่ายต้องมากกว่าค่าโดยสาร"

    
    change = payment - fare
    coins = [10,5,2,1]
    change_dict = {10:0,5:0,2:0,1:0}
    
    for coin in coins:
       if change >= coin :
        change_dict[coin] = change // coin
        change %= coin
        

    return  change_dict 


def display_change(change_dict):
    for coin, count in change_dict.items():
        if count > 0:
            print(f"เหรียญ {coin} บาท: {count} เหรียญ")

fare = int(input("ใส่ค่าตั๋ว"))
payment = int(input("ใส่จำนวนเงินที่จะจ่าย"))
change_dict = calculate_change(fare, payment)
display_change(change_dict)

