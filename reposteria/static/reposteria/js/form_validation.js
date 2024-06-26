$(document).ready(function() {
    $('.formulario_contacto').on('submit', function(event) {
        var isValid = true;
        var nombre = $('#id_nombre').val().trim();
        var apellido = $('#id_apellido').val().trim();
        var telefono = $('#id_telefono').val().trim();
        var correo = $('#id_correo').val().trim();
        var mensaje = $('#id_mensaje').val().trim();
        
        // Validar el campo de nombre
        if (nombre === '') {
            alert('El campo de nombre es obligatorio.');
            isValid = false;
        }
        
        // Validar el campo de apellido
        if (apellido === '') {
            alert('El campo de apellido es obligatorio.');
            isValid = false;
        }
        
        // Validar el campo de teléfono
        if (telefono === '' || isNaN(telefono)) {
            alert('El campo de teléfono es obligatorio y debe ser numérico.');
            isValid = false;
        }
        
        // Validar el campo de correo
        if (correo === '') {
            alert('El campo de correo es obligatorio.');
            isValid = false;
        } else if (!validateEmail(correo)) {
            alert('El correo electrónico no es válido.');
            isValid = false;
        }
        
        // Validar el campo de mensaje
        if (mensaje === '') {
            alert('El campo de mensaje es obligatorio.');
            isValid = false;
        }
        
        if (!isValid) {
            event.preventDefault(); // Evita que el formulario se envíe si no es válido
        }
    });

    function validateEmail(email) {
        var re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return re.test(String(email).toLowerCase());
    }
});
