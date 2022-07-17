def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


# def solution(phone_book):
#     answer = True
#     phonebook = sorted(phone_book, key=len)
#     for i in range(len(phonebook)):
#         if i > 0:
#             if phonebook[i].startswith(phonebook[0]):
#                 answer=False
#     return answer