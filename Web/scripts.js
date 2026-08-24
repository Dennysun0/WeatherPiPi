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
                    <h2>Hoy</h2>
                        <p>
                            <strong>${formatearFecha(hoy)}</strong><br>
                            Mínima: ${datos[hoy].minima} °C<br>
                            Máxima: ${datos[hoy].maxima} °C
                        </p>
                `;


                contenedor.innerHTML += `<h2>Histórico</h2>`

                for(const dia of dias) {

                    if(dia === hoy){
                        continue;
                    }

                    contenedor.innerHTML += `
                        <p>
                            <strong>${formatearFecha(dia)}</strong><br>
                            Mínima: ${datos[dia].minima} °C<br>
                            Máxima: ${datos[dia].maxima} °C
                        </p>
                    `;
                }
            })
}

function formatearFecha(fecha){
    const partes = fecha.split("-");

    return `${partes[2]}/${partes[1]}/${partes[0]}`;
}

mostrarTemperaturas();