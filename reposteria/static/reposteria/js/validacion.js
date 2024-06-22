$(document).ready(function() {
    $('form').on('submit', function(event) {
        // Prevent the form from submitting initially
        event.preventDefault();

        // Remove any existing error messages
        $('.error-message').remove();

        const firstName = $('#firstname').val();
        const lastName = $('#lastname').val();
        const nameRegex = /^[a-zA-Z]+$/; 
        if (firstName.length < 3 || !nameRegex.test(firstName) || lastName.length < 3 || !nameRegex.test(lastName)) {
            $('#firstname').after('<div class="error-message">El nombre y el apellido deben tener al menos 3 letras.</div>');
            return;
        }

        // Validación del teléfono
        const phone = $('#phone').val();
        if (phone.length !== 9 || isNaN(phone)) {
            $('#phone').after('<div class="error-message">El teléfono debe tener 9 números.</div>');
            return;
        }

        // Validación del tipo
        const type = $('#type').val();
        if (type === '--Sin Seleccionar--') {
            $('#type').after('<div class="error-message">Por favor selecciona un tipo.</div>');
            return;
        }

        // Validación del email
        const email = $('#email').val();
        const emailRegex = /[a-zA-Z]/; 
        if (!emailRegex.test(email)) {
            $('#email').after('<div class="error-message">El correo electrónico debe contener al menos una letra.</div>');
            return;
        }

        // Validación del mensaje
        const message = $('#message').val();
        if ($.trim(message) === '') {
            $('#message').after('<div class="error-message">Por favor escribe un mensaje.</div>');
            return;
        }

        // If all validations pass, submit the form
        this.submit();
    });

    // Check if the togglePassword element exists before adding event listener
    const togglePassword = document.querySelector('#togglePassword');
    if (togglePassword) {
        togglePassword.addEventListener('click', function (e) {
            // toggle the type attribute
            const password = document.querySelector('#inputPassword');
            const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
            password.setAttribute('type', type);
            // toggle the eye slash icon
            this.classList.toggle('fa-eye-slash');
        });
    }
});
