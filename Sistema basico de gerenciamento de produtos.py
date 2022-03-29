import json
import os

opcao_menu = None
CAMINHO_ARQUIVO = r"C:" #Caminho do arquivo de texto onde será armazenado os produtos.
lista_produtos = []

while opcao_menu != 5:
    print ('''
1) Cadastrar produto. 
2) Consultar produtos por faixa de preço. 
3) Gravar produtos em arquivo. 
4) Carregar produtos do arquivo. 
5) Sair''')
    
    opcao_menu = int(input("Opção: "))

    if opcao_menu == 1:
        codigo = int(input("Código:"))
        existe = None

        for x in lista_produtos:  
            if x['codigo'] == codigo:
                existe = True
        
        if existe != True:
            nome = input("Nome:")
            decricao = input("Descrição:")
            valor = float(input("Valor:"))

            produto = {
                'codigo': codigo,
                'nome': nome,
                'descricao': decricao,
                'valor': valor
            }
            lista_produtos.append(produto)

        else:
            print("Código já cadastrado, operação cancelada")


    elif opcao_menu == 2:
        valor_minimo = float(input("Valor Mínimo: "))
        valor_maximo = float(input("Valor Máximo: "))
        valores = []

        if lista_produtos != []:
            print(f"LISTA DE PRODUTOS DENTRO DA FAIXA DE VALOR: R$ {valor_minimo} à R$ {valor_maximo}")
            print("----------------------------------------------------------------")
            valores = []

            for x in lista_produtos:
                if x['valor'] >= valor_minimo and x['valor'] <= valor_maximo:
                    valores.append({'nome': x['nome'], 'valor': x['valor']})

                    print(f"Código: {x['codigo']} \nNome:{x['nome']} \nDescrição: {x['descricao']} \nValor: {x['valor']}")
                    print("----------------------------------------------------------------")

            sorted(lista_produtos, key=lambda x: x['valor'], reverse = False)
            
            if valores != []:
                menores_valores = list(filter(lambda x: x['valor'] == valores[0]['valor'], lista_produtos))
                maiores_valores = list(filter(lambda x: x['valor'] == valores[-1]['valor'], lista_produtos))
            
                print (f"Produtos de menor valor(R${menores_valores[0]['valor']}):")
                for x in menores_valores:
                    print(f"{x['nome']}")

                print (f"Produtos de maior valor(R${maiores_valores[0]['valor']}):")
                for x in maiores_valores:
                    print(f"{x['nome']}")
            else: 
                print ("Não há produtos nessa faixa de preço.")

        else:
            print ("Não há produtos no sistema.")


    elif opcao_menu == 3:
        if os.path.exists(CAMINHO_ARQUIVO):
            arquivo = open(CAMINHO_ARQUIVO, "w")
            json.dump(lista_produtos, arquivo)
            arquivo.close()
            print("Produtos gravados")
        else: 
            print("Caminho não encontrado")


    elif opcao_menu == 4:
        if os.path.exists(CAMINHO_ARQUIVO):
            arquivo = open(CAMINHO_ARQUIVO, "r")
            conteudo_arquivo = arquivo.read()

            if conteudo_arquivo != "":
                arquivo_produto = json.loads(conteudo_arquivo)
                lista_produtos = arquivo_produto 
                arquivo.close() 
                print("Produtos carregados.")
            else: 
                print("Não há produtos no arquivo.")
                
        else: 
            print("Caminho não encontrado")


    elif opcao_menu < 1 or opcao_menu > 5:
        print("Opção invalida")

    print("----------------------------------------------------------------")

        
