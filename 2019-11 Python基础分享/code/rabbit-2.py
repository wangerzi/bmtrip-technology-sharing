def fiber(day = 12):
    if day in [1, 2]:
        return 1
    return fiber(day - 1) + fiber(day - 2)

print(fiber(12))
