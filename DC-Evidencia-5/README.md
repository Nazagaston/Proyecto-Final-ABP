![Image](https://github.com/user-attachments/assets/63c62ed2-53dc-4dbb-9175-497dce5313e9)

Justificación del diagrama de clases

En el diagrama de clases adjunto se representa la estructura del sistema orientado a objetos, mostrando las clases que lo componen junto con sus atributos, métodos y las relaciones existentes entre ellas.

En cuanto a la visibilidad de los atributos, se definieron como privados aquellos que requieren un acceso restringido desde fuera de la clase, asegurando así la encapsulación. Por otro lado, se declararon algunos atributos como públicos para permitir su acceso directo desde otras partes del programa cuando resulte necesario.

La clase Dispositivo se estableció como clase base, ya que concentra los atributos y métodos comunes que describen el comportamiento general de cualquier dispositivo. A partir de ella se derivan diferentes clases específicas mediante una relación de herencia, lo cual facilita la especialización de los dispositivos. De esta forma, las subclases heredan atributos y métodos de la clase base, pero a la vez incorporan características propias, promoviendo la reutilización y extensión del código.

Además, se implementaron relaciones de agregación entre:

*GestorUsuarios y Usuario.

*GestorDispositivos y Dispositivo.

En ambos casos, el gestor funciona como un administrador de una lista de objetos, pero no controla de manera exclusiva su existencia. Por ejemplo, un Usuario puede existir de manera independiente, aunque al ser agregado a un GestorUsuarios este puede administrarlo (registrar, iniciar sesión, modificar rol, listarlo, etc.). Del mismo modo, un Dispositivo puede existir sin necesidad de un GestorDispositivos, aunque este último cumple el rol de gestionarlo (alta, baja, búsqueda, listado).


Por ultimo, se incluyó una relación de asociación entre las clases Dispositivo y Automatización, ya que ambas colaboran de manera bidireccional en los procesos de automatización. Esta asociación indica que un dispositivo puede estar vinculado a múltiples automatizaciones y viceversa, compartiendo atributos y métodos en el desarrollo de dicha funcionalidad.
