from app.validador_telefono import (
    validar_numero_fijo,
    validar_numero_movil
)


# ==========================
# CASOS VÁLIDOS
# ==========================

def test_fijo_con_parentesis_y_guion():
    # Arrange
    numero = "(55) 1234-5678"

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is True


def test_fijo_con_espacios():
    # Arrange
    numero = "55 1234 5678"

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is True


def test_fijo_sin_separadores():
    # Arrange
    numero = "5512345678"

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is True


def test_movil_valido():
    # Arrange
    numero = "6641234567"

    # Act
    resultado = validar_numero_movil(numero)

    # Assert
    assert resultado is True


# ==========================
# CASOS INVÁLIDOS
# ==========================

def test_lada_invalida():
    # Arrange
    numero = "9912345678"

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is False


def test_menos_de_10_digitos():
    # Arrange
    numero = "551234567"

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is False


def test_mas_de_10_digitos():
    # Arrange
    numero = "55123456789"

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is False


def test_contiene_letras():
    # Arrange
    numero = "55AB345678"

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is False


def test_parentesis_sin_cerrar():
    # Arrange
    numero = "(55 1234-5678"

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is False


def test_numero_vacio():
    # Arrange
    numero = ""

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is False


def test_numero_nulo():
    # Arrange
    numero = None

    # Act
    resultado = validar_numero_fijo(numero)

    # Assert
    assert resultado is False