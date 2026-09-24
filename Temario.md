# Temario

1. Fundamentos de JWT
    - ¿Qué es JWT y para qué se usa?
    - Estructura del token:
        - Header - Tipo de token y algoritmo
        - Payload (claims) - Datos del usuario
        - Signature - Firma para verificación
    - Claims estándar v/s personalizados
    - JWT v/s sesiones tradicionales
    - Ventajas y riesgos

2. Generación de JWT en Python
    - Librerias más usadas
        - PyJWT
        - python-jose
    - Creación de:
        - Access Token - Corta duración
        - Refresh Token - Larga duración
    - Secret key v/s Public/Private key (RS256)
    - Definición de expiración exp, lat, nbf