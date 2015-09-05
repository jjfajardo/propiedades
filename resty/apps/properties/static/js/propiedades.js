/**
 * Created by gaspardzul on 5/09/15.
 */

var propiedades = {
  add:function(){

      $('#id_code').on('keyup',function(){
          var input = $(this);
          if(input.val()){
              validarCódigo(input);
          }else{
              input.removeAttr('style');
              $('#msj').html('').removeClass('alert-danger').removeClass('alert-success').addClass('alert-warning').append('<p>Ingresar Código</p>');
          }
      });

      function validarCódigo(input){
          $.ajax({
              url:'/ws/validate/code/',
              type:'POST',
              data:{'house_code':input.val()},
              success: function (response) {
                  if(response.available){
                      input.css('border','2px solid green');
                      $('#btnEnviar').removeAttr('disabled');
                      $('#msj').html('').removeClass('alert-danger').removeClass('alert-warning').addClass('alert-success').append('<p>Código Válido</p>');
                  }else{
                      $('#btnEnviar').attr('disabled','disabled');
                      input.css('border','2px solid red');
                       $('#msj').html('').removeClass('alert-success').removeClass('alert-warning').addClass('alert-danger').append('<p>Código inválido</p>');
                  }

              }
          });
      }
  }
};