# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    return sum([i for i in range(0, number) if i % 3 == 0 or i % 5 == 0])
