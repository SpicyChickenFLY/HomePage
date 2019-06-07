$(document).ready(function () {
    $(".blog-post").click(function () {
        // $(this).hide();

        url = "/blog/" + $(".blog-post-meta#id").text();
        alert(url);
        // window.location.href = url;
    });
});