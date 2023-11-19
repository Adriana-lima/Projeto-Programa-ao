# Inicio de um sonho
print("Seja bem-vindo ao plano financeiro automático desenvolvido para estudantes universitários que desejam estruturar suas finanças, maximizar seus ganhos e reduzir suas despesas de maneira inteligente. ")

def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

# Função principal
def main():
    # Obtendo informações financeiras do usuário
    total_renda = obter_valor("\nDigite o total de dinheiro que você ganha em um mês: ")

    # Obtendo os gastos do usuário
    alimentacao = obter_valor("Digite o custo de alimentação: ")
    transporte = obter_valor("Digite o custo de transporte: ")
    saude = obter_valor("Digite o custo de saúde: ")
    despesas_pessoais = obter_valor("Digite o custo de despesas pessoais: ")
    pet = obter_valor("Digite o custo com o pet: ")
    faculdade = obter_valor("Digite o custo da faculdade: ")
    dividas = obter_valor("Digite o valor das dívidas: ")

    # Exibindo os resultados
    print(f"\nResumo Financeiro R$:")
    print(f"Total de Renda: R${total_renda:.2f}")
    print("\nResumo dos Gastos:")
    print(f"Alimentação: R${alimentacao:.2f}")
    print(f"Transporte: R${transporte:.2f}")
    print(f"Saúde: R${saude:.2f}")
    print(f"Despesas Pessoais: R${despesas_pessoais:.2f}")
    print(f"Pet: R${pet:.2f}")
    print(f"Faculdade: R${faculdade:.2f}")
    print(f"Dívidas: R${dividas:.2f}")
    total_gastos = dividas + faculdade + pet + despesas_pessoais + transporte + alimentacao
    print(f"\nTotal de gastos: R${total_gastos:.2f}")
    renda_custo = total_renda - total_gastos
    print(f"\nO montante remanescente após as despesas é de: R${renda_custo:.2f}")

    # mensagem de plano financeiro 60, 20, 10, 10.
    print(f"\nAgora, vamos aplicar o método financeiro, destinando 60% para despesas essenciais, reservando 20% para gastos pessoais, alocando 10% para situações emergenciais e dedicando os últimos 10% para investimentos.")

    prosseguir = input("\nPodemos começar? (Sim/Não): ")
    # Loop enquanto a resposta for diferente de "Sim" 
    while prosseguir.lower() != "sim":
        if prosseguir.lower() == "não":
            print("Encerrando...")
            break  # Encerra o loop se a resposta for "Não"
        else:
             print("Resposta inválida. Tente novamente.")
             prosseguir = input("Podemos começar? (Sim/Não): ")

    
    sesentacalculo = total_renda *60/100
    vintepessoais = total_renda *20/100
    dezemergencia = total_renda *10/100
    dezinveste = total_renda *10/100
    total_dividas = vintepessoais - dividas
    print("\nSeção de 60% para despesas essenciais")
    print(f"Valor que deve ser distribuido para despesas essenciais é de: R${sesentacalculo:.2f}")
    print("Isso inclui:")
    print(f"-Despesas com alimentação. Estimasse que 47% de R${sesentacalculo:.2f}, ou R${sesentacalculo*47/100}, seja para despesas com alimetação")
    print(f"-Custos de transporte. Estimasse que 32% de R${sesentacalculo:.2f}, ou R${sesentacalculo*32/100}, seja para despesas com transporte")
    print(f"-Despesas com saúde. Estimasse que 8% de R${sesentacalculo:.2f}, ou R${sesentacalculo*8/100}, seja para despesas com saúde")
    print(f"-Cuidados com animais de estimação (Pet). Estimasse que 8% de R${sesentacalculo:.2f}, ou R${sesentacalculo*8/100}, seja para despesas com animais de estimação")
    print(f"-Gastos com faculdade. Estimasse que 5% de R${sesentacalculo:.2f}, ou R${sesentacalculo*5/100}, seja para despesas com a faculdade")
    print(f"\nSeção de 20% para gastos pessoais")
    print(f"Valor que deve ser distribuido para gastos pessoais é de: R${vintepessoais:.2f}")
    print("Isso inclui:")
    print("-Gastos com lazer e entretenimento")
    print(f"-Pagamento de dívidas. Utilize o orçamento de R${vintepessoais:.2f} destinado aos gastos pessoais para pagar as dívidas de R${dividas:.2f}. ")
    print(f"Sobrando um total de R${total_dividas:.2f}")
    print(f"\nSeção de 10% para situações emergenciais")
    print(f"Valor que deve ser reservado para situações emergenciais é de: R${dezemergencia:.2f}")
    print(f"\nSeção de 10% para investimentos")
    print(f"Valor que deve ser reservado para investimentos é de: R${dezinveste:.2f}")
    print("Sugestão para investimentos seguros:")
    print(f"-Poupança: 0.50% de rendimento ao mês. Sendo R${dezinveste} investidos rendera R${dezinveste*0.50/100} por mês")
    print(f"-Tesouro Prefixado: 10.00% de rendimento ao ano. Sendo R${dezinveste} investidos rendera R${dezinveste*10/100} em um ano")
    print(f"-Tesouro Selic: 12.65% de rendimento ao ano. Sendo R${dezinveste} investidos rendera R${dezinveste*12.65/100} em um ano")
    print(f"-Tesouro IPCA: 5.50% de rendimento ao ano. Sendo R${dezinveste} investidos rendera R${dezinveste*5.5/100} em um ano")
    print(f"-CDB e LC: 13,41% de rendimento ao ano. Sendo R${dezinveste} investidos rendera R${dezinveste*13.41/100} em um ano")
    print(f"-LCI e LC: 13,41% de rendimento ao ano. Sendo R${dezinveste} investidos rendera R${dezinveste*13.41/100} em um ano")


    


    
if __name__ == "__main__":
    main()


