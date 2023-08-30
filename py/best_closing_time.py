def bestClosingTime(customers: str) -> int:
    penalties = {}
    print(customers[1:])
    for idx in range(len(customers)):
        penalties.update({
            str(idx): list(customers[idx:]).count('Y')
        })
    return int(min(penalties, key=penalties.get))
    
print(bestClosingTime('YNYY'))
