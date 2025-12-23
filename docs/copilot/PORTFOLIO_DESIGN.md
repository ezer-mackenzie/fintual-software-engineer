# Portfolio Management Module - Diseño y Decisiones

## Estructura de Carpetas

- **src/entities/**: Entidades principales (`Stock`, `Portfolio`).
- **src/services/**: Servicios auxiliares (no usado en este ejemplo simple).
- **src/tests/**: Pruebas unitarias.
- **main.py**: Punto de entrada del programa.
- **docs/**: Documentación y conversación.

## Solución Propuesta

- `Stock`: Representa una acción, con método para obtener el precio actual.
- `Portfolio`: Representa el portafolio, con métodos para calcular el valor total y rebalancear según la asignación objetivo.
- `rebalance()`: Calcula qué comprar/vender para alcanzar la distribución deseada.

## Ejecución

- Ejecutar `main.py` para ver el valor total y las acciones de rebalanceo.
- Ejecutar los tests en `src/tests/test_portfolio.py` para validar la lógica.

## Tipado y Documentación

- Todo el código está tipado y documentado con docstrings y comentarios.

## Conversación y Decisiones

- Se siguió una arquitectura limpia y simple, separando entidades, lógica y tests.
- Se priorizó la legibilidad y mantenibilidad.
- La conversación completa se documenta en `docs/conversation.md`.
