$(document).ready(function () {
    $(".blog-post").hover(
        function () {
            $(this).css("background-color", "rgba(200, 255, 200, 0.7)");
        },
        function () {
            $(this).css("background-color", "rgba(255, 127, 127, 0)");
        }
    );

    $(".blog-post").click(function () {
        url = "/blog/" + $(this).find("#id").text();
        window.location.href = url;
    });
});