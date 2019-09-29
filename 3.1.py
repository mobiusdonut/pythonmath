def gcf(a, b):
    gcf = 1
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) & (b % i == 0) & (i > gcf):
            gcf = i
    return gcf
print(gcf(150,138))
