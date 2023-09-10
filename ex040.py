n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('\033[4;31mSUA MÉDIA FICOU {:.2F} E VOCÊ FOI REPROVADO!'.format(media))
    
elif media > 5.0 and media < 6.9:
    print('\033[4;33mVocê ficou de recuperação, porque sua média fico {:.2f}, boa sorte na prova final'.format(media))

elif media >= 7.0:
    print('\033[4;32mPARABÉNS, sua média ficou {:.2f}, você foi aprovado'.format(media))
