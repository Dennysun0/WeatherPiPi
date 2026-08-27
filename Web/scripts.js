function mostrarTemperaturas(){
    
    fetch("/temperaturas")
            .then(respuesta => respuesta.json())
            .then(datos => {
                const contenedor = document.getElementById("temperaturas");

                // Obtenemos todas la claves de nuestro JSON
                const dias = Object.keys(datos);

                // Cogemos el último día de la lista después de ordenarla
                const hoy = dias.sort().at(-1);

                contenedor.innerHTML += `
                    <div class="temperatura-hoy">    
                        <h2>Hoy</h2>
                        <strong>${formatearFecha(hoy)}</strong><br>
                        <div class="temperaturas-extremos">
                            <div>
                                <span>Mínima</span>
                                <strong>${datos[hoy].minima} °C</strong>
                            </div>
                            <div>
                                <span>Máxima</span>
                                <strong>${datos[hoy].maxima} °C</strong>
                            </div>
                    </div>
                `;


                contenedor.innerHTML += `<h2>Histórico</h2>`

                for(const dia of dias) {

                    if(dia === hoy){
                        continue;
                    }

                    contenedor.innerHTML += `
                        <div class="temperatura-dia">
                            <p>
                                <strong>${formatearFecha(dia)}</strong><br>
                                Mínima: ${datos[dia].minima} °C<br>
                                Máxima: ${datos[dia].maxima} °C
                            </p>
                        </div>
                    `;
                }
            })
}

function formatearFecha(fecha){
    const partes = fecha.split("-");

    return `${partes[2]}/${partes[1]}/${partes[0]}`;
}

mostrarTemperaturas();