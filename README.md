# Calculadora de Áreas

Aplicação desktop em Python que calcula, em tempo real, a área de formas geométricas a partir das medidas informadas pelo usuário.

## O que o sistema faz

A calculadora trabalha com medidas em metros e calcula a área em metros quadrados para:

- quadrado;
- retângulo;
- triângulo;
- círculo.

Ao selecionar uma forma, o programa exibe seu desenho e apresenta apenas os campos necessários. O resultado é atualizado automaticamente durante a digitação, sem a necessidade de clicar em um botão.

## Como foi desenvolvido

O projeto foi dividido em dois módulos:

- `calculos_area.py`: contém as fórmulas e a validação das medidas;
- `interface_area.py`: contém a interface gráfica construída com Tkinter.

As fórmulas utilizadas são:

- Quadrado: lado × lado;
- Retângulo: base × altura;
- Triângulo: (base × altura) ÷ 2;
- Círculo: π × raio².

A aplicação aceita ponto ou vírgula como separador decimal, impede medidas negativas e mostra mensagens quando um valor é inválido.

## Tecnologias utilizadas

- Python 3
- Tkinter
- ttk
- módulo `math`

Não é necessário instalar bibliotecas externas.

## Como usar

Tenha o Python 3 instalado e clone o repositório:

```bash
git clone https://github.com/GPLeal-dev/calculadoradearea.git
cd calculadoradearea
```

Execute a interface:

```bash
python interface_area.py
```

No Windows, também é possível usar:

```bash
py interface_area.py
```

Depois:

1. selecione a forma geométrica;
2. informe as medidas em metros;
3. visualize o cálculo automático em m².

## Estrutura do projeto

```text
calculadoradearea/
├── calculos_area.py    # fórmulas e validações
└── interface_area.py   # janela, campos e desenhos
```

## Autor

Desenvolvido por [Gabriel Leal](https://github.com/GPLeal-dev).
