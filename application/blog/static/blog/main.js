document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('.like').onclick = count;
});

let counter = 0;

function count(){
    counter++;
    document.querySelector('#counter').innerHTML = counter;
}