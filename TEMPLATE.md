# Como usar
Se você deseja usar esse projeto como base ou template para desenvolver seus próprios bots, siga os passos a seguir 

---

# Como funciona
1. Clone o repositório 
```
git clone https://github.com/kev1n999/luna-bot 
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
5. Crie um arquivo `.env`(ainda na pasta raiz), e preencha as seguintes váriaveis
```
BOT_TOKEN= # Token do bot 
DEFAULT_PREFIX= # Prefixo dos comandos de mensagens  
MONGO_URI= # URI de um banco de dados criado no dashboard do MongoDB 
GOOGLE_GENAI_KEY= # Chave da API do google-gemini 
``` 
6. Inicie o bot
```
python3 -m luna.main
```

---

# Observações 
> O projeto já está com uns comandos por padrão, mas você pode ficar a vontade pra removê-los e adicionar mais comandos
> Esse template segue uma estrutura específica e adequada para a criação de comandos, você pode aprender facilmente seguindo as instruções abaixo
> É recomendável ter um nível intermediário de conhecimento na linguagem Python e em programação geral, mas em teoria você só precisa seguir o padrão de criação dos comandos
> Caso não queira usar algum recurso em específico, como banco de dados ou gemini-api, você pode remover algumas partes relacionadas em determinados módulos
---

# Como criar novos comandos? 
> - Todos os comandos disponíveis, por padrão serão definidos dentro de sub-pastas dentro da pasta `luna/commands`
> - Pasta cogs: Essa pasta é responsável por armazenar todos os módulos de comandos de barra 
> - Pasta messages: Essa pasta é responsável por armazenar todos os módulos de comandos de mensagem/prefixo 

---

# Como criar comandos de barra(/)
1. Crie um novo arquivo `.py` dentro de alguma sub-pasta da pasta `cogs`(ex: cogs/utils/ping.py)
2. Siga esse padrão de código para criar um novo comando funcional:
```py
from discord import app_commands, Interaction

class Ping(app_commands.Command):
  def __init__(self):
    super().__init__(
      name="ping", # Aqui você define o nome do comando
      description="reply with pong", # Aqui você define a descrição do comando(o que ele faz)
      callback=self.callback # Aqui você define a função que será executada ao chamar o comando, evite usar outro nome além de callback!
    )

  async def callback(self, interaction: Interaction): 
    await interaction.response.send_message("Pong!") # Responde ao usuário com a mensagem "Pong!"

# A função "setup" énecessária para adicionar o comando criado a árvore de comandos
# Sempre siga esse padrão para registrar o comando, a única coisa que vai mudar aqui é o nome da classe onde você definiu o comando
# Por exemplo, eu criei a classe com o nome "Ping" para o comando, então vou passar para app.add_command(Ping()) nessa ordem.
def setup(app: app_commands.CommandTree):
  app.add_command(Ping())
```

---

# Como criar comandos de prefixo/mensagem 
> 1. Crie um novo arquivo `.py` dentro de alguma sub-pasta da pasta `messages`(ex: messages/utils/ping.py)
> 2. Siga esse padrão de código para criar um novo comando de prefixo funcional:
```py
import discord 
from luna.core.message_register import MessageCommandRegister

# Use sempre esse padrão para criar a função principal do comando de prefixo
# message: discord.Message -> É sempre o primeiro paramêtro da função, pois em cada mensagem ao servidor, um evento de Mensagem do discord será disparado
# args: Aqui são os argumentos que o usuário pode enviar após o comando "<prefixo><nome> arg1, arg2 ..."
# Você pode acessar argumentos a partir do índice, exemplo: 
# !ping hello world -> arg[0] = "hello", arg[1] = "world"
async def ping_command(message: discord.Message, args):
  await message.reply("Pong!")

# A função "message_setup" é necessária para registrar o comando criado
# Siga esse padrão para registrar o comando
"""ao chamar o método "register_command_message()", passe os seguintes argumementos:
  1. Nome do comando: str 
  2. Nome da função principal do comando 
  Como no exemplo abaixo, eu estou registrando um comando de prefixo com o nome "ping" e passando logo em seguida o nome da função ping_command que faz o envio da mensagem "Pong!" ao usuário que chamou o comando 
"""
def message_setup(register: MessageCommandRegister):
  register.register_command_message("ping", ping_command)
```

---

# Caso não queira usar banco de dados
1. Remova ou comente a seguinte linha no arquivo `main.py`:
```py
from .config.luna_db import luna_db
```
### ⚠️ Atenção
> Ao remover o recurso de banco de dados, comandos padrões que vieram no projeto e interagem com o banco de dados(como o `cogs/utils/todolist.py` não irão funcionar, é recomendável deletar o comando também

---

# Caso não queira usar Gemini API 
1. Delete o arquivo `services/google_genai.py`(ou a pasta `services` caso não vá utilizar)
2. Recomendável deletar também o arquivo `services/instructions.txt` pois será desnecessário
### ⚠️ Atenção
> Ao remover o recurso de Gemini API, comandos padrões que vieram no projeto e interagem com o Gemimi API (como o `messages/utils/agent.py` não irão funcionar, é recomendável deletar o comando também

# Melhor recomendação
> Use a versão mais limpa do template(sem banco de dados nem google-genai), é só instalar as dependências, configurar token e prefixo, e iniciar o bot
> Para usar, clique **[aqui](https://github.com/kev1n999/luna-bot/tree/clean/template)**

--- 

# Se ocorrer algum problema ou bug
Caso ocorra algum problema, abra uma issue descrevendo o mesmo!
