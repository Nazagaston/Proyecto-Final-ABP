

CREATE TABLE Rol (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL
);
CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES Rol(id_rol)
);
CREATE TABLE Dispositivo (
    id_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(50) NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    pulgadas INT,
    tipo_sincronizacion VARCHAR(50),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);
CREATE TABLE Automatizacion (
    id_automatizacion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    hora TIME NOT NULL,
    accion VARCHAR(100) NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);
CREATE TABLE Escenario (
    id_escenario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);
CREATE TABLE Escenario_Dispositivo (
    id_escenario INT,
    id_dispositivo INT,
    accion_configurada VARCHAR(100),
    PRIMARY KEY (id_escenario, id_dispositivo),
    FOREIGN KEY (id_escenario) REFERENCES Escenario(id_escenario),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo)
);
CREATE TABLE Consumo (
    id_consumo INT PRIMARY KEY AUTO_INCREMENT,
    fecha_hora DATETIME NOT NULL,
    valor_kwh DECIMAL(6,2) NOT NULL,
    id_dispositivo INT,
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo)
);
