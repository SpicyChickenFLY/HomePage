$(document).ready(function () {
    $(".form-signin").submit(function () {
        $.ajax({
            type: "POST",
            url: "/auth/signin/",
            data: $('.form-signin').serialize(),
        }).success(function (message) {
            console.log(message)
        }).fail(function (err) {
            console.log(err)
        })
        event.preventDefault() //阻止form表单默认提交
    });
});