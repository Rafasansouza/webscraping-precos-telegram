
# Webscraping de Preços com Notificação no Telegram

Este projeto realiza web scraping no Mercado Livre para monitorar o preço de um produto específico. Se o preço atingir o valor desejado, você será notificado automaticamente via Telegram.


## 🚀 Funcionalidades
- Coleta automática de preços de um produto via web scraping.
- Registro histórico de preços em CSV.
- Alerta automático no Telegram quando o preço for igual ou inferior ao definido.

## 📦 Requisitos
- Python 3.9+
- Conta no Telegram com Bot criado

## 🛠️ Instalação e Execução

### 1. Clone o repositório
```bash
git clone https://github.com/Rafasansouza/webscraping-precos-telegram.git
cd webscraping-precos-telegram
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Crie o arquivo `.env`
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
TOKEN_BOT_TELEGRAM=seu_token_aqui
CHAT_ID_TELEGRAM=seu_chat_id_aqui
```

### 5. Obtenha seu Token e Chat ID no Telegram
1. Acesse o Telegram e busque por `@BotFather`
2. Crie um novo bot com o comando `/newbot`
3. Copie o token fornecido e adicione ao `.env`
4. Envie uma mensagem qualquer para seu bot
5. Acesse o link abaixo substituindo o '<SEU_TOKEN>':
```
https://api.telegram.org/bot<SEU_TOKEN>/getUpdates
```
6. Envie uma mensagem para o seu bot e atualize a pagina anterior
7. Vai aparecer o seu ID e sua mensagem assim como do seu bot. Então, Copie o valor do campo `"chat":{"id":...}` e adicione como `CHAT_ID_TELEGRAM` no `.env`

### 6. Execute o projeto
```bash
python main.py
```

O script irá coletar os dados periodicamente e enviar uma mensagem no Telegram caso o preço atinja o valor definido. Não se esqueça de ajustar a variavel price_target para a sua necessidade.

---

## 📄 Histórico de Preços
Os dados coletados são armazenados em `hist_prices.csv` com as seguintes colunas:
- Preço
- Nome do produto
- Data/Hora
- URL do produto
Permitindo realizar análises temporais também, importando o csv para um power bi, por exemplo. 😊
