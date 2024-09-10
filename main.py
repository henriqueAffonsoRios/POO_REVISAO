from quiz import *

if __name__ == "__main__":
    q1 = Quiz(10, 2)
    print(q1)
    q2 = Quiz2A(10, 2)
    print(q2)
    q3 = Quiz3A(10, 2)
    print(q3)

    listaQuizes = [q1, q2, q3]

    aluno1 = Aluno(123, "Henrique", listaQuizes)
    aluno2 = Aluno(321, "Rafael", listaQuizes)


    try:
        poo = Disciplina("POO", "Ferauche", 2024, 4)
        poo.add_aluno(aluno1)
        poo.add_aluno(aluno2)
        print(poo)
    except Exception as e:
        raise(e)