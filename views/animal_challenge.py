# CH_ANIMALS = [
#     {
#         "id": 1,
#         "name": "Snickers",
#         "species": "Dog",
#         "customerId": 4
#     },
#     {
#         "id": 2,
#         "name": "Brixton",
#         "species": "Dog",
#         "customerId": 1
#     },
#     {
#         "id": 3,
#         "name": "Blue",
#         "species": "Cat",
#         "customerId": 5
#     },
#     {
#         "id": 4,
#         "name": "Micky",
#         "species": "Mouse",
#         "customerId": 2
#     },
#     {
#         "id": 5,
#         "name": "Scooby",
#         "species": "Dog",
#         "customerId": 6
#     },
#     {
#         "id": 6,
#         "name": "Jack",
#         "species": "Rabbit",
#         "customerId": 3
#     },
#     {
#         "id": 7,
#         "name": "Winston",
#         "species": "Dog",
#         "customerId": 3
#     },
#     {
#         "id": 8,
#         "name": "Goofy",
#         "species": "Dog",
#         "customerId": 6
#     },
#     {
#         "id": 8,
#         "name": "Daisy",
#         "species": "Cat",
#         "customerId": 1
#     },
#     {
#         "id": 10,
#         "name": "Minnie",
#         "species": "Mouse",
#         "customerId": 2
#     },
#     {
#         "id": 11,
#         "name": "Scruffy",
#         "species": "Dog",
#         "customerId": 3
#     },
#     {
#         "id": 12,
#         "name": "Lucky",
#         "species": "Rabbit",
#         "customerId": 2
#     }
#     # {
#     #     "id": 1,
#     #     "name": "Snickers",
#     #     "species": "Dog",
#     #     "customerId": 4
#     # },
#     # {
#     #     "id": 2,
#     #     "name": "Brixton",
#     #     "species": "Dog",
#     #     "customerId": 1
#     # },
#     # {
#     #     "id": 3,
#     #     "name": "Blue",
#     #     "species": "Cat",
#     #     "customerId": 5
#     # },
#     # {
#     #     "id": 4,
#     #     "name": "Micky",
#     #     "species": "Mouse",
#     #     "customerId": 2
#     # },
#     # {
#     #     "id": 5,
#     #     "name": "Scooby",
#     #     "species": "Dog",
#     #     "customerId": 6
#     # },
#     # {
#     #     "id": 6,
#     #     "name": "Jack",
#     #     "species": "Rabbit",
#     #     "customerId": 3
#     # }
# ]


# CH_CUSTOMERS = [
#     {
#         "id": 1,
#         "name": "Grace",
#         "age": 24
#     },
#     {
#         "id": 2,
#         "name": "Josh",
#         "age": 18
#     },
#     {
#         "id": 3,
#         "name": "Jeff",
#         "age": 37
#     },
#     {
#         "id": 4,
#         "name": "Jamal",
#         "age": 41
#     },
#     {
#         "id": 5,
#         "name": "Megan",
#         "age": 28
#     },
#     {
#         "id": 6,
#         "name": "Caroline",
#         "age": 64
#     }
# ]

# def get_pairings():

#     for ch_customer in CH_CUSTOMERS:
#         for ch_animal in CH_ANIMALS:
#             if ch_customer["id"] == ch_animal["customerId"]:
#                 print(f"{ch_customer['name']} owns {ch_animal['name']}")

# get_pairings()

# def new_pairings():

#     for ch_customer in CH_CUSTOMERS:
#         print(f"{ch_customer['name']}s animals are- ")

#         for ch_animal in CH_ANIMALS :
#             if ch_animal["customerId"] == ch_customer["id"]:
#                 print(f" - {ch_animal['name']} ({ch_animal['species']})")
# new_pairings()
