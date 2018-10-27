# flappybird-serial

Esse é o exemplo do flappybird que acompanha o pygamezero, adicionado com uma thread que faz a leitura da serial identificando o comando 'shake' permitindo que o microcontrolador interaja com o jogo.

## Requisitos

Python 2.7+
PyGameZero
Dependências no arquivo `requirements.txt`, apenas rode `pip -r requirements.txt`.

## Getting Started

Executar o script com os seguintes argumentos:
`python flappybird.py <porta>`
|||
|--------|----------------------------|
| `porta` | Porta serial utilizada, ex.: 'COM10' |
