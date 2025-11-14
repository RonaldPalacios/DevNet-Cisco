import pytest
from biblioteca import Biblioteca  # importamos desde otro Archivo


# 1 Configuracion Inicial
def test_integracion_biblioteca():
    biblioteca = Biblioteca()

    # 2 Prueba de registro de Libro
    biblioteca.agregar_libro("Master en Cisco")
    assert "Master en Cisco" in biblioteca.libros

    # 3 Prueba Registro de Usuario
    biblioteca.registrar_usuarios("Ronald Palacios")
    assert "Ronald Palacios" in biblioteca.usuarios

    # 4 Prueba de libro Prestado
    assert biblioteca.prestar_libro("Master en Cisco", "Ronald Palacios")
    assert not biblioteca.libros["Master en Cisco"].disponible
    assert "Master en Cisco" in biblioteca.usuarios["Ronald Palacios"].libros_prestado

    # 5 Prueba de prestamos de libro no disponible
    with pytest.raises(Exception) as exinfo:
        biblioteca.prestar_libro("Master en Cisco", "Ronald Palacios")
    assert str(exinfo.value) == "Libro no disponible"

    # 6 Prueba de prestamos con libros inexistente
    with pytest.raises(Exception) as exinfo:
        biblioteca.prestar_libro("Libro Inexistente", "Ronald Palacios")
    assert str(exinfo.value) == "Libro no disponible"

    # 7 Prueba de libro con usuario no registrado
    with pytest.raises(Exception) as exinfo:
        biblioteca.agregar_libro("Nuevo Libro")
        biblioteca.prestar_libro("Nuebo Libro", "Usuario No registrado")
    assert str(exinfo.value) == "Usuario No registrado"
