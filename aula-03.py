# 1. Listas ([])
> * São coleções ordenadas e mutáveis. Você as usa quando tem uma sequência de itens que pode precisar alterar, adicionar ou remover depois.
## Lista de frutas (pode ser alterada)
```
frutas = ["maçã", "banana"]
frutas.append("laranja") # Adicionando um item
```
<br />
<br />

# 2. Tuplas (())
```
São coleções ordenadas, mas imutáveis. Uma vez criada, você não consegue mudar os valores. São ótimas para garantir a segurança dos dados (como coordenadas geográficas ou configurações que não devem mudar).
````
## Tupla de coordenadas (não muda)
> * Código
```
posicao = (10.5, -42.8)
```
<br />
<br />
# 3. Dicionários ({})
## Dicionário de um usuário
> * Código
```
usuario = {
    "nome": "Alice",
    "idade": 25
}
print(usuario["nome"]) # Acessa o valor pela chave
```
<br />
<br />

## Qual a diferença principal?
> * Lista: Use para filas ou coleções de itens similares que mudam.
> * Tupla: Use para dados que são "escritos em pedra". É mais rápida e ocupa menos memória.
> * Dicionário: Use quando precisar rotular seus dados para encontrá-los rapidamente por um nome.

# Exemplo Prático de Treinamento
> * Imagine que estamos gerenciando um pequeno inventário de produtos. Vamos usar as três estruturas juntas:
```
  # 1. Tupla: Informação fixa do sistema (nome da loja e ID da filial)
info_loja = ("Mercado Central", 101)

# 2. Dicionário: Detalhes de um produto específico
produto = {
    "nome": "Caderno",
    "preco": 15.50,
    "estoque": 10
}

# 3. Lista: Uma coleção de dicionários (vários produtos)
inventario = [
    produto,
    {"nome": "Caneta", "preco": 2.00, "estoque": 50}
]

# Exibindo os dados
print(f"Bem-vindo ao {info_loja[0]}")
for item in inventario:
    print(f"Produto: {item['nome']} | Preço: R$ {item['preco']}")
```

# Qual a diferença principal?
## Lista: Use para filas ou coleções de itens similares que mudam.
## Tupla: Use para dados que são "escritos em pedra". É mais rápida e ocupa menos memória.
## Dicionário: Use quando precisar rotular seus dados para encontrá-los rapidamente por um nome.
