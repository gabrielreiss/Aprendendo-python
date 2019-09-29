#dicionarios

meu_dict = {}
meu_dict["nome"] = "Joelson"
meu_dict["sobrenome"] = "Beija-Flor"
meu_dict["hobbies"] = ["jogos", "podcast", 'series']
meu_dict["idade"] = 20

novo_dict = {   "nome": "Zerola",
                "sobrenome": "Adelaide",
                "idade": 30,
                "hobbies": ["livro de artesanato",
                            "filmes espanhois",
                            "series espanholas"]
}

familia = {
    "joelson": meu_dict,
    "zerola": novo_dict
}

#selecionando dados
familia["joelson"]["hobbies"]+familia["zerola"]["hobbies"]