

$(document).ready(function () {
    $('#cat').click(function () {



        $('header').toggleClass('active');
        $('main').toggleClass('main');
    })

})

$('#home').click(function () {
    location.href = '/';
})
$('#myOrders').click(function () {
    location.href = '/myorders/';
})
$('#cart').click(function () {
    location.href = '/cart/';
})

$('#account').click(function () {
    location.href = '/account_settings/';
})


