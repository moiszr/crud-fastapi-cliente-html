document.body.style.zoom = "95%";

async function CagarAgendaGET(url) {

    let datos = await fetch(url)
        .then(res => res.json())
        .then((agenda) => {
            return agenda;
        });

    return datos;
}

async function CrearCargar() {

    let tareasAgenda = await CagarAgendaGET('http://127.0.0.1:8000/agenda/');

    let tabla = document.getElementById('tbody');

    for (let k in tareasAgenda) {

        tareas = tareasAgenda[k];

        tr = document.createElement('tr');

        for (let x in tareas) {

            td = document.createElement('td');
            td.innerHTML = tareas[x];
            tr.appendChild(td);
        }

        tdOpc = document.createElement('td');
        tdOpc.innerHTML = `
        <button class="btn btn-danger" onclick="EliminarAgendaDelete(this)"><i class="far fa-trash-alt"></i></button>`;
        tr.appendChild(tdOpc);

        tabla.appendChild(tr);
    }
}

async function CrearAgendaPOST() {

    let nombre = document.getElementById("Nombre").value;
    let telefono = document.getElementById("Telefono").value;
    let correo = document.getElementById("Correo").value;

    TareaAgenda = {}
    TareaAgenda.nombre = nombre;
    TareaAgenda.telefono = telefono;
    TareaAgenda.correo = correo;

    let url = 'http://127.0.0.1:8000/agenda/';

    await fetch(url, {
            method: 'POST',
            body: JSON.stringify(TareaAgenda),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => console.log('Éxito:', response));
}

function EliminarAgendaDelete(btn) {
    
    let fila = btn.parentNode.parentNode;
    let id = fila.firstElementChild.innerHTML;
    console.log(id);
    
    let url = 'http://127.0.0.1:8000/agenda/';

    alertify.confirm("Se eliminara la tarea de la agenda con el ID " + id + "",
        function () {
            fetch(url + id, {
                method: 'DELETE'
            })
                .then(res => res.json())
                .catch(error => console.error('Error:', error))
                .then(response => console.log('Éxito:', response))
                .then(() => location.reload())
            alertify.success('Borrado');
        },
        function () {
            alertify.error('Cancelado');
        });
}