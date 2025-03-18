PAG_INICIAL = """
================================================
Bem-vindo ao sistema de gerenciamento de água!
================================================

[r] - Registrar consumo
[e] - Exibir consumo
[s] - Sair


"""
META_DIARIA = 2000
consumo = []

while True:
    exibir_pag_inicial = input (PAG_INICIAL)

    if exibir_pag_inicial == "r":
        horario = input("\nDigite que horas são (Formato: HH:MM): ")
        qntd_agua = int(input("\nDigite quantas mL de água você consumiu: "))
        consumo.append({
            'id': int(len(consumo) + 1),
            'horario': horario,
            'qntd_de_agua_consumida': qntd_agua
        })
    elif exibir_pag_inicial == "e":
        print('========================Registro de consumo========================')
        if not consumo:
            print("""Hoje você não consumiu água, vá beber!""")
        else:
            total = sum(quanto_consumiu['qntd_de_agua_consumida'] for quanto_consumiu in consumo)
            for quanto_consumiu in consumo:
                if quanto_consumiu == consumo[-1]:
                    print(f"\nID: {quanto_consumiu['id']} | ⏱️ {quanto_consumiu['horario']} -> {quanto_consumiu['qntd_de_agua_consumida']} mL. (Ultimo horário de consumo!)")
                else:
                    print(f'ID: {quanto_consumiu['id']} | ✅ {quanto_consumiu['horario']} -> {quanto_consumiu['qntd_de_agua_consumida']} mL.')

            print(f'\nVocê consumiu {total} mL de {META_DIARIA} mL.')
            porcentagem = total/META_DIARIA * 100
            print(f'Gráfico: {"|" * int(porcentagem // 10)} ({porcentagem:.0f}%)')

        print('===================================================================')
    elif exibir_pag_inicial == "s":
        print("saindo...")
        break
    else:
        print("Opção invalida!")