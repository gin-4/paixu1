def bucket_sort(arr):
    bucket_size = 10
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        buckets[(num - min_val) // bucket_size].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr