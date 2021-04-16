def sockMerchant(n, ar):
    ar_no_duplicates = dict.fromkeys(ar)
    pairs = 0
    for sock in ar_no_duplicates:
        ocurrences = ar.count(sock)
        print("ocurrences of {} in {} -> {}".format(sock, ar, ocurrences))
        if ocurrences  % 2 == 0:
            pairs += ocurrences / 2
        elif ocurrences % 2 == 1 and ocurrences > 2:
            pairs += (ocurrences - 1) / 2

    return int(pairs)
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(n, ar))