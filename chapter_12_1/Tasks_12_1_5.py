# import json
# import random
#
#
# def generate_users(first_names, last_names, cities):
#     while True:
#         user = {
#             "first_name": random.choice(first_names),
#             "last_name": random.choice(last_names),
#             "age": random.choice(range(18, 66)),
#             "city": random.choice(cities)
#         }
#         yield user
#
# if __name__ == "__main__":
#     cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
#     first_names = ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah']
#     last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson']
#
#     users = generate_users(first_names, last_names, cities)
#
#     user_group1 = [next(users) for i in range(4)]
#     user_group2 = [next(users) for i in range(6)]
#
#     print('User group #1')
#     print(json.dumps(user_group1, indent=4))
#     print('User group #2')
#     print(json.dumps(user_group2, indent=4))
