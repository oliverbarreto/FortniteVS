// The following code is based off a toggle menu by @Bradcomp
// source: https://gist.github.com/Bradcomp/a9ef2ef322a8e8017443b626208999c1
/*
(function() {
    var burger = document.querySelector('.burger');
    var menu = document.querySelector('#'+burger.dataset.target);
    burger.addEventListener('click', function() {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });
})();
*/

/* Dismisses the notification element */
/* TODO: and scrolls back the page to the top when flash message has been dismissed */
$(document).on('click', '.notification > button.delete', function() {
    $(this).parent().addClass('is-hidden');
    $('#flashMessages').remove();
    return false;
});

/* Scrolls the page to the bottom on load to the results divs*/
$(document).ready(function () {
    // Handler for .ready() called.
    $('html, body').animate({
        scrollTop: $('#players').offset().top
    }, 'slow');
});
