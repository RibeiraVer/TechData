# # Definindo o número de alunos
# num_alunos = 20

# # Estrutura de repetição para processar as notas de cada aluno
# for i in range(1, num_alunos + 1):
#     print(f"\nAluno {i}:")
    
#     # Entrada de dados
#     nota1 = float(input("Digite a nota da primeira avaliação: "))
#     nota2 = float(input("Digite a nota da segunda avaliação: "))
#     nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

#     # Substituir a menor nota pela optativa, se ela for maior
#     if nota_optativa != -1:
#         menor_nota = min(nota1, nota2)
#         if nota_optativa > menor_nota:
#             if nota1 == menor_nota:
#                 nota1 = nota_optativa
#             else:
#                 nota2 = nota_optativa

#     # Cálculo da média
#     media = (nota1 + nota2) / 2

#     # Exibindo resultado e status
#     print(f"Média do semestre: {media:.2f}")
    
#     if media >= 6.0:
#         print("Aprovado")
#     elif media < 3.0:
#         print("Reprovado")
#     else:
#         print("Exame")

# num=5
# while True:
#     print('teste')
#     if not(num<3):
#         pass


#>>>Desenvolva um programa que guarde os dados de 10 pessoas que estão se candidatando a uma vaga de emprego, sabendo que candidatos 
# menores de 18 anos não podem participar. Os dados coletados são: nome, data de nascimento, telefone, e-mail, formação acadêmica e a 
# experiência profissional.

# ATIVIDADE DE FIXAÇÃO


# from datetime import datetime

# def calcular_idade(data_nascimento):
#     hoje = datetime.now()
#     nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
#     idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
#     return idade

# # VARIAVEL PARA ARMAZENAR OS CANDIDATOS VALIDOS
# def coletar_dados():
#     candidatos = []

# # ENQUANTO NAO ATINGIMOS 10 CANDIDATOS VALIDOS    
#     while len(candidatos) < 10:
#         nome = input("Nome: ")
#         data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        
#         # VERIFICAR SE O CANDIDATO MINIMA DE 18 ANOS
#         if calcular_idade(data_nascimento) < 18:
#             print("Candidatos menores de 18 anos não podem se inscrever. Tente novamente.")
#             continue
        
#         telefone = input("Telefone: ")
#         email = input("E-mail: ")
#         formacao = input("Formação Acadêmica: ")
#         experiencia = input("Experiência Profissional: ")
        
#         # ARMAZENAR OS DADOS DOS CANDIDATOS
#         candidato = {
#             'nome': nome,
#             'data_nascimento': data_nascimento,
#             'telefone': telefone,
#             'email': email,
#             'formacao': formacao,
#             'experiencia': experiencia
#         }
        
#         candidatos.append(candidato)
#         print(f"Candidato {nome} adicionado com sucesso!")
    
#     return candidatos

# def exibir_candidatos(candidatos):
#     print("\nLista de Candidatos:")
#     for i, candidato in enumerate(candidatos, start=1):
#         print(f"{i}. Nome: {candidato['nome']}, Data de Nascimento: {candidato['data_nascimento']}, "
#               f"Telefone: {candidato['telefone']}, E-mail: {candidato['email']}, "
#               f"Formação: {candidato['formacao']}, Experiência: {candidato['experiencia']}")

# if __name__ == "__main__":
#     candidatos = coletar_dados()
#     exibir_candidatos(candidatos)


#ESTRUTURA DE ARMAZENAMENTO

#LISTAS 'conversão list()'
candidatos=[] #lista vazia
lista1=[2,4,6,8,10]
print(lista1)
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])
print(lista1[4])
print(lista1[-1])
print(lista1[-2])
lista1.append(20)
lista1.insert(26,3)
lista1.insert(2,3)
print(lista1)
print(len(lista1))
      




#TUPLAS 'conversão:tupla()'
senhas=() #tupla vazia

#DICIONARIOS 'conversão: dict()'
estados_uf={} #dicionario vazio