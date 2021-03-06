'''
QUESTION 1: Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a sequence on a 
table. She challenges Bob to pick out the card containing a given number by turning over as 
few cards as possible. 
Write a function to help Bob locate the card.
'''


# inputs

cards = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
query = 6


# Output
# output = 3



# ********** function linear search *****************

# def find_card(card, query):
#     position = 0
    
#     while len(card) > position:
#         if card[position] == query:
#             return position
#         position += 1

#     return -1


# result = find_card(cards, query)
# print(result)




# ********* binary search function ************

# helper function for repeated number

# def check_location(cards, query, mid):
#     mid_number = cards[mid]

#     if mid_number == query:
#         if mid - 1 >= 0 and cards[mid-1] == query:
#             return 'left'
#         else:
#             return 'found'
    
#     elif mid_number < query:
#         return 'left'
#     else:
#         return 'right'


# def find_card(cards , query):
#     lo, hi = 0, len(cards) - 1

#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = check_location(cards, query, mid)


#         if result == 'found':
#             return mid

#         elif result == 'right':
#             lo = mid + 1

#         elif result == 'left':
#             hi = mid - 1

#     return -1



# result = find_card(cards, query)
# print(result)



# ************** Generic Binary Search ***************


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        else:
            lo = mid + 1
    return -1

def find_card(cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
        
    return binary_search(0, len(cards) - 1, condition)


result = find_card(cards, query)
print(result)







# ********** Tests *********

# test = {
#     "input": {
#         "cards": [13, 12, 11, 7, 4, 3, 2, 1],
#         "query": 7
#     },
#     "output": 3
# }

# result = find_card(**test['input']) == test['output']
# print(result)

tests = []

tests.append({
     "input": {
         "cards": [13, 12, 11, 4, 3, 2, 1],
         "query": 7
     },
     "output": 3
})


tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})


# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})


# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})


# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})


# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})


# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})


# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})



# def test_case(test_card, test):   
#     if test_card(test['input']['cards'], test['input']['query']) == test['output']:
#         return 'found'
#     return 'not found'


# # res = test_case(find_card, tests)
# # print(res)

# for test in tests:
#     res = test_case(find_card, test)
#     print(res)
