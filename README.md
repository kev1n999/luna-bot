# Luna - Clean/Template 
Essa é uma versão do projeto principal, mas focado em oferecer um template mais "limpo", sem recursos adicionais como database e serviçoes extras. 

--- 

# Como usar
1. Clone essa branch do repositório
```
git clone -b clean/template --single-branch https://github.com/kev1n999/luna-bot
```
2. Abra a pasta raiz do projeto em seu editor de texto/código
3. Crie um ambiente virtual dentro dessa pasta
```
python3 -m venv venv ou python -m venv venv 
source venv/bin/activate ou(no windows) venv\Scripts\activate
```
4. Instale as bibliotecas necessárias
```
pip3 install -r requirements.txt ou pip install -r requirements.txt
```
5. Crie um arquivo .env(ainda na pasta raiz), e preencha as seguintes váriaveis
```
BOT_TOKEN= # Token do bot 
DEFAULT_PREFIX= # Prefixo dos comandos de mensagens
```
6. Inicie o bot
```
python3 -m luna.main
```

# Como criar novos comandos?
> Para saber mais, leia a parte sobre "Como criar comandos" em **[README](https://github.com/kev1n999/luna-bot/blob/main/TEMPLATE.md)**
