def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.

    Args:
        notas (list): Lista contendo as notas do aluno.

    Returns:
        float: Média das notas. Retorna 0 se a lista estiver vazia.
    """
    if len(notas) == 0:
        return 0

    return sum(notas) / len(notas)


def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica se o aluno foi aprovado.

    Args:
        media (float): Média final do aluno.
        media_minima (float): Valor mínimo necessário para aprovação.

    Returns:
        bool: True se o aluno estiver aprovado, False caso contrário.
    """
    return media >= media_minima


def gerar_relatorio(alunos):
    """
    Gera um relatório com nome, média e situação dos alunos.

    Args:
        alunos (list): Lista de dicionários contendo nome e notas.

    Returns:
        None
    """
    print("RELATÓRIO ACADÊMICO")
    print("-" * 30)

    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        aprovado = verificar_aprovacao(media)
        situacao = "Aprovado" if aprovado else "Reprovado"

        print(f"Aluno: {aluno['nome']}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print("-" * 30)


def main():
    """
    Executa o fluxo principal do gerenciador de notas.

    Returns:
        None
    """
    alunos = [
        {
            "nome": "Ana",
            "notas": [8.0, 7.5, 9.0]
        },
        {
            "nome": "Bruno",
            "notas": [5.0, 6.0, 4.5]
        },
        {
            "nome": "Carla",
            "notas": [10.0, 9.0, 8.5]
        }
    ]

    gerar_relatorio(alunos)


if __name__ == "__main__":
    main()
