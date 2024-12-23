# List comprehension
list_1 = [n**2 for n in range(5)]
print(list_1)

list_2 = [n for n in range(11) if n % 2 == 0]
print(list_2)

list_3 = []
for i in range(11):
    if i % 2 == 0:
        list_3.append(i)
        print(list_3)
    
print(list_3)

# Dictionary comprehension

languages = ["Python", "Java", "C++", "JavaScript", "PHP"]
dict_1 = {n: len(n) for n in languages}
print(dict_1)

users = [
    {"id": 0, "name": "Andrea", "is_subscribed": True},
    {"id": 1, "name": "Cristian", "is_subscribed": True},
    {"id": 2, "name": "Elizabeth", "is_subscribed": False},
    {"id": 3, "name": "Alejandro", "is_subscribed": True},
]

subscribed_users = {f"id_{users[i]["id"]}": users[i]["name"] for i in range(len(users)) if users[i]["is_subscribed"]}
print( subscribed_users )