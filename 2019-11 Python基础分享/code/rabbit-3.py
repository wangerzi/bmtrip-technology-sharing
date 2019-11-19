global fiberCache
fiberCache = {}
def fiber(day = 12):
    if day in [1, 2]:
        return 1
    global fiberCache
    if day not in fiberCache.keys():
        fiberCache[day] = fiber(day - 1) + fiber(day - 2)
    return fiberCache[day]
ans = fiber(12)
print(ans)
