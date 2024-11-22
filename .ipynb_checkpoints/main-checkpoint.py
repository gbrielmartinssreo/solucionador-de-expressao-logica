from specificExpression import resolve_expression
from typeExpre import typeExpression
from truthTable import truthTable_generator

def menu():
    print("Bem-vindo ao Solucionador de Lógica Proposicional!")
    print("Escolha uma das opções abaixo:")
    print("1. Gerar tabela verdade")
    print("2. Resolver expressão lógica com valores específicos")
    print("3. Resolver demonstrações com regras de inferência")
    print("4. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    return opcao

choice = menu();


if choice == "1":
    expression,values = typeExpression(False);
    truthTable_generator(expression,values);

elif choice == "2":
    expression,values = typeExpression(True);
    resul = resolve_expression(expression,values);
    print(resul);

elif choice == "4":
    print("Até mais!")
    exit()

