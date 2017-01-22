// AJAX for posting
function translate_text(text, fromLang, toLang, actor){
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "translate/", //the endpoint
        type : "POST", //http method
        data : {
        	'text' : text,
        	'fLang': fromLang,
        	'tLang': toLang,
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            if (actor=='a') {
            	color = '#D6E1FF';
            }
            else{
            	color = '#FFF0D6';
            }
            if($('#table-translate:visible').length == 0){
                $('#table-translate').show();
            }
        	$('#text-translate').prepend(
        		"<tr style='background-color:"+color+";'>\
                  <td>"+json.text+"</td>\
                  <td>"+json.translation+"</td>\
                  <td><input data-id='"+json.id+"' type='button' class='btn btn-danger btn-sm error' value='Error'> </td>\
                </tr>"
        	);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$(function() {
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});


// <div class='row' style='border: 2px solid"+color+"; margin-top: 1%;'>\
//                     <div class='col-md-offset-2 col-md-4'>\
//                         <h4>"+ json.text +"</h4>\
//                     </div>\
//                     <div class='col-md-4'>\
//                         <h4>"+ json.translation +"</h4>\
//                     </div>\
//                     <div class='col-md-2 text-center'>\
//                         <form class='f-error' id='f-"+ json.id +"'>\
//                             <div class='form-group'>\
//                                 <input type='submit' class='btn btn-danger btn-sm' id='row-"+json.id+"' value='Error'>\
//                             </div>\
//                         </form>\
//                     </div>\
//                 </div>