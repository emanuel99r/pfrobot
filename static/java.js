var motor1=document.getElementById("motor1");
var motor2=document.getElementById("motor2");
var boton=document.getElementById("turnOnBtn");
boton.addEventListener('click',function(e){
var vdata = [motor1.value,motor2.value];
ydata = JSON.stringify(vdata);
console.log(`los datos son ${ydata}`);
$(document).ready(function() {
 
            $.ajax({
                type: "POST",
                url: "/",        
                dataType: "json",
                contentType: "application/json; charset=UTF-8",
                data: ydata,
                    //email : $('#emailInput').val()
                
                success: function(result) {
                    console.log(result);
             }
            });
            e.preventDefault();
        });
        });
