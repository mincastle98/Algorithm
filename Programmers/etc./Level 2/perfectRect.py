# 멀쩡한 사각형
from math import gcd


def solution(w, h):
    gcd_ = gcd(w, h)
    w_ = w // gcd_
    h_ = h // gcd_

    return w * h - (w_ + h_ - 1) * gcd_


print(solution(8, 12))
