seat_count = 9
vip_seat_array = [4, 7]


# def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
#     count = 0
#     total = 1
#     for i in range(1, total_count + 1):
#         if i not in fixed_seat_array:
#             count += 1
#         else:
#             if count > 0:
#                 total *= fibo(count, memo)
#                 count = 0
#     if count > 0:
#         total *= fibo(count, memo)
#     return total

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo(total_count - current_index, memo)
    all_ways *= count_of_ways

    return all_ways


memo = {
    1: 1,
    2: 2
}


def fibo(n, memo):
    if n in memo:
        return memo[n]

    nth_fibo = fibo(n - 1, memo) + fibo(n - 2, memo)
    memo[n] = nth_fibo
    return nth_fibo


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9, [2, 4, 7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11, [2, 5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10, [2, 6, 9]))