import re

# LADAS válidas para la actividad
LADAS_VALIDAS = {
    "664",  # Tijuana
    "55",   # CDMX
    "33",   # Guadalajara
    "81",   # Monterrey
    "222",  # Puebla
    "999",  # Mérida
    "477"   # León
}


def limpiar_numero(numero):
    """
    Elimina espacios, guiones y paréntesis.
    """
    return re.sub(r"[\s\-\(\)]", "", numero)


def formato_valido(numero):
    """
    Verifica formatos permitidos:
    (XX) XXXX-XXXX
    XX XXXX XXXX
    XXXXXXXXXX
    (XXX) XXX-XXXX
    XXX XXX XXXX
    """
    patron = (
        r'^(\(\d{2,3}\)\s?\d{3,4}-\d{4}'
        r'|\d{2,3}\s\d{3,4}\s\d{4}'
        r'|\d{10})$'
    )

    return bool(re.match(patron, numero))


def lada_valida(numero_limpio):
    """
    Verifica si inicia con alguna LADA válida.
    """
    for lada in LADAS_VALIDAS:
        if numero_limpio.startswith(lada):
            return True
    return False


def validar_numero_fijo(numero):
    """
    Valida un teléfono fijo mexicano.
    """

    if numero is None or numero.strip() == "":
        return False

    if not formato_valido(numero):
        return False

    numero_limpio = limpiar_numero(numero)

    if len(numero_limpio) != 10:
        return False

    if not numero_limpio.isdigit():
        return False

    return lada_valida(numero_limpio)


def validar_numero_movil(numero):
    """
    Valida un teléfono móvil mexicano.
    (Para la actividad se distingue mediante función separada)
    """

    if numero is None or numero.strip() == "":
        return False

    if not formato_valido(numero):
        return False

    numero_limpio = limpiar_numero(numero)

    if len(numero_limpio) != 10:
        return False

    if not numero_limpio.isdigit():
        return False

    return lada_valida(numero_limpio)