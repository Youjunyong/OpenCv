times = [7,10]
def count_per_times(target):
    cnt = 0
    for i in times:
        cnt += target // i
    return cnt

print(count_per_times(27))