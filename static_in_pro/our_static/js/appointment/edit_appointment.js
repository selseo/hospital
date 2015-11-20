'use strict';

function getAppointmentByPage(page) {
    var preparedData = [];
    preparedData.push({aid : '1', date : '2015/11/24', period : 'Morning', drid : '1', drname : 'Peerapat Lamyai', drdepartment : 'Surgery', currentstatus : 'Upcoming'});
    preparedData.push({aid : '2', date : '2015/11/21', period : 'Afternoon', drid : '2', drname : 'Peerapat Lamyai', drdepartment : 'Surgery', currentstatus : 'Closed'});
    preparedData.push({aid : '3', date : '2015/11/02', period : 'Morning', drid : '1', drname : 'Peerapat Lamyai', drdepartment : 'Surgery', currentstatus : 'Cancelled'});
    preparedData.push({aid : '4', date : '2015/11/24', period : 'Morning', drid : '1', drname : 'Peerapat Lamyai', drdepartment : 'Surgery', currentstatus : 'Upcoming'});
    preparedData.push({aid : '5', date : '2015/11/24', period : 'Morning', drid : '1', drname : 'Peerapat Lamyai', drdepartment : 'Surgery', currentstatus : 'Upcoming'});
    preparedData.forEach(function(pd, idx, a) {
        appMapper[parseInt(pd.aid)] = idx;
    });
    // $.ajax({
    //     type: "GET",
    //     url: "/appointment/getappointmentbypage",
    //     data : {
    //         "page" : page
    //     },
    //     success: function(e){

    //     },
    //     error: function(e){
    //         // this line must be removed
    //         console.log(e);
    //     },
    //     async:false,
    // })
    return preparedData;
}

function getAvailable(drid) {
    // $.ajax({
    //     type: "GET",
    //     url: "/appointment/getavailable",
    //     data : {
    //         "drid" : drid
    //     },
    //     success: function(e){

    //     },
    //     error: function(e){
    //         // this line must be removed
    //         console.log(e);
    //     },
    //     async:false,
    // })
    var preparedData = [];
    preparedData.push({drid : 1, date : '2015/11/23', period : 'Morning', tid : '1'})
    preparedData.push({drid : 1, date : '2015/11/23', period : 'Afternoon', tid : '2'})
    preparedData.push({drid : 1, date : '2015/11/24', period : 'Afternoon' ,tid : '3'})
    preparedData.push({drid : 1, date : '2015/11/25', period : 'Morning' ,tid : '4'})
    preparedData.push({drid : 1, date : '2015/11/25', period : 'Morning', tid : '5'})
    timeslots = preparedData;
    timeslots.forEach(function (ts, idx, a) {
        timeMapper[ts.tid] = idx;
    })
    return preparedData;
}

function renderPostponeModal(aid, drid, row) {
    var app = appointments[appMapper[aid]];
    $('#m-name').html(app.drname);
    $('#m-dept').html(app.drdepartment);
    $('#m-date').html(app.date + ' (' + app.period + ')');
    $('.date-napp-selector').remove();
    var availables = getAvailable(drid);
    var select = document.createElement('select');
    select.className = 'form-control date-napp-selector';
    select.setAttribute('size', '1');
    availables.forEach(function(av) {
        var option = document.createElement('option');
        option.setAttribute('value', av.tid);
        var optionText = document.createTextNode(av.date + ' (' + av.period + ')');
        option.appendChild(optionText);
        select.appendChild(option);
    });
    $('#postpone-app-id').attr('data-aid', aid);
    $('#postpone-app-id').attr('data-row', row);
    $('#select-date-napp').append(select);
    $('#modal-postpone').modal('show');
}

function renderCancelModal(aid) {
    console.log('Render Cancel Modal');
    $('#modal-cancel').modal('show');
}

function renderConfirmationBox(){
    $('#modal-confirm').modal('show');
}

function createElementWithText(element, text) {
    var el  = document.createElement(element);
    el.appendChild(document.createTextNode(text));
    return el;
}

function createElementWithClassAndText(element, cl, text) {
    var el  = document.createElement(element);
    el.appendChild(document.createTextNode(text));
    el.className = cl;
    return el;
}

function createElementWithIcon(element, cl, text, icon){
    var el  = document.createElement(element);
    el.appendChild(icon);
    el.appendChild(document.createTextNode(text));
    el.className = cl;
    return el;
}

