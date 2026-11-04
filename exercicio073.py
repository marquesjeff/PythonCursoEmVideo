print("Tuplas com Times de Futebol")

times = ("Flamengo", "Palmeiras", "Cruzeiro", "Fluminense", "Athletico-PR",
         "Bahia", "Atlético-MG", "Bragantino", "Santos", "São Paulo",
         "Coritiba", "Mirassol", "Botafogo", "Vasco", "Vitória",
         "Internacional", "Grêmio", "Corinthians", "Remo", "Chapecoense")

top5 = times[:5]
last4 = times[-4:]
pos_chape = times.index("Chapecoense")
print(f"Os 5 primeiros são: {top5}")
print(f"Os 4 últimos são: {last4}")
print(f"O chapecoense está na posição {pos_chape + 1}°")