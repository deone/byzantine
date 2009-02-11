$(function()    {

        document.forms.login.username.focus();

        validateLogin();

});


function validateLogin()    {

        $("#login").validate({

                rules:  {
                        username: "required",
                        password: "required"
                },

                messages:   {
                        username: "Your user name is required",
                        password: "Your password is required"
                },

                submitHandler: function()   {

                        var email = $("#username").val();
                        var password = $("#password").val();
                        var url = "/libman/login";

                        var data = "username=" + email + 
                                "&password=" + password;

                        login(data, url);

                }

        });

}


function login(data, url)   {

        $.ajax({

                url: url,
                type: "POST",
                data: data,
                dataType: "json",

                success: function(response) {
                        if (response.data.body == false)   {
                            $("#login-error")
                                .addClass("err")
                                .html("Invalid user name and/or password").show();
                        } else  {
                            document.location = "/librarymanager/dashboard";
                        }

                }

        });

}
