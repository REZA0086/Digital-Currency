$(document).ready(function(){$(".js-form-group__password-toggle").on("click",function(t){t.preventDefault(),t.stopPropagation(),$(this).toggleClass("show");t=$(this).attr("data-password"),t=$("#"+t);"password"===t.attr("type")?t.attr("type","text"):t.attr("type","password")})});