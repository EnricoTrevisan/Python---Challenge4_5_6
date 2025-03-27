# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escolar
#   1. O aluno deverá digitar sua nota através do teclado
#   2. Verificar qual a situação o aluno se encontra conforma as notas abaixos
#    2.1 nota > 70 = aprovado
#    2.2 nota < 40 = reprovado
#    2.3 nota entre 40 e 70 = exame / recuperação
#   3. Mostrar na tela para o aluno a situação final baseado na nota digitada.


print("Seja bem-vindo ao site educacional. Esse é o site perfeito para saber se será aprovado ou reprovado")
nota = int(input("Para iniciar, digite sua nota:"))

if nota > 70:
    print("A sua nota foi", nota, ". Você foi aprovado!")
elif nota > 40 and nota < 70:
    print("A sua nota foi", nota, "Você está de recuperação.")
else:
    print("A sua nota foi", nota, "Você foi reprovado.")


print("Obrigado por usar nosso site. Esperamos sua próxima visita.")
