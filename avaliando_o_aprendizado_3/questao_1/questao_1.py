def empty(s):

    if len(s) == 0:
        return True
    else:
        return False


def pop(s):
    return s.pop(-1)


stack = ['calça', 'meias', 'paletó', 'gravata', 'camisa']

if not empty(stack):
    print(pop(stack))
else:

    print('Pilha vazia')