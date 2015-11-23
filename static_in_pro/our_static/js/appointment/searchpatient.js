function searchPatient(){
    console.log();
    var el = $(this).attr('id');
    var elval = $(this).val();
    if(elval == '') {
        $('#patientname').val('');
        $('#patientid').val('');
        $('#patientidcard').val('');
    } else {
        ajaxSetup();
        $.ajax({
            type: "GET",
            url: "/app/searchpatient/",
            data : {
                "pid" : el == 'patientid' ? elval : '',
                "pidcard" : el == 'patientidcard' ? elval : ''
            },
            success: function(e){
                console.log(e);
                $('#patientid').val(e[0].pk);
                $('#patientname').val(e[0].fields.firstname + '  ' + e[0].fields.lastname);
                $('#gotopatient').attr('href', './'+e[0].pk);
            },
            error: function(rs, e){
                console.log(rs.responseText);
            }
        })
    }
    
}

function addSearchPatientListener() {
    $('#patientid').change(searchPatient);
    $('#patientidcard').change(searchPatient);
}

function ajaxSetup() {
    $.ajaxSetup({ 
        beforeSend: function(xhr, settings) {
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
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        } 
    });
}

!function() {
    addSearchPatientListener();
}();
