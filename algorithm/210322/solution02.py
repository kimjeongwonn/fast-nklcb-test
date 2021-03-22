def solution(n, m):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def lcm(x, y):
        result = (x*y)//gcd(x, y)
        return result

    x = gcd(n, m)
    y = lcm(n, m)
    return [x, y]
