"""
https://contest.yandex.ru/algorithm2018/contest/8254/problems/B/
"""
# def get_indexes(mas: list, is_nvp: bool):
#     r = []
#     for i in range(0, len(mas) - 1):
#         for k in range(i + 1, len(mas)):
#             t = [i + 1]
#             v = mas[i]
#             for j in range(k, len(mas)):
#                 if is_nvp:
#                     if mas[j] > v:
#                         v = mas[j]
#                         t.append(j + 1)
#                 else:
#                     if mas[j] < v:
#                         v = mas[j]
#                         t.append(j + 1)
#             if len(t) > 1 and t not in r:
#                 r.append(t)
#     return r

# def to_str(mas: list):
#     return " ".join(str(element) for element in mas)

# def get_solve(nvps: list, nups: list):
#     for nvp in nvps:
#         for i in range(0, len(nups)):
#             skip = False
#             for nv in nvp:
#                 if nv in nups[i]:
#                     skip = True
#                 if skip:
#                     break
#             if not skip:               
#                 return f"{len(nvp)}\n{to_str(nvp)}\n{len(nups[i])}\n{to_str(nups[i])}"
#     return "IMPOSSIBLE"

# n = int(input())
# p = list(map(int, input().split()))
# print(get_solve(get_indexes(p, is_nvp=True), get_indexes(p, is_nvp=False)))

"""
https://contest.yandex.ru/algorithm2018/contest/8254/problems/D/
"""

# def f(s, query):
#     count = 0
#     start = 0
#     while True:
#         start = s.find(query, start)
#         if start == -1:
#             break
#         count += 1
#         start += 1
#     return count

# def main(db,n):
#     s = db[0]
#     cnt = f(db,s)

#     for i in range(1,n):
#         s = db[i]+s if (f(db,db[i]+s)>f(db,s+db[i])) else s+db[i]
#         cnt += f(db,s)
#     print(cnt)


# n = int(input())
# s = input()
# main(s,n)
