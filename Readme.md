# 🚀 Repositorio de Prácticas de JSON Web Token (JWT)

![Estado del Proyecto](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PyJWT](https://img.shields.io/badge/PyJWT-2.14.0-blue?logo=jsonwebtokens&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?logo=jsonwebtokens&logoColor=00B9F1)
![Udemy Course](https://img.shields.io/badge/Curso-Backend%20Developer%20(Udemy)-ec1c24?logo=udemy&logoColor=white)

---

## 📖 Descripción del Proyecto

Este repositorio reúne el conjunto de prácticas, conceptos y ejemplos de código desarrollados a lo largo de mi aprendizaje sobre **JSON Web Tokens (JWT)** y la implementación de mecanismos de autenticación y autorización seguros en el ecosistema del desarrollo backend con **Python**. Abarca desde la anatomía y fundamentos de un token JWT hasta la creación de *Access Tokens* y *Refresh Tokens*, protección de endpoints, control de acceso basado en roles (*RBAC*), manejo de expiraciones y firma criptográfica mediante algoritmos simétricos (`HS256`) y asimétricos (`RS256`).

Todo el contenido forma parte de mi especialización académica orientada al desarrollo backend:

1. **Curso de Backend Developer (Udemy):** Estudio teórico sobre arquitectura de autenticación, diferencias entre sesiones e intermediarios de estado vs. tokens sin estado (*stateless*), seguridad en cabeceras HTTP y vectores de ataque comunes en tokens de acceso.
2. **Prácticas y Ejercicios en Python (`JWT`):** Implementación práctica de scripts en Python utilizando la librería `PyJWT` para generación, codificación, firma, decodificación y verificación de tokens de acceso, manejo de claims estándar (`exp`, `iat`, `nbf`), inspección de cabecera/payload y middlewares de autorización.

---

## 🎯 Objetivo

Consolidar el dominio técnico sobre el diseño, emisión, verificación y gestión del ciclo de vida de JSON Web Tokens (*JWT*) siguiendo los estándares del IETF (RFC 7519) y las buenas prácticas de la industria backend, logrando:

- Comprender la **estructura fundamental de un JWT** (*Header*, *Payload*, *Signature*) y la diferencia con autenticación basada en sesiones tradicionales.
- Dominar el uso de **Claims Estándar** (`exp`, `iat`, `nbf`, `sub`, `iss`) y **Claims Personalizados** para transportar contexto del usuario de forma segura.
- Generar y verificar tokens de **corta duración (Access Tokens)** y **larga duración (Refresh Tokens)** en Python utilizando `PyJWT`.
- Diferenciar y aplicar esquemas de firma **simétrica (`HS256`)** con clave secreta compartida y **asimétrica (`RS256`)** con pares de llaves pública/privada.
- Implementar **Middlewares de Autorización** para la extracción de tokens en la cabecera `Authorization: Bearer <token>` y validación de firma y expiración.
- Aplicar control de acceso granular (**RBAC**) filtrando permisos y roles directamente desde las declaraciones del token.

---

## 🛠️ Requerimientos Técnicos / Temas Cubiertos

Este proyecto cumple con los estándares exigidos para el aprendizaje integral de autenticación y seguridad con JWT:

### 1. Fundamentos de JWT
- ✅ **Concepto e Identidad:** Arquitectura *stateless* (sin estado) para APIs desacopladas.
- ✅ **Anatomía del Token:** Inspección del *Header* (algoritmo y tipo), *Payload* (datos del usuario/claims) y *Signature* (firma hash de integridad).
- ✅ **JWT vs Sesiones:** Comparativa de escalabilidad, uso de memoria en servidor y desacoplamiento de microservicios.

### 2. Generación y Manejo de JWT en Python
- ✅ **Uso de PyJWT:** Codificación (`jwt.encode`) y decodificación (`jwt.decode`) segura de datos.
- ✅ **Claims Temporales:** Aplicación estricta de `iat` (emisión), `nbf` (válido desde) y `exp` (expiración con `datetime.timezone.utc`).
- ✅ **Estrategia de Firma:** Uso de claves secretas seguras y algoritmos de hash criptográfico.

### 3. Autenticación y Protección de Endpoints
- ✅ **Flujo de Login:** Validación de credenciales y generación del token de acceso inicial.
- ✅ **Cabecera HTTP Bearer:** Extracción e inspección del encabezado `Authorization: Bearer <token>`.
- ✅ **Validación Criptográfica:** Verificación de firma y manejo de excepciones por token expirado (`ExpiredSignatureError`) o token alterado (`InvalidSignatureError`).

### 4. Control de Acceso y Refresh Tokens
- ✅ **Control de Acceso basado en Roles (RBAC):** Definición de roles (`admin`, `user`, `qa`) y scopes de permiso dentro del payload.
- ✅ **Ciclo de Vida Extendido:** Separación entre Access Tokens (15-30 min) y Refresh Tokens (días/meses).
- ✅ **Buenas Prácticas de Seguridad:** Prevención de fugas en `localStorage`, requerimiento de transmisión segura (HTTPS) y mitigación de Secret Keys débiles.

---

## 📁 Estructura del Repositorio

```text
JWT/
├── Files/
│   └── jwt_fundamentos/
│       ├── entorno_virtual/        # Entorno virtual aislado de Python (venv)
│       ├── crear_jwt.py            # Ejercicio: Generación y firma de tokens JWT con PyJWT
│       ├── ver_header.py           # Ejercicio: Decodificación e inspección del Header
│       ├── ver_payload.py          # Ejercicio: Decodificación y validación de Claims del Payload
│       └── ver_firma.py            # Ejercicio: Verificación criptográfica de la firma del token
├── Readme.md                       # Documentación principal del repositorio
└── Temario.md                      # Plan de estudios detallado del módulo JWT
```

---

## 💻 Entorno de Desarrollo y Requisitos

* **Lenguaje:** Python 3.10+
* **Gestor de Paquetes:** `pip`
* **Librerías Clave:** `PyJWT` (v2.14.0+)

---

## 🚀 Instalación y Ejecución

1. **Clonar o ingresar a la carpeta del proyecto:**
   ```bash
   cd "Files/jwt_fundamentos"
   ```

2. **Activar el Entorno Virtual:**
   * **PowerShell (Windows):**
     ```powershell
     .\entorno_virtual\Scripts\Activate.ps1
     ```
   * **Bash (Linux/macOS):**
     ```bash
     source entorno_virtual/bin/activate
     ```

3. **Instalar dependencias (en caso de recrear el entorno):**
   ```bash
   pip install PyJWT
   ```

4. **Ejecutar un script de prueba:**
   ```powershell
   python crear_jwt.py
   ```

---

## 🔒 Buenas Prácticas de Seguridad

* 🔑 **Gestión de Claves:** Mantener la `SECRET_KEY` fuera del control de versiones utilizando variables de entorno (`.env`).
* ⏱️ **Tiempos de Vida Cortos:** Asignar una expiración no mayor a 15-30 minutos para los Access Tokens.
* 🌐 **Protocolo Seguro:** Requerir siempre HTTPS en entornos de producción para evitar la interceptación de cabeceras `Authorization`.

---

## ✒️ Autor

* **Jorge Tamayo Cabello**  
* **Desarrollador Front-End**

---

## 📄 Licencia

Este repositorio es de carácter estrictamente académico y educativo. Todo el contenido es libre de ser consultado con fines de aprendizaje y referencia técnica.
