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

3. Autenticación Básica: Login
    - Flujo típico: 
        - Usuario envía credenciales
        - API valida usuario
        - API genera JWT
        - API retorna el token
    - Frameworks populares:
        - Flask
        - FastAPI
        
4. Protección de Endpoints
    - Middleware / Dependency injection
    - Validación de:
        - Firma del token
        - Expiración 
        - Claims obligatorios
    - Extracción del usuario desde el token
    - Header obligatorio:
        Authorization: Bearer <token>

5. Manejo de Roles y Permisos
    - JWT con roles definidos en el token:
    admin * user * qa * otros
    - Autorización basada en:
        - Roles asignados
        - Scopes de permiso
    - Protección granular de endpoints según permisos

6. Refresh Tokens (Clave en Producción)
    - Diferencia:
        . Access Token: Corta duración (15-30 min)
        - Refresh Token: Larga duración (días/meses)
    - Flujo de renovación de tokens
    - Invalidación de refresh tokens
    - Rotación de tokens para mayor seguridad