# Minicursos Data2Learning
## O que o twitter está pensando? Extraindo informações em redes sociais utilizando Python.

Esse projeto foi resultado de um minicurso de coleta de dados do twitter ministrado em 2016. 
Em março de 2018, resolvi retomá-lo para ministrar novamente o minicurso. Na ocasião foram coletados 
em torno de 600 tweets com as hashtags *#teambatman* e *#teamsuperman*. A proposta do minicurso era 
coletar os dados, fazer um rápido pré-processamento e exibir as informações em uma página web. 

Detalhes de configuração do ambiente utilizado e do material disponível do minicurso estão no site:

[http://www.data2learning.com/minicurso-o-que-o-twitter-esta-pensando/](http://www.data2learning.com/minicurso-o-que-o-twitter-esta-pensando/)

A seguir um breve resumo de como colocar o projeto para funcionar.

## Repositório

O repositório está orgaizado da seguinte forma: 

* **notebook:** jupyter notebook com o material do minicurso.
* **scripts:** scripts gerados a partir do material descrito nos notebooks.
* **web:** página web para exibir as informações coletadas

## Instalação das dependências

Para o projeto funcionar é necessário instalar algumas depedências que estão listadas no arquivo `requirements.txt`. Para 
instalar utilize o comando: 

```shell
pip install -r requirements.txt
```

O projeto utiliza python versão 2.x (Uma atualização para versão 3.x está sendo planejada para breve).

### API do Twitter

Para usar a API do Twitter é preciso se cadastrar em [apps.twitter.com](http://apps.twitter.com) e criar um App para obter 
as credenciais: Keys e Tokens. As credenciais utilizadas neste código foram desativadas. Uma breve explicação de como obter tais credenciais
pode se encontrada [aqui](http://www.data2learning.com/minicurso-o-que-o-twitter-esta-pensando/).

### Projeto Web

O projeto web exibe as informações coletadas e processadas. Foi utilizado o **flask** como framework e um banco de dados em **sqlite**. No 
entanto, por conta da política de uso da API do Twitter, os tweets devem ser coletados novamente já que não é permitido distribuir
os tweets coletados. 

Para inserir os tweets na base, execute o script `updadte_database.py` no diretório `web/db/files/`. 

Após coletar os tweets é preciso gerar os dados processados. Para isto execute o script `run.py` na pasta `web/scripts`.

Para executar o servidor web com a página, use: `python flask_app.py` no diretório raiz. 

**O projeto foi criado há 2 anos e estou melhorando algumas coisas. Qualquer dúvida e sugestões é só entrar em contato:**

[adolfo@data2learning.com](mailto:adolfo@data2learning.com) ou [@profadolfoguimaraes](www.instagram.com/profadolfoguimaraes) (instagram) 

