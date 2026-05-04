def validar_senha(senha):
    # Lista para armazenar o que falta
    erros = []
    
    # 1. Comprimento mínimo
    if len(senha) < 8:
        erros.append("Mínimo de 8 caracteres")
    
    # Flags para os critérios
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    caracteres_especiais = "!@#$%^&*(),.?\":{}|<>"

    # Lógica: Percorrer caractere por caractere
    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in caracteres_especiais:
            tem_especial = True

    # Adicionar à lista de erros se não cumprir os requisitos
    if not tem_maiuscula:
        erros.append("Um caractere maiúsculo")
    if not tem_minuscula:
        erros.append("Um caractere minúsculo")
    if not tem_numero:
        erros.append("Um número")
    if not tem_especial:
        erros.append("Um caractere especial")

    # Resultado
    if not erros:
        return "Senha forte"
    else:
        return "Requisitos ausentes: " + ", ".join(erros)

# Teste
senha_usuario = input("Digite sua senha: ")
print(validar_senha(senha_usuario))