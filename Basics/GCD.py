# 두 자연수 A,B에 대해서 (A>B) A를 B로 나눈 나머지를 R이라고 할때, AB의 최대공약수는 BR의 최대공약수와 같다.

def GCD(a,b):
    if a%b == 0:
        return b
    else:
        return GCD(b, a%b)

print(GCD(192,162))