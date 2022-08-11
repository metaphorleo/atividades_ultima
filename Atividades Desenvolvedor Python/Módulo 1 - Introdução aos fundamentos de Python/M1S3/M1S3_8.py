def prefix_match(word1, word2):
    prefixo = word1.startswith(word2)
    return prefixo

teste = prefix_match("telhado", "telha")

print(teste)