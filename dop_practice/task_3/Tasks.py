# import os
#
# def count_files_and_folders(directory: str = None, recursive: bool = False) -> dict:
#     if directory is None:
#         directory = os.path.dirname(os.path.abspath(__file__))
#
#     files_count = 0
#     folders_count = 0
#
#     if recursive:
#         for root, dirs, files in os.walk(directory):
#             files_count += len(files)
#             folders_count += len(dirs)
#     else:
#         with os.scandir(directory) as it:
#             for entry in it:
#                 if entry.is_file():
#                     files_count += 1
#                 elif entry.is_dir():
#                     folders_count += 1
#
#     return {
#         "files": files_count,
#         "folders": folders_count
#     }
#
# # Пример использования функции
# if __name__ == "__main__":
#     directory_path = input("Введите путь до директории (или оставьте пустым для текущей директории): ")
#     if not directory_path:
#         directory_path = None
#
#     recursive_count = input("Выполнять рекурсивный подсчет? (да/нет): ").strip().lower() == "да"
#
#     result = count_files_and_folders(directory_path, recursive_count)
#     print(result)

# def sort_product(arg: list, category=None) -> list:
#     if category is None:
#         return sorted(arg, key=lambda x: x.get('price'), reverse=True)
#     return sorted(filter(lambda x: x.get('category') == category, arg), key=lambda x: x.get('price'), reverse=True)
#
#
# if __name__ == "__main__":
#     products = [
#         {"name": "Apple", "price": 1.2, "category": "Fruits", "quantity": 10},
#         {"name": "Banana", "price": 0.5, "category": "Fruits", "quantity": 20},
#         {"name": "Carrot", "price": 0.7, "category": "Vegetables", "quantity": 15},
#         {"name": "Beef", "price": 5.0, "category": "Meat", "quantity": 5},
#         {"name": "Chicken", "price": 3.0, "category": "Meat", "quantity": 8},
#         {"name": "Orange", "price": 1.5, "category": "Fruits", "quantity": 12},
#     ]
#
#     # Сортировка всех продуктов по убыванию стоимости
#     print(sort_product(products))
#
#     # Сортировка продуктов из категории "Fruits" по убыванию стоимости
#     print(sort_product(products, category="Fruits"))


# def order_analyze(arg):
#     res_dict = {}
#     for el in arg:
#         if el.get("items", 0) != 0:
#             year_month = el.get('date')[:-3]
#             total_order = sum(item['price'] * item['quantity'] for item in el["items"])
#
#             if year_month not in res_dict:
#                 res_dict[year_month] = {
#                     "total_value": 0,
#                     "count_value": 0
#                 }
#             res_dict[year_month]["total_value"] += total_order
#             res_dict[year_month]["count_value"] += 1
#
#     result = {}
#     for year_month, item in res_dict.items():
#         average_order_value = item['total_value'] / item['count_value']
#         result[year_month] = {
#             "average_order_value": average_order_value,
#             "order_count": item['count_value']
#         }
#     return result
#
#
# if __name__ == "__main__":
#     orders = [
#         {
#             "id": 1,
#             "date": "2023-05-15",
#             "items": [
#                 {"name": "item1", "price": 100, "quantity": 2},
#                 {"name": "item2", "price": 50, "quantity": 1}
#             ]
#         },
#         {
#             "id": 2,
#             "date": "2023-05-20",
#             "items": [
#                 {"name": "item3", "price": 200, "quantity": 1},
#                 {"name": "item4", "price": 150, "quantity": 2}
#             ]
#         },
#         {
#             "id": 3,
#             "date": "2023-06-05",
#             "items": [
#                 {"name": "item5", "price": 300, "quantity": 1}
#             ]
#         }
#     ]
#
#     result = order_analyze(orders)
#     print(result)

