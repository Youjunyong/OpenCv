# n ~ 2*n 사이의 소수를 구해야 한다.


# r = int(input()) #입력하는 만큼 범위
# cheak = [False for _ in range(r)]

# for i in range(2,int(r**0.5)) : # 2부터 ~ 범위(r)의 제곱근까지
#     if cheak[i] == False : # 지워지지 않고, 가장 작은수라면
#         for j in range(i*2 , r, i ): # i의 2배수 부터, 3배수, 4배수, .... 범위끝까지 지운다.(True로)
#             cheak[j] = True
# print(cheak)
# prime_number = [i for i,j in enumerate(cheak) if i>=2 and j==False]

# print(prime_number)
while(True):
    
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else :
        check = [False for _ in range(2*n)]   
        for i in range(2, int((2 * n)** 0.6)):
            if check[i] == False:
                for j in range(i*2, 2*n, i):
                    check[j] = True

        prime_number = [i for i,j in enumerate(check) if i>n and j == False]
        print(len(prime_number))