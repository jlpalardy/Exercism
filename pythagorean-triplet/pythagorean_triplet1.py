def triplets_with_sum(number):
    results = []
    end = number // 2
    for i in range(1,end):
        for j in range(i+1,end):
            k = number - (i + j)
            if k > j and is_triplet([i,j,k]):
                results.append([i,j,k])
    return results


def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return a ** 2 + b ** 2 == c **2
