📊 Prueba Técnica – Módulo de Importación y Análisis de Ventas en Odoo 18
🧾 Descripción del Proyecto

Este proyecto consiste en el desarrollo de un módulo personalizado para Odoo 18, orientado a la importación, gestión y análisis de datos de ventas provenientes de archivos Excel.

La solución permite la carga masiva de información comercial, su validación y almacenamiento estructurado dentro del sistema, habilitando posteriormente su análisis mediante herramientas nativas de Odoo como vistas Tree, Form, Graph y Pivot.

El objetivo principal es demostrar habilidades en el desarrollo de módulos en Odoo, manejo de datos externos, validación de información y generación de reportes analíticos para la toma de decisiones.

🎯 Objetivo de la Solución

Desarrollar un sistema que permita:

Importar ventas desde archivos Excel.
Validar la integridad y coherencia de los datos.
Almacenar la información en modelos personalizados de Odoo.
Facilitar el análisis de datos mediante vistas dinámicas.
Proporcionar un dashboard de ventas con métricas clave.
⚙️ Funcionalidades Implementadas
📥 Importación de archivos Excel mediante wizard.
🧠 Validación de datos obligatorios y reglas de negocio.
💾 Registro de ventas en modelo personalizado.
📊 Visualización de datos en vistas:
Lista (Tree View)
Formulario (Form View)
Gráficos (Graph View)
Vista Pivot para análisis multidimensional
🔎 Filtros de búsqueda por cliente, vendedor, producto y estado.
⚠️ Manejo de errores en la carga de información.
📊 Dashboard Analítico

El módulo permite analizar la información de ventas desde diferentes perspectivas:

Total vendido en el mes.
Número total de ventas registradas.
Ventas por vendedor.
Ventas por cliente.
Ventas por producto.
Ventas por estado.
Visualización mediante gráficos de barras y circulares.
Análisis detallado mediante vista Pivot.
🧱 Arquitectura del Módulo
models/ → Modelo de ventas importadas
wizard/ → Asistente de carga de archivos Excel
views/ → Vistas de interfaz (lista, formulario, gráficos, pivot y menú)
security/ → Control de acceso a los modelos
manifest.py → Configuración del módulo
🛠️ Tecnologías Utilizadas
Odoo 18
Python 3
OpenPyXL
XML (vistas Odoo)
PostgreSQL
🧠 Valor Técnico del Proyecto

Este desarrollo evidencia competencias en:

Creación de módulos personalizados en Odoo
Integración de datos externos mediante Excel
Implementación de lógica de negocio en Python
Validación y control de calidad de datos
Diseño de vistas analíticas para soporte de decisiones
Manejo de errores y experiencia de usuario
👨‍💻 Autor

Johan Esteban Rodriguez Duarte
