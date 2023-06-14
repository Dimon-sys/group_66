items = [
    {
        "name":"Iphone 9",
        "price":45_000,
        "brand":"Apple"
    },
    {
        "name":"Galaxy A50",
        "price":38_000,
        "brand":"Samsung"
    },
    {
        "name":"3310",
        "price":0,
        "brand":"Nokia"
    },
    {
        "name":"M 12",
        "price":20_000,
        "brand":"Xiaomi"
    }
]
from pprint import pprint
pprint(items)
print(*items, sep='\n')

def get_price(item):
    return item.get('price')


pprint(sorted(items, key=lambda i: i.get("price")))


#my_numbers = ['1','2','3','4','5']
#print(my_numbers[0] + "1")
#my_map = map(int, my_numbers)
#my_new_map = list(my_map)
#print(my_new_map[0] + 1)

