console.log("JavaScript Connected...");

function like(id) {

    let element = document.getElementById('like');
    let count = document.getElementById('count');

    $.get(`like/${id}`).then(response => {
        if (response['response'] === 'liked') {
            element.className = 'fa fa-heart';
            count.innerText = Number(count.innerText) + 1;
        } else {
            element.className = 'fa fa-hear-o';
            count.innerText = Number(count.innerText) - 1;
        }
    })
}
