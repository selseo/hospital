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
			},
			error: function(rs, e){
				console.log(rs.responseText);
			}
		})
	}
	
}

function getDoctorList(){
	// TODO : get doctor list and add to $('#doctor') -- clear the existing one first
	$.ajax({
		type: "GET",
		url: "/app/getdoctorlist/",
		data : {
			"department" : $('#department').val()
		},
		success: function(e){
			doctorlist = JSON.parse(e);
			var el = document.createElement('option');
			var eltext = document.createTextNode("--- Select Doctor (Optional) ---");
			el.appendChild(eltext);
			$('#doctor').append(el);
			doctorlist.forEach(function(doctor){
				el = document.createElement('option');
				el.setAttribute('value', doctor.pk);
				el.setAttribute('id', 'doc' + doctor.pk);
				eltext = document.createTextNode(doctor.fields.firstname + ' ' + doctor.fields.lastname);
				el.appendChild(eltext);
				$('#doctor').append(el);
				console.log(el);
			});
			
		},
		error: function(rs, e){
			console.log(rs.responseText);
		}
	})
	addSelectDoctorListener();
}

function getAppointmentList(){
	// TODO : get appointment list and add to $('#appointment') -- clear the existing one first
	// console.log($('#doctor').val());
	$.ajax({
		type: "GET",
		url: "/app/getappointmentlist/",
		data : {
			"doctor" : $('#doctor').val()
		},
		success: function(e){
			// doctorlist = JSON.parse(e);
			// doctorlist.forEach(function(doctor){
			// 	var el = document.createElement('option');
			// 	el.setAttribute('value', doctor.pk);
			// 	var eltext = document.createTextNode(doctor.fields.firstname + ' ' + doctor.fields.lastname);
			// 	el.appendChild(eltext);
			// 	$('#doctor').append(el);
			// 	console.log(el);
			// });
			console.log(e);
			timelist = JSON.parse(e);
			timelist.forEach(function(t){
				console.log(t.fields.date);
				var el = document.createElement('option');
				el.setAttribute('value', t.pk);
				el.setAttribute('id', 'app'+t.pk);
				var eltext = document.createTextNode(t.fields.date + ', ' + (t.fields.period == 'm'? "Morning" : "Afternoon"));
				el.appendChild(eltext);
				$('#appointment').append(el);
			})
		},
		error: function(rs, e){
			console.log(rs.responseText);
		}
	})
}


function addSearchPatientListener() {
	$('#patientid').change(searchPatient);
	$('#patientidcard').change(searchPatient);
}

function addSelectDepartmentListener(){
	$('#department').change(getDoctorList);
}

function addSelectDoctorListener(){
	$('#doctor').change(getAppointmentList);
	// console.log($('#doctor').val());
}

function addSubmitButtonListener(){
	$('#submit-button').on('click', function(){
		$('#s-name').html($('#patientname').val());
		$('#s-department').html($('#department').val());
		$('#s-doctor').html($('#doc'+$('#doctor').val()).html());
		$('#s-date').html($('#app' + $('#appointment').val()).html());
		$('#s-cause').html($('#cause').val().replace('<','&lt;'));
		$('#s-symptom').html($('#symptom').val().replace('<','&lt;'));
		$('#modal-summary').modal('show');
	});
}

function submitForm(){
	ajaxSetup();
	$.ajax({
		type: "POST",
		url: "/app/show/bystaff",
		data: $('#appointment-form').serialize(), // get the form data
		success: function(e){
			console.log(e);
			if(e == 'success') {
				$('#modal-summary').modal('hide');
				$('#modal-success').modal('show');

				setTimeout(function(){
					location.href = 'http://www.google.com';
				}, 4500);
			}
		},
		error: function(rs, e){
			console.log(rs.responseText);
			$('#modal-summary').modal('hide');
			$('#modal-fail').modal('show');
			setTimeout(function(){
				$('#modal-fail').modal('hide');
			}, 1500);
		}
	})
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
	addSelectDepartmentListener();
	addSubmitButtonListener();
}();
