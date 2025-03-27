# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   [ ] 1. O aluno deverá digitar 3 notas através do teclado
#   [ ] 2. Seu programa deverá calcular a média das notas    
#   [ ] 3. A partir da média, verificar qual situação o aluno se encontra conforme notas abaixo:
#       3.1 media > 70 - aprovado
#       3.2 media < 40 - reprovado
#       3.3 media entre 40 e 70 - exame/recuperação
#   [ ] 4. Não será permitido médias acima de 100 e abaixo de zero
#   [ ] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de digitação
#   [ ] 6. Mostrar na tela para o aluno a situação final baseado na media calculada

print("Seja bem-vindo ao site educacional. Esse é o site perfeito para saber se será aprovado ou reprovado")
nota1 = int(input("Para iniciar, digite sua primeira nota:"))
nota2 = int(input("Para iniciar, digite sua segunda nota:"))
nota3 = int(input("Para iniciar, digite sua terceira nota:"))

media = (nota1+nota2+nota3)/3

if media < 0 or media > 100:
    print("Você digitou errado. Por favor, reinice o programa, e digite de forma correta.")
elif media > 70:
    print("A sua nota foi", media, ". Você foi aprovado!")
elif media > 40 and media < 70:
    print("A sua nota foi", media, "Você está de recuperação.")
else:
    print("A sua nota foi", media, "Você foi reprovado.")
