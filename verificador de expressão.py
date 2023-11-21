expressao = str(input('digite uma expressão matemática'))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) > 0:
    print('expressão inválida')
else:
    print('válida')
