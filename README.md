# NET NET — Streaming Pessoal

O NET NET é um projeto de streaming pessoal desenvolvido para organizar e reproduzir vídeos por meio de uma interface web própria. O acesso remoto é realizado utilizando o Tailscale, permitindo acessar o servidor pela rede privada entre dispositivos conectados.

## Funcionalidades

- Interface web para exibição de filmes.
- Capas clicáveis para selecionar os vídeos.
- Reprodução de vídeos em uma nova guia.
- Organização dos conteúdos em uma grade de três colunas.
- Servidor HTTP desenvolvido em Python.
- Acesso remoto por meio do Tailscale.

## Tecnologias utilizadas

- HTML5 — estrutura da interface.
- CSS3 — estilização e organização visual.
- JavaScript — interação com os botões e abertura dos vídeos.
- Python — execução do servidor HTTP.
- Tailscale — conexão privada entre dispositivos.

## Estrutura do projeto

```text
NET-NET/
├── index.html
├── style.css
├── main.js
├── main.py
└── assets/
    ├── anime.png
    ├── anime.mp4
    ├── coraline.jpeg
    └── outros arquivos de mídia
```

## Como executar

### 1. Instale o Python

Verifique se o Python está instalado:

```bash
python3 --version
```

### 2. Configure os arquivos

Coloque os vídeos e suas respectivas imagens na pasta `assets/`. Configure os caminhos dos arquivos no `index.html`.

### 3. Configure o endereço do Tailscale

No arquivo `main.py`, ajuste o endereço IP exibido no terminal para o IP Tailscale do dispositivo servidor.

### 4. Inicie o servidor

No terminal, dentro da pasta do projeto, execute:

```bash
python3 main.py
```

O servidor utiliza a porta `8080`.

### 5. Acesse o streaming

Em outro dispositivo conectado à mesma rede Tailscale, abra o navegador e acesse:

```text
http://IP-TAILSCALE-DO-SERVIDOR:8080
```

Substitua `IP-TAILSCALE-DO-SERVIDOR` pelo endereço correto do computador que hospeda o projeto.

## Como adicionar filmes

1. Adicione a imagem e o vídeo à pasta `assets/`.
2. Crie um botão no `index.html` com a imagem correspondente.
3. Adicione um elemento `<video>` com um identificador exclusivo.
4. Configure o botão para chamar a função JavaScript `Video()` com o identificador do vídeo.

## Objetivo

O objetivo do NET NET é criar uma solução de streaming pessoal, simples e acessível, utilizando tecnologias web, Python e uma rede privada para acessar os conteúdos entre dispositivos.

## Segurança

O Tailscale permite conectar dispositivos por uma rede privada, mas o acesso deve ser configurado corretamente. O servidor HTTP deste projeto não implementa autenticação própria nem criptografia HTTPS. Evite expor a porta do servidor diretamente à internet e utilize apenas dispositivos autorizados na sua rede.

## Status do projeto

Em desenvolvimento.

## Licença

Defina uma licença antes de permitir o uso, a modificação ou a redistribuição do projeto por terceiros.
