# Input do usuário
nome = input("Digite o nome do lead: ")
email = input("Digite o e-mail do lead: ")
valor_investimento = float(input("Digite o valor de investimento do lead: "))

# Verificação de qualificação do lead
if valor_investimento < 100000:
    # Lead Desqualificado
    print(
        email,
        "Obrigado pelo Interesse - Informações Importantes",
        f"""
        Olá {nome},

        Agradecemos seu interesse em nossos serviços. No momento, estamos focados em investimentos acima de 100 mil.

        Para ajudar você a alcançar seus objetivos financeiros, sugerimos alguns conteúdos que podem ser úteis:

        - [Link para Blog]
        - [Link para Vídeos Educativos]

        Esperamos poder atendê-lo no futuro.

        Atenciosamente,
        Equipe PG INVEST
        """
    )
    print("Email de desqualificação enviado.")

elif 100000 <= valor_investimento < 300000:
    # Lead Qualificado (100 mil até 300 mil)
    print(
        email,
        "Bem-vindo à PG INVEST!",
        f"""
        Olá {nome},

        Obrigado por se conectar com a PG INVEST! Estamos animados para ajudá-lo a alcançar seus objetivos financeiros.

        Em breve, um de nossos consultores entrará em contato para entender melhor suas necessidades e apresentar as melhores oportunidades de investimento.

        Atenciosamente,
        Equipe PG INVEST
        """
    )
    print(
    
        f"Novo lead qualificado: {nome}, investimento de {valor_investimento}. Entre em contato."
    )
    print("Email de boas-vindas e mensagem de WhatsApp enviados.")

elif 300000 <= valor_investimento < 500000:
    # Lead Qualificado (300 mil até 500 mil)
    print(
        email,
        "Bem-vindo à PG INVEST!",
        f"""
        Olá {nome},

        Obrigado por se conectar com a PG INVEST! Estamos animados para ajudá-lo a alcançar seus objetivos financeiros.

        Em breve, um de nossos consultores entrará em contato para entender melhor suas necessidades e apresentar as melhores oportunidades de investimento.

        Atenciosamente,
        Equipe PG INVEST
        """
    )
    print(
        f"Novo lead qualificado: {nome}, investimento de {valor_investimento}. Entre em contato."
    )
    print("Email de boas-vindas e mensagem de WhatsApp enviados.")

elif 500000 <= valor_investimento < 1000000:
    # Lead Qualificado (500 mil até 1 milhão)
    print(
        email,
        "Bem-vindo à PG INVEST!",
        f"""
        Olá {nome},

        Obrigado por se conectar com a PG INVEST! Estamos animados para ajudá-lo a alcançar seus objetivos financeiros.

        Em breve, um de nossos consultores entrará em contato para entender melhor suas necessidades e apresentar as melhores oportunidades de investimento.

        Atenciosamente,
        Equipe PG INVEST
        """
    )
    print(
    
        f"Novo lead qualificado: {nome}, investimento de {valor_investimento}. Entre em contato."
    )
    print("Email de boas-vindas e mensagem de WhatsApp enviados.")

else:
    # Lead Superqualificado (acima de 1 milhão)
    print(
        email,
        "Bem-vindo à PG INVEST!",
        f"""
        Olá {nome},

        Obrigado por se conectar com a PG INVEST! Estamos animados para ajudá-lo a alcançar seus objetivos financeiros.

        Em breve, um de nossos consultores entrará em contato para entender melhor suas necessidades e apresentar as melhores oportunidades de investimento.

        Atenciosamente,
        Equipe PG INVEST
        """
    )
    print(
    
        f"Novo lead superqualificado: {nome}, investimento de {valor_investimento}. Tratar com prioridade."
    )
    print("Email de boas-vindas e mensagem de WhatsApp enviados.")
