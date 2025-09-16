# Versión corregida del modelo relacional

En la versión corregida del modelo relacional se ajustaron las entidades y relaciones para que sean consistentes con el DER.  

## Claves y relaciones

Se definieron correctamente las **claves primarias (PK)** y las **claves foráneas (FK)**, además de indicar las cardinalidades con sus relaciones.

## Nuevas entidades y tablas

- Se incorporó la entidad **Rol** para asociar a los usuarios.  
- Se agregó la tabla intermedia **Escenario_Dispositivo** para vincular escenarios con dispositivos.  
- Se incorporó la entidad **Consumo** para registrar el uso energético de cada dispositivo.

## Beneficios del modelo

El modelo ahora refleja de manera clara y estructurada las dependencias entre entidades, mejora la coherencia con el DER y facilita futuras implementaciones del sistema.
