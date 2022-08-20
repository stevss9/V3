//-----------------------------------INICIALIZACION DE VARIABLES-------------------------------------
let tarjetasDestapadas = 0;
let tarjeta1 = null;
let tarjeta2 = null;
let primerResultado = null;
let segundoResultado = null;
let movimientos = 0;
let aciertos = 0;
let temporizador = false;
let timer = 600;
let timepoRegresivoId = null;
let timerIncial = timer;
//----------------------------------IMPORTAMOS LOS SONIDOS-------------------------------------------
let corrAudio = new Audio('static/assets/sounds/acierto.wav');
let clicAudio = new Audio('static/assets/sounds/seleccion.wav');
//---------------------------------ESTADISTICAS DEL PUNTAJE-----------------------------------------
let mostrarMovimientos = document.getElementById('movimientos');
let mostrarAciertos = document.getElementById('aciertos');
let mostrarTiempo = document.getElementById('t-restante');

//--------------------------GENERAMOS NUMEROS ALEATORIOS DENTRO DE UN ARRAY-------------------------
let numeros = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8];
numeros = numeros.sort(() => { return Math.random() - 0.5 });
console.log(numeros);

//---------------------------------FUNCION DEL TIMER------------------------------------------------
function contarTiempo() {
    timepoRegresivoId = setInterval(() => {
        timer--;
        mostrarTiempo.innerHTML = `Tiempo: ${timer} segundos`;
        if (timer == 0) {
            clearInterval(timepoRegresivoId);
            bloquearTarjetas();
            loseAudio.play();
        }
    }, 1000);
}
//--------------------------------FUNCION DE BLOQUEAR LAS CARDS-------------------------------------
function bloquearTarjetas() {
    for (let i = 0; i <= 15; i++) {
        let tarjetaBloqueada = document.getElementById(i);
        tarjetaBloqueada.innerHTML = `<img src="static/assets/images/juego/${numeros[i]}.png" alt="">`;
        //tarjetaBloqueada.innerHTML = `<image src="{{url_for('static',filename = 'templates/static/resources/images/${numeros[i]}.png')}}" ></image>`;
        tarjetaBloqueada.disabled = true;
    }
}
//-------------------------------FUNCION PRINCIPAL DEL JUEGO----------------------------------------
function destapar(id) {
    //LLAMAMOS A LA FUNCION CREADA ANTERIORMENTE CONTAR TIEMPO PARA MOSTRAR LAS CARTAS SELECIONADAS
    //POR UN CIERTO TIEMPO HASTA COMPARAR SI SON IGUALES
    if (temporizador == false) {
        contarTiempo();
        temporizador = true;
    }
    tarjetasDestapadas++;
    console.log(tarjetasDestapadas);
    //VERIFICAMOS LA PRIMERA CARTA CON LA FIGURA CORRESPONDIENTE
    if (tarjetasDestapadas == 1) {
        //MUESTRA EL NUMERO DE LA CARTA GIRADA PRIMERA
        clicAudio.play();
        tarjeta1 = document.getElementById(id);
        primerResultado = numeros[id];
        tarjeta1.innerHTML = `<img src="static/assets/images/juego/${primerResultado}.png" alt="">`;
        //tarjeta1.innerHTML = `<image src="{{url_for('static',filename = 'static/assets/images/juego/${primerResultado}.png')}}" ></image>`;
        //DESABILITAMOS TEMPORALMENTE EL BOTON
        tarjeta1.disabled = true;
        //VALIDACION DE LA SEGUNDA CARTA
    } else if (tarjetasDestapadas == 2) {
        //MUESTRA EL NUMERO DE LA CARTA GIRADA SEGUNDA
        clicAudio.play();
        tarjeta2 = document.getElementById(id);
        segundoResultado = numeros[id];
        tarjeta2.innerHTML = `<img src="static/assets/images/juego/${segundoResultado}.png" alt="">`;
        //tarjeta2.innerHTML = `<image src="{{url_for('static',filename = 'templates/static/resources/images/${segundoResultado}.png')}}" ></image>`;
        //DESBILITAMOS LA CARTA TEMPORALMENTE
        tarjeta2.disabled = true;
        //AL SELECCIONAR DOS CARTAS AUMENTA 1 MOVIMIENTO
        movimientos++;
        mostrarMovimientos.innerHTML = `Movimientos: ${movimientos}`;
        //VALIDAMOS SI LAS CARTAS GIRADAS SON IGUALES
        if (primerResultado == segundoResultado) {
            //ENCERAMOS EL PRIMER RESULTADO
            tarjetasDestapadas = 0;
            corrAudio.play();
            //AUMENTAMOS LOS ACIERTOS
            aciertos++;
            mostrarAciertos.innerHTML = `Aciertos: ${aciertos}`;
            //VALIDAMOS SI GIRARON TODAS LAS CARTAS CORRECTAS
            if (aciertos == 8) {
                clearInterval(timepoRegresivoId);
                mostrarAciertos.innerHTML = `Aciertos: ${aciertos} 
                ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐<br>
                ⭐⭐⭐FELICIDADES LO ⭐⭐
                ⭐⭐⭐⭐LOGRASTE⭐⭐⭐⭐<br>`;
                /*mostrarTiempo.innerHTML = `Tiempo:  
                ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐<br>
                ⭐⭐SOLO TE DEMORASTE ${timerIncial - timer}⭐<br>
                ⭐⭐⭐⭐SEGUNDOS⭐⭐⭐⭐`;*/
                mostrarMovimientos.innerHTML = `Movimientos:<br>
                ⭐⭐⭐LO HICISTE EN⭐⭐⭐<br>
                ⭐⭐⭐ ${movimientos} MOVIMIENTOS⭐⭐<br>
                ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐`;
                
            }
            //SI EL TIMER LLEGA A 0 SE DESABILITARAN LOS BOTONES Y SE REVELARAN LAS CARTAS
        } else {
            //MOSTRAMOS MOMENTANEAMENTE LAS CARTAS AL SELECCIONARLA
            setTimeout(() => {
                tarjeta1.innerHTML = ' ';
                tarjeta2.innerHTML = ' ';
                tarjeta1.disabled = false;
                tarjeta2.disabled = false;
                tarjetasDestapadas = 0;
            }, 800);
        }
    }
}