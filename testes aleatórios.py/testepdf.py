from datetime import datetime, timedelta

# Configurações
start_date = datetime(2025, 6, 3)
end_date = datetime(2025, 12, 31)
weekdays_available = [1, 5]  # terça (1) e sábado (5)

# Conteúdo do cronograma (resumido)
study_plan = [
    # Junho e Julho (8 semanas como exemplo anterior)
    ("Matemática", ["Números inteiros e operações", "Frações e decimais", "Problemas simples"]),
    ("Português", ["Classes gramaticais", "Pontuação básica", "Interpretação de texto"]),
    ("Geografia", ["Mapas e localização", "Continentes e oceanos", "Tipos de clima"]),
    ("História", ["Pré-história: Paleolítico e Neolítico"]),
    ("Ciências", ["Estados físicos da matéria", "Força e movimento simples", "Misturas e soluções"]),
    ("Redação", ["Estrutura do texto", "Parágrafos", "Escrita livre"]),
    ("Matemática", ["Porcentagem básica", "Proporcionalidade", "Problemas simples"]),
    ("História", ["Antiguidade: Egito e Mesopotâmia"]),
    ("Geografia", ["Relevo brasileiro", "Recursos naturais", "Sustentabilidade"]),
    ("História", ["Antiguidade: Grécia e Roma"]),
    ("Física", ["Forças básicas", "Movimento retilíneo", "Exercícios simples"]),
    ("História", ["Idade Média: Feudalismo e Igreja"]),
    ("Química", ["Estados físicos", "Tabela periódica", "Ligações químicas"]),
    ("História", ["Idade Moderna: Navegações e descobertas"]),
    ("Matemática", ["Geometria plana", "Progressões", "Exercícios"]),
    ("História", ["Brasil Colonial: início da colonização"]),
]

# Gerar as datas disponíveis (terças e sábados)
current_date = start_date
study_dates = []
while current_date <= end_date:
    if current_date.weekday() in weekdays_available:
        study_dates.append(current_date)
    current_date += timedelta(days=1)

# Preencher o cronograma
cronograma = []
for i, date in enumerate(study_dates):
    if i < len(study_plan):
        materia, topicos = study_plan[i]
    else:
        # Repetir o ciclo com temas variados e aprofundados
        index = i % len(study_plan)
        materia, topicos = study_plan[index]
    cronograma.append({
        "data": date.strftime("%d/%m/%Y (%A)"),
        "materia": materia,
        "topicos": topicos
    })

# Mostrar os primeiros itens para conferência
cronograma[:5]
