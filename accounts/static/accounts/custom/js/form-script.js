// let form = document.querySelector('form');

// form.addEventListener('submit', () => {
//     event.preventDefault();
//     console.log('haha');
//     form.submit();
// });


let errorList = document.querySelectorAll('ul.errorlist');

errorList.forEach(function(errorFeedback) {
    let label = errorFeedback.previousElementSibling;
    label.style.display = 'block';
});

