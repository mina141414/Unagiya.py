
n = int(input("店の座席数"))
m = int(input("来店したグループ数"))

seat_list = [0] * n



for i in range(m):
    a_i = int(input("グループの人数"))
    b_i = int(input("そのグループの座る初期位置"))

    if  not 1 in seat_list[b_i-1:a_i+b_i-1]:
        seat_list[b_i-1:a_i+b_i-1] = [1] * a_i


print(seat_list.count(1))

