import math

#Входные данные # 1:
""" point_drive = {'A': (1, 1), 'B': (10, 10)}


total_orders = [
    
        {'A': (1, 3), 'B': (8, 8)},
        {'A': (2, 2), 'B': (2, 2)},
       {'A': (3, 3), 'B': (3, 3)},
         {'A': (1, 1), 'B': (9, 9)},
        {'A': (4, 4), 'B': (4, 4)}

       ]
 """
#Входные данные # 2:

point_drive = {'A': (62.0281, 129.7325), 'B': (62.0354, 129.7339)}

total_orders = [
          {'A': (62.0328, 129.7342), 'B': (62.0341, 129.7317)},
          {'A': (62.0294, 129.7355), 'B': (62.0362, 129.7309)},
          {'A': (62.0301, 129.7319), 'B': (62.0346, 129.7362)},
          {'A': (62.0312, 129.7293), 'B': (62.0275, 129.7398)},
          {'A': (62.0333, 129.7338), 'B': (62.0269, 129.7354)}] 
         

print(f'Доступные заказы: {len(total_orders)}.')

def distance(point1, point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

distances_A = []
for order in total_orders:
    dist_A = distance(order['A'], point_drive['A'])
    distances_A.append(dist_A)

print("Тестовые данные для проверки:", distances_A )

count = int(input('Сколько заказов вы хотите взять? '))

indexes = sorted(range(len(distances_A)), key=lambda k: distances_A[k])[:count]
selected_orders = [total_orders[i] for i in indexes]

for order in selected_orders:
    if distance(order['A'], point_drive['A'])>distance(point_drive['A'],order['B']) and distance(order['B'], point_drive['B'])>distance(order['B'], point_drive['A']):
        print(f'К сожелению нету заказов по пути, но мы предлагаем самый близкий заказ Точка А ({order["A"][0]}, {order["A"][1]}), Точка Б ({order["B"][0]}, {order["B"][1]})')
    else:
        print(f'Заказ по пути Точка А ({order["A"][0]}, {order["A"][1]}), Точка Б ({order["B"][0]}, {order["B"][1]})')
