# BD-Evidencia-5

Este directorio contiene los scripts SQL correspondientes a la Evidencia 5 del proyecto **SmartHome**.  

---

## Contenido  

- **init.sql** → Definición de la base de datos y creación de tablas.  
- **queries.sql** → Inserción de datos iniciales (30 registros) y consultas simples de verificación.  

---

## Cómo ejecutar los scripts en un DBMS online  

Para esta evidencia utilizaremos **OneCompiler (MySQL)**:  
[https://onecompiler.com/mysql](https://onecompiler.com/mysql)  

### 1. Crear la base de datos (DDL)  

1. Abrir el enlace a OneCompiler.  
2. En el editor, copiar y pegar el contenido de **init.sql**.  
3. Ejecutar con el botón **Run ▶️**.  

Esto creará la base de datos **smarthome** con las tablas principales:  

- usuario  
- dispositivo  
- automatizacion  
- escenario  
- escenario_dispositivo  
- consumo  
- rol  

---

### 2. Insertar datos y consultas (DML)  

1. En el mismo editor, después de ejecutar el DDL, copiar y pegar el contenido de **queries.sql**.  
2. Ejecutar con el botón **Run ▶️**.  

Se insertarán datos de ejemplo (usuarios, dispositivos, automatizaciones, escenarios).  

Al final, el script incluye consultas como:  

```sql
SELECT * FROM usuario;
SELECT * FROM dispositivo;
SELECT * FROM automatizacion;
SELECT * FROM escenario;
SELECT * FROM consumo;