function drawAppointment(appointments) {
    $('.appointment-list').remove();
    appointments.forEach(function(ap, idx, a) {
        var apRow = document.createElement('tr');
        apRow.setAttribute('id', 'row' + ap.aid);
        apRow.className = 'appointment-list';
        var dateCol = createElementWithClassAndText('td', 'date'+idx,ap.date);
        var periodCol = createElementWithClassAndText('td', 'period' + idx, ap.period == 0 ? 'Morning' : 'Afternoon');
        var doctorCol = createElementWithClassAndText('td', 'drname' + idx, ap.drname);
        var departmentCol = createElementWithText('td',ap.drdepartment);
        var statusCol = document.createElement('td');
        var statusText = createElementWithClassAndText('p', ap.currentstatus == 'Upcoming' ? 'label label-success' : (ap.currentstatus == 'Closed' ? 'label label-primary' : 'label label-danger'), ap.currentstatus);
        statusCol.appendChild(statusText);

        var actionCol = document.createElement('td');
        actionCol.className = 'text-center';
        var postponeIcon = document.createElement('i');
        postponeIcon.className = 'fa fa-mail-forward';
        var cancelIcon = document.createElement('i');
        cancelIcon.className = 'fa fa-times';
        var actionPostpone = createElementWithIcon('a','btn btn-warning btn-xs',' Reschedule', postponeIcon);
        actionPostpone.setAttribute('href', './reschedule/' + ap.aid);
        // actionPostpone.addEventListener('click', function() {
        //     renderPostponeModal(ap.aid, ap.drid, idx);
        // });
        // this line is for temporary fix rendering problem, root cause should be found out.
        $(actionPostpone).css('margin-right', '4px');
        var actionCancel = createElementWithIcon('a', 'btn btn-danger btn-xs',' Cancel', cancelIcon);
        actionCancel.setAttribute('href', './cancel/' + ap.aid);
        // actionCancel.addEventListener('click', function() {
        //     renderCancelModal(ap.aid);
        // });
        if(ap.currentstatus !== 'Upcoming') {
            actionPostpone.setAttribute('disabled', 'disabled');
            actionCancel.setAttribute('disabled', 'disabled');
        }
        actionCol.appendChild(actionPostpone);
        actionCol.appendChild(actionCancel);

        apRow.appendChild(dateCol);
        apRow.appendChild(periodCol);
        apRow.appendChild(doctorCol);
        apRow.appendChild(departmentCol);
        apRow.appendChild(statusCol);
        apRow.appendChild(actionCol);
        $('#appointment-table').append(apRow);
    });

}



function getUpcomingAppointment(appointments) {
    var upcoming = {};
    var d = new Date();
    var today = d.getFullYear() + '/' + (d.getMonth() + 1) + '/' + d.getDate();
    appointments.forEach(function(ap) {
        if (ap.date >= today && ap.currentstatus == 'Upcoming') { 
            upcoming = ap; 
        } else {
            return upcoming;
        }
    });
    console.log(upcoming);
    return upcoming;
}

function drawUpcomingAppointment(upcoming) {
    if(upcoming.aid) {
        $('#upcoming-date').html(upcoming.date + ', ' + upcoming.period);
        $('#upcoming-doctor').html(upcoming.drname);
        $('#upcoming-department').html(upcoming.drdepartment);    
    } else {
        $('#upcoming-date').html('-');
        $('#upcoming-doctor').html('-');
        $('#upcoming-department').html('-');    
    }
}

function confirmCancelAppointment() {

}

function reschedule() {
    var tmp1 = $('.date-napp-selector').val();
    var tmp2 = $('#postpone-app-id').attr('data-row');
    var newtime = timeslots[timeMapper[tmp1]];
    $('.date' + tmp2).html(newtime.date);
    $('.period' + tmp2).html(newtime.period);
    // TODO : edit appointment in database
}

function getTotalPages(){
    // TODO : get total pages from server side
    return 3;
}

function createPage(text, val) {
    // <li><a href="javascript:void(0)">2</a></li>
    var li = document.createElement('li');
    li.className = 'paging';
    li.setAttribute('id', 'page'+val);
    var a = document.createElement('a');
    a.setAttribute('href', 'javascript:gotopage("' + val + '")');
    var atxt = document.createTextNode(text);
    a.appendChild(atxt);
    li.appendChild(a);
    return li;
}

function drawPagination(){
    var totalpages = getTotalPages();
    var page = createPage("«", 1);
    page.setAttribute('id', 'first');
    $('.pagination').append(page);

    page = createPage("1", 1);
    page.className = 'paging active';
    $('.pagination').append(page);
    
    for(var i = 2; i <= totalpages; i+=1) {
        page = createPage(i, i);
        $('.pagination').append(page);
    }
    var page = createPage("»", totalpages);
    page.setAttribute('id', 'last');
    $('.pagination').append(page);
}

function gotopage(n) {
    appointments = getAppointmentByPage(n);
    $('.paging').removeClass('active');
    $('#page'+n).addClass('active');
    drawAppointment(appointments);
}

var appointments = [];
var timeslots = [];
var appMapper = [];
var timeMapper = [];

$('document').ready(function(){
    appointments = getAppointmentByPage(1);
    var upcomingAppointment = getUpcomingAppointment(appointments);
    drawAppointment(appointments);
    drawUpcomingAppointment(upcomingAppointment);
    drawPagination();
});