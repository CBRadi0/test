solution=lambda t:-(-t//5)



# def solution(distance:int):
#     while distance != 0:
#         possible_strides = [5,4,3,2,1]
#         steps = 0
#         for step in possible_strides:
#             while distance >= step:
#                 distance -= step
#                 steps +=1
#     return steps
print(solution(32))
