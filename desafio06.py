# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   [x] 1. O aluno deverá digitar 3 notas através do teclado
#   [x] 2. Seu programa deverá calcular a média das notas    
#   [x] 3. A partir da média, verificar qual situação o aluno se 
# encontra conforme notas abaixo:
#       3.1 media > 70 - aprovado
#       3.2 media < 40 - reprovado
#       3.3 media entre 40 e 70 - exame/recuperação
#   [x] 4. Não será permitido médias acima de 100 e abaixo de zero
#   [x] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de digitação
#   [x] 6. Mostrar na tela para o aluno a situação final baseado na media calculada
#   [] 7. Acrescente no desafio anterior a frequencia de no minimo 75% para ser aprovado
#   [x] 8. O aluno pode ser aprovado se ele recebeu uma dispensa da disciplina

print("Seja bem-vindo ao site educacional. Esse é o site perfeito para saber se será aprovado ou reprovado")
print("Antes de tudo, você tem alguma dispensa disciplinar?")

dispensa = input("Digite sim, caso tenha:")

if dispensa == "sim":
    print("Certo, você não precisa digitar sua média. Obrigado por usar nosso site!")
else:
    frequencia = int(input("Agora, digite sua frequência escolar:"))

    if frequencia < 75: 
        print("Você não tem a frequência necessária para ser aprovado. Obrigado por usar nosso site!")
    else:   
        nota1 = int(input("Para iniciar, digite sua primeira nota (prática):"))
        nota2 = int(input("Para iniciar, digite sua segunda nota (oral):"))
        nota3 = int(input("Para iniciar, digite sua terceira nota (escrita):"))

        media = (nota1+nota2+nota3)/3

        if media < 0 or media > 100:
            print("Você digitou errado. Por favor, reinice o programa, e digite de forma correta.")
        elif media > 70:
            print("A sua nota foi", media, ". Você foi aprovado!")
        elif media > 40 and media < 70:
            print("A sua nota foi", media, "Você está de recuperação.")
        else:
             print("A sua nota foi", media, "Você foi reprovado.")

print("Obrigado por usar nosso programa. Esperamos para sua próxima visita.")