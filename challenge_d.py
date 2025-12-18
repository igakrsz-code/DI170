#1

word = input("Enter a word: ")

letter_indexes = {}

for index, letter in enumerate(word):
    if letter in letter_indexes:
        letter_indexes[letter].append(index)
    else:
        letter_indexes[letter] = [index]

print(letter_indexes)


#2

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

wallet_amount = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price_str in items_purchase.items():
    # Clean price string and convert to integer
    price = int(price_str.replace("$", "").replace(",", ""))
    
    # Check if wallet can afford the item
    if wallet_amount >= price:
        basket.append(item)
        wallet_amount -= price  

if basket:
    print(sorted(basket))  
else:
    print("Nothing")
