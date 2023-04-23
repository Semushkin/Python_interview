$(function (){
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function (){
                $("#modal-good").modal("show");
            },
            success: function (data) {

                $("#modal-good .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("url-data"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("body").html(data.html_good_list);
                    $("#modal-good").modal("hide");
                }
                else {
                    $("#modal-good .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };
    $(".js-create-good").click(loadForm);
    $(".js-good-create-form").submit(saveForm);
});