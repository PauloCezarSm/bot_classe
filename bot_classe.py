
NICKNAMES = {
    'Barbaro': 'Carinha bravo, nível de habilidades: Legal e Raivoso.',
    'Arqueiro': 'Ótimo tipo de classe, muito cooperativo, nível de habilidades: alta!',
    'Mago': 'Considerado um dos melhores classes no game, extremamente flexível e\n adaptável ao jogo de seu parceiro, nível de habilidades: Muito alta!',
    'Guerreiro': 'Comum porém não tem erro nível de habilidades: Adequavel!'
}

DEFAULT = 'Huum, não sei o que dizer sobre essa Classe :('

while True:

    nome = input("Seu nome: ")

    print("Opa, Blz\n Mefa seu nome ai para começarmos com o pé direito")
    print('Uhhh, {}'.format(nome),' nome legal')
    print("Qual Classe voce gostaria de utilizar?")
    print("Que tal essas opções:", list(NICKNAMES.keys()), '?')

    classe = input("Classe: ")

    print(NICKNAMES.get(classe, DEFAULT))

    confirm = input('Gostaria de manter essa classe? [S/n] ')

    if confirm in ['S', 's', '']:
        break
    else:
        print()

print('Parabens {}, seu nick será {}'.format(classe))
