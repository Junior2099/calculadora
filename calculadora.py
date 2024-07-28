import flet as ft
from flet import colors
from decimal import Decimal, InvalidOperation

# Lista de botões da calculadora, com informações sobre operadores, cores de fonte e fundo.
botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
]

def main(page: ft.Page):
    # Configurações da janela da calculadora.
    page.bgcolor = '#000'
    page.window.resizable = False
    page.window.width = 300
    page.window.height = 430
    page.title = 'Calculadora'
    page.window.always_on_top = True

    # Elemento de texto que mostra o resultado da calculadora.
    result = ft.Text(value="0", color=colors.WHITE, size=20)
    
    # Função para calcular as operações da calculadora.
    def calculate(expression):
        try:
            # Substitui operadores '%' e '±' por operações matemáticas.
            expression = expression.replace('%', '/100').replace('±', '-')
            
            # Avalia a expressão de forma segura.
            value = Decimal(str(eval(expression)))
            
            # Retorna o resultado formatado.
            return f"{value:.5f}".rstrip('0').rstrip('.')
        except (InvalidOperation, SyntaxError, ZeroDivisionError):
            return 'Error'

    # Função para lidar com a seleção de botões da calculadora.
    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'):
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ('=', '%', '±'):
                value = calculate(value_at)

        result.value = value
        result.update()

    # Criação dos botões da calculadora.
    btn = [ft.Container(
            content=ft.Text(value=btn['operador'], color=btn['fonte']),
            alignment=ft.alignment.center,
            width=50,
            height=50,
            bgcolor=btn['fundo'],
            border_radius=100,
            on_click=select
        ) for btn in botoes]

    # Configuração dos elementos de exibição do resultado e do teclado.
    display = ft.Row(
        width=250, 
        controls=[result],
        alignment='end'
    )
    
    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end',
    )

    # Adição dos elementos à página.
    page.add(display)
    page.add(keyboard)

# Inicialização da aplicação.
ft.app(target=main)
