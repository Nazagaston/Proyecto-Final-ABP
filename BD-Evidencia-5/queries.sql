
INSERT INTO Rol (nombre) VALUES ('Admin'), ('Usuario');
INSERT INTO Usuario (nombre, correo, contraseña, rol_id) VALUES
('Lucas González', 'lucas@mail.com', '1234', 1),
('Nazarena Gastón', 'naza@mail.com', '1234', 2);
INSERT INTO Dispositivo (tipo, marca, modelo, pulgadas, tipo_sincronizacion, id_usuario) VALUES
('Televisor', 'Samsung', 'QLED55', 55, NULL, 1),
('Consola', 'Sony', 'PS5', NULL, NULL, 1),
('Luz RGB', 'Philips', 'Hue', NULL, 'WiFi', 1),
('Barra de Sonido', 'LG', 'Sound360', NULL, NULL, 1),
('Televisor', 'LG', 'OLED48', 48, NULL, 2),
('Luz RGB', 'Xiaomi', 'Yeelight', NULL, 'WiFi', 2),
('Router', 'TP-Link', 'AX50', NULL, NULL, 2),
('Televisor', 'Sony', 'Bravia', 50, NULL, 2),
('Computadora', 'HP', 'Pavilion', NULL, NULL, 1),
('Tablet', 'Apple', 'iPad', 11, NULL, 2);
INSERT INTO Automatizacion (nombre, hora, accion, id_usuario) VALUES
('Encendido Noche', '20:00:00', 'Encender todos', 1),
('Escena Gaming', '21:30:00', 'Encender PS5 y TV', 1),
('Luces de descanso', '22:00:00', 'Encender luces suaves', 2),
('Inicio Trabajo', '08:00:00', 'Encender PC y Luz', 1),
('Modo Relax', '19:00:00', 'Encender TV y luz cálida', 2);
INSERT INTO Escenario (nombre, descripcion, id_usuario) VALUES
('Modo Cine', 'TV + barra sonido + luces apagadas', 1),
('Modo Gaming', 'PS5 + TV + luces RGB', 1),
('Modo Lectura', 'Luz cálida encendida', 2),
('Modo Oficina', 'PC + Luz blanca', 2);
INSERT INTO Escenario_Dispositivo (id_escenario, id_dispositivo, accion_configurada) VALUES
(1,1,'Encendido'),
(1,4,'Encendido'),
(1,3,'Apagado'),
(2,2,'Encendido'),
(2,1,'Encendido'),
(2,3,'Encendido'),
(3,6,'Encendido'),
(4,9,'Encendido'),
(4,10,'Encendido');
INSERT INTO Consumo (fecha_hora, valor_kwh, id_dispositivo) VALUES
(NOW(), 0.50, 1),
(NOW(), 0.20, 2),
(NOW(), 0.05, 3),
(NOW(), 0.10, 4),
(NOW(), 0.40, 5),
(NOW(), 0.06, 6),
(NOW(), 0.15, 7),
(NOW(), 0.25, 8),
(NOW(), 0.80, 9),
(NOW(), 0.30, 10);
SELECT * FROM Rol;
SELECT * FROM Usuario;
SELECT * FROM Dispositivo;
SELECT * FROM Automatizacion;
SELECT * FROM Escenario;
SELECT * FROM Escenario_Dispositivo;
SELECT * FROM Consumo;
