

function Pass(){
      const togglePassword = document.getElementById('togglePassword');
      console.log(togglePassword)
      // const password = document.querySelector('#id_password');

      togglePassword.addEventListener('click', function (e) {
          document.getElementById("id_password").style.backgroundImage="url(/static/image(1).png)";
          console.log("ddddddd")
        // toggle the type attribute
        // const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        // password.setAttribute('type', type);
        // // toggle the eye slash icon
        // this.classList.toggle('fa-eye-slash');
    });
      }