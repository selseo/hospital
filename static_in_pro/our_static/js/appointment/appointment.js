'use strict';

class Appointment {
    constructor(aid, date, period, drid, drname, drdepartment, currentStatus) {
        this._aid = aid;
        this._date = date;
        this._period = period;
        this._drid = drid;
        this._drname = drname;
        this._drdepartment = drdepartment;
        this._currentStatus = currentStatus;
    }

    get aid() { return this._aid }
    set aid(aid) { this._aid = aid }

    get date() { return this._date }
    set date(date) {this._date = date}

    get period() { return this._period }
    set period(period) { this._period = period }
    
    get drid() { return this._drid }
    set drid(drid) { this._drid = drid }

    get drname() { return this._drname }
    set drname(drname) { this._drname = drname }

    get drdepartment() { return this._drdepartment }
    set drdepartment(drdepartment) { this._drdepartment = drdepartment }

    get currentStatus() { return this._currentStatus }
    set currentStatus(currentStatus) { this._currentStatus = currentStatus }

    reschedule(d, period) {
        // $.ajax({
    //     type: "POST",
    //     url: "/appointment/reschedule",
    //     data : {
    //         "aid" : aid,
    //         "date" : d,
    //         "period" : period
    //     },
    //     success: function(e){
    //          
    //     },
    //     error: function(e){
    //         // this line must be removed
    //         console.log(e);
    //     },
    //     async:false,
    // })
    }

    cancel() {
        if(this._currentStatus === 'Upcoming') {
                // $.ajax({
    //     type: "POST",
    //     url: "/appointment/cancelAppointment",
    //     data : {
    //         "aid" : aid
    //     },
    //     success: function(e){
    //          
    //     },
    //     error: function(e){
    //         // this line must be removed
    //         console.log(e);
    //     },
    //     async:false,
    // })
        } else {
            console.log('This appointment can not be cancelled.');
        }
    }

    getDoctorAvailableSlot() {
        let available = [];
        // $.ajax({
    //     type: "POST",
    //     url: "/appointment/getDoctorAvailableSlot",
    //     data : {
    //         "drid" : drid
    //     },
    //     success: function(e){
    //          available = e;
    //     },
    //     error: function(e){
    //         // this line must be removed
    //         console.log(e);
    //     },
    //     asyn:false,
    //})
        return available;
    }

}
