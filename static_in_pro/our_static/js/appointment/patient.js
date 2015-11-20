'use strict';

class Patient {
    constructor(pname) {
        this._pname = pname;


        this._appointmentList = [];
    }

    get pname() { return this._pname }
    set pname(pname) { this._pname = pname }

    get appointmentList() { return this._appointmentList }
    set appointmentList(appointmentList) { this._appointmentList = appointmentList }

    loadAppointment() {
        // $.ajax({
    //     type: "GET",
    //     url: "/appointment/getappointment",
    //     success: function(e){
    //          e.forEach(function(ap) {
    //              this._appointmentList.push(new Appointment(ap.aid, ap.date, ap.period, ap.drid, ap.drname, ap.drdepartment, ap.currentstatus));
    //          });
    //     },
    //     error: function(e){
    //         // this line must be removed
    //         console.log(e);
    //     },
    //     async:false,
    // })
    }

    getUpcomingAppointment() {
        let upcoming = {};
        let d = new Date();
        let today = d.getFullYear() + '/' + (d.getMonth() + 1) + '/' + d.getDate();
        this._appointmentList.forEach(function(ap) {
            ointments.forEach(function(ap) {
            if (ap.date >= today && ap.currentstatus == 'Upcoming') { 
                upcoming = ap; 
            } else {
                return upcoming;
            }
        });
        return upcoming;
    }

    getAppointmentNum() {
        return this._appointmentList.length;
    }

}

