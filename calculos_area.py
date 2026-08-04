"""Funções de cálculo e validação para a calculadora de áreas."""

import math


def _validar_medida(valor: float, nome: str) -> float:
    """Converte a medida para float e impede valores negativos."""
    try:
        medida = float(valor)
    except (TypeError, ValueError) as erro:
        raise ValueError(f"Digite um valor numérico para {nome}.") from erro

    if medida < 0:
        raise ValueError(f"{nome.capitalize()} não pode ser negativo.")

    return medida


def area_quadrado(lado: float) -> float:
    lado = _validar_medida(lado, "o lado")
    return lado**2


def area_retangulo(base: float, altura: float) -> float:
    base = _validar_medida(base, "a base")
    altura = _validar_medida(altura, "a altura")
    return base * altura


def area_triangulo(base: float, altura: float) -> float:
    base = _validar_medida(base, "a base")
    altura = _validar_medida(altura, "a altura")
    return (base * altura) / 2


def area_circulo(raio: float) -> float:
    raio = _validar_medida(raio, "o raio")
    return math.pi * raio**2
