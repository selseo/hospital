!function() {

  var today = moment();

  function Calendar(selector) {
    this.el = document.querySelector(selector);
    this.changelist = [];
    this.current = moment().date(1);
    this.events = this.getEventByMonth();
    this.draw();
    var current = document.querySelector('.today');
    if(current) {
      var self = this;
      window.setTimeout(function() {
        self.openDay(current);
      }, 500);
    }
  }

  Calendar.prototype.draw = function() {
    this.drawHeader();

    this.drawMonth();

  }

  Calendar.prototype.drawHeader = function() {
    var self = this;
    if(!this.header) {
      //Create the header elements
      this.header = createElement('div', 'header');
      this.header.className = 'header';

      this.title = createElement('h1');

      var right = createElement('div', 'right');
      right.addEventListener('click', function() { self.nextMonth(); });

      var left = createElement('div', 'left');
      left.addEventListener('click', function() { self.prevMonth(); });

      //Append the Elements
      this.header.appendChild(this.title); 
      this.header.appendChild(right);
      this.header.appendChild(left);
      this.el.appendChild(this.header);
    }

    this.title.innerHTML = this.current.format('MMMM YYYY');
  }

  Calendar.prototype.drawMonth = function() {
    var self = this;
    this.events = this.getEventByMonth();
    // event date & time
    this.events.forEach(function(ev) {
     //ev.date = self.current.clone().date(Math.random() * (29 - 1) + 1);
     ev.date = self.current.clone().date(ev.d);
   });
    
    
    if(this.month) {
      this.oldMonth = this.month;
      this.oldMonth.className = 'month out ' + (self.next ? 'next' : 'prev');
      this.oldMonth.addEventListener('webkitAnimationEnd', function() {
        self.oldMonth.parentNode.removeChild(self.oldMonth);
        self.month = createElement('div', 'month');
        self.backFill();
        self.currentMonth();
        self.fowardFill();
        self.el.appendChild(self.month);
        window.setTimeout(function() {
          self.month.className = 'month in ' + (self.next ? 'next' : 'prev');
        }, 16);
      });
    } else {
      this.month = createElement('div', 'month');
      this.el.appendChild(this.month);
      this.backFill();
      this.currentMonth();
      this.fowardFill();
      this.month.className = 'month new';
    }
  }

  Calendar.prototype.backFill = function() {
    var clone = this.current.clone();
    var dayOfWeek = clone.day();

    if(!dayOfWeek) { return; }

    clone.subtract('days', dayOfWeek+1);

    for(var i = dayOfWeek; i > 0 ; i--) {
      this.drawDay(clone.add('days', 1));
    }
  }

  Calendar.prototype.fowardFill = function() {
    var clone = this.current.clone().add('months', 1).subtract('days', 1);
    var dayOfWeek = clone.day();

    if(dayOfWeek === 6) { return; }

    for(var i = dayOfWeek; i < 6 ; i++) {
      this.drawDay(clone.add('days', 1));
    }
  }

  Calendar.prototype.currentMonth = function() {
    var clone = this.current.clone();

    while(clone.month() === this.current.month()) {
      this.drawDay(clone);
      clone.add('days', 1);
    }
  }

  Calendar.prototype.getWeek = function(day) {
    if(!this.week || day.day() === 0) {
      this.week = createElement('div', 'week');
      this.month.appendChild(this.week);
    }
  }

  Calendar.prototype.drawDay = function(day) {
    var self = this;
    this.getWeek(day);

    //Outer Day
    var outer = createElement('div', this.getDayClass(day));
    outer.addEventListener('click', function() {
      self.openDay(this);
    });

    //Day Name
    var name = createElement('div', 'day-name', day.format('ddd'));

    //Day Number
    var number = createElement('div', 'day-number', day.format('DD'));
    number.id = day.format('DD');

    //Events
    var events = createElement('div', 'day-events');
    this.drawEvents(day, events);

    outer.appendChild(name);
    outer.appendChild(number);
    outer.appendChild(events);
    this.week.appendChild(outer);
  }

  Calendar.prototype.drawEvents = function(day, element) {
    if(day.month() === this.current.month()) {
      var todaysEvents = this.events.reduce(function(memo, ev) {
        if(ev.date.isSame(day, 'day')) {
          memo.push(ev);
        }
        return memo;
      }, []);

      todaysEvents.forEach(function(ev, index) {
        var evSpan = createElement('span', ev.color);
        // evSpan.id =  'ev' + ((2*ev.d-1) + (index % 2));
        element.appendChild(evSpan);
      });
    }
  }

  Calendar.prototype.getDayClass = function(day) {
    classes = ['day'];
    if(day.month() !== this.current.month()) {
      classes.push('other');
    } else if (today.isSame(day, 'day')) {
      classes.push('today');
    }
    return classes.join(' ');
  }

  Calendar.prototype.openDay = function(el) {
    var details, arrow;
    var dayNumber = +el.querySelectorAll('.day-number')[0].innerText || +el.querySelectorAll('.day-number')[0].textContent;
    var day = this.current.clone().date(dayNumber);

    var currentOpened = document.querySelector('.details');

    //Check to see if there is an open detais box on the current row
    if(currentOpened && currentOpened.parentNode === el.parentNode) {
      details = currentOpened;
      arrow = document.querySelector('.arrow');
    } else {
      //Close the open events on differnt week row
      //currentOpened && currentOpened.parentNode.removeChild(currentOpened);
      if(currentOpened) {
        currentOpened.addEventListener('webkitAnimationEnd', function() {
          currentOpened.parentNode.removeChild(currentOpened);
        });
        currentOpened.addEventListener('oanimationend', function() {
          currentOpened.parentNode.removeChild(currentOpened);
        });
        currentOpened.addEventListener('msAnimationEnd', function() {
          currentOpened.parentNode.removeChild(currentOpened);
        });
        currentOpened.addEventListener('animationend', function() {
          currentOpened.parentNode.removeChild(currentOpened);
        });
        currentOpened.className = 'details out';
      }

      //Create the Details Container
      details = createElement('div', 'details in');

      //Create the arrow
      var arrow = createElement('div', 'arrow');

      //Create the event wrapper

      details.appendChild(arrow);
      el.parentNode.appendChild(details);
    }

    var first = true;
    var todaysEvents = this.events.reduce(function(memo, ev) {
      if(ev.date.isSame(day, 'day')) {
        memo.push(ev); // mark events on calendar
      }
      return memo;
    }, []);
    this.drawPatientList(el.childNodes[1].id);
    this.renderEvents(todaysEvents, details);

    arrow.style.left = el.offsetLeft - el.parentNode.offsetLeft + 27 + 'px';
  }

  Calendar.prototype.renderEvents = function(events, ele) {
    //Remove any events in the current details element
    var self = this;
    var currentWrapper = ele.querySelector('.events');
    var wrapper = createElement('div', 'events in' + (currentWrapper ? ' new' : ''));
    tmpEvent = this.events;
    events.forEach(function(ev) {
      var div = createElement('div', 'event');
      var square = createElement('div', 'event-category ' + ev.color);
      var span = createElement('span', '', ev.eventName);
      var patientSlot = createElement('span', '', ev.count + '/15');
  
      div.appendChild(span);
      div.appendChild(patientSlot);
      wrapper.appendChild(div);
});

if(!events.length) {
  var div = createElement('div', 'event empty');
  var span = createElement('span', '', 'No Events');

  div.appendChild(span);
  wrapper.appendChild(div);
}

if(currentWrapper) {
  currentWrapper.className = 'events out';
  currentWrapper.addEventListener('webkitAnimationEnd', function() {
    currentWrapper.parentNode.removeChild(currentWrapper);
    ele.appendChild(wrapper);
  });
  currentWrapper.addEventListener('oanimationend', function() {
    currentWrapper.parentNode.removeChild(currentWrapper);
    ele.appendChild(wrapper);
  });
  currentWrapper.addEventListener('msAnimationEnd', function() {
    currentWrapper.parentNode.removeChild(currentWrapper);
    ele.appendChild(wrapper);
  });
  currentWrapper.addEventListener('animationend', function() {
    currentWrapper.parentNode.removeChild(currentWrapper);
    ele.appendChild(wrapper);
  });
} else {
  ele.appendChild(wrapper);
}
}

Calendar.prototype.drawLegend = function() {
 var self = this;
 var legend = createElement('div', 'legend');
 var calendars = this.events.map(function(e) {
  return e.calendar + '|' + e.color;
}).reduce(function(memo, e) {
  if(memo.indexOf(e) === -1) {
    memo.push(e);
  }
  return memo;
}, []).forEach(function(e) {
  var parts = e.split('|');
  var entry = createElement('span', 'entry ' +  parts[1], parts[0]);
  legend.appendChild(entry);
});

this.el.appendChild(legend);
}

Calendar.prototype.drawPatientList = function(date) {
  var preparedData = getPatientList(this, date);
  var self = this;
  
  var mPatient = JSON.parse(preparedData['morning']);
  var aPatient = JSON.parse(preparedData['afternoon'])
  
  // Change List
  $("#change-list-div").empty();
  var self = this;

  var headingdiv = createElement('div', 'header');
  var heading = createElement('h3', '', 'Patient List');
  var patientWrapper = createElement('div', 'patient-wrapper');
  var morning = createElement('div', 'morning-div');
  var afternoon = createElement('div', 'afternoon-div');
  var morningHeading = createElement('h4', 'period-header', 'Morning');
  var afternoonHeading = createElement('h4', 'period-header', 'Afternoon');
  var morningPatient = this.listMorningPatient(mPatient, this.events[2*(date)-2].tid);
  var afternoonPatient = this.listAfternoonPatient(aPatient, this.events[2*(date)-1].tid);
  
  morning.appendChild(morningHeading);
  morning.appendChild(morningPatient);
  afternoon.appendChild(afternoonHeading);
  afternoon.appendChild(afternoonPatient);
  patientWrapper.appendChild(morning);
  patientWrapper.appendChild(afternoon);
  headingdiv.appendChild(heading);
  $('#change-list-div').append(headingdiv);
  $('#change-list-div').append(patientWrapper);
}

Calendar.prototype.listMorningPatient = function(patients,tid) {
    var patientList = createElement('ol', 'morning');
    patients.forEach(function(pt){
        var tmp_list = createElement('li', 'pid' + pt.fields.user, pt.fields.firstname + ' ' + pt.fields.lastname);
        tmp_list.addEventListener('click', function(){
          $('#m-name').html('Loading ...');
          $('#m-age').html('Loading ...');
          $('#m-gender').html('Loading ...');
          $('#m-causes').html('Loading ...');
          $('#m-symtoms').html('Loading ...');
          $('#modal-user-detail').modal('show');
          var pid = (this.className.substr(3));
          var tmp = getPatientAppointment(pid, tid);
          var info = JSON.parse(tmp['appointment'])[0].fields;
          var profile = JSON.parse(tmp['profile'])[0].fields;
          var age = (new Date()).getFullYear() - new Date(profile.birthdate).getFullYear();
          $('#m-name').html(pt.fields.firstname + ' ' + pt.fields.lastname );
          $('#m-age').html(age);
          $('#m-gender').html(profile.sex);
          $('#m-causes').html(info.cause.replace('<','&lt;'));
          $('#m-symtoms').html(info.symptom.replace('<','&lt;'));
          $('.viewfullprofile').on('click', function(){
            location.href = "/patient/" + pid;
          });

        });
         patientList.appendChild(tmp_list);
    });
    if(patients.length == 0) {
      patientList.appendChild(createElement('i', '', 'No Appointment'));
    }
    return patientList;
  }

  Calendar.prototype.listAfternoonPatient = function(patients,tid) {
    var patientList = createElement('ol', 'afternoon');
    patients.forEach(function(pt){
      var tmp_list = createElement('li', 'pid' + pt.fields.user, pt.fields.firstname + ' ' + pt.fields.lastname);
      tmp_list.addEventListener('click', function(){
          $('#m-name').html('Loading ...');
          $('#m-age').html('Loading ...');
          $('#m-gender').html('Loading ...');
          $('#m-causes').html('Loading ...');
          $('#m-symtoms').html('Loading ...');
          $('#modal-user-detail').modal('show');

          var pid = (this.className.substr(3));
          var tmp = getPatientAppointment(pid, tid);
          var info = JSON.parse(tmp['appointment'])[0].fields;
          var profile = JSON.parse(tmp['profile'])[0].fields;
          var age = (new Date()).getFullYear() - new Date(profile.birthdate).getFullYear();
          $('#m-name').html(pt.fields.firstname + ' ' + pt.fields.lastname );
          $('#m-age').html(age);
          $('#m-gender').html(profile.sex);
          $('#m-causes').html(info.cause);
          $('#m-symtoms').html(info.symptom);
          $('.viewfullprofile').on('click', function(){
            location.href = "/patient/" + pid;
          });
        });
          patientList.appendChild(tmp_list);
    });
    if(patients.length == 0) {
      patientList.appendChild(createElement('i', '', 'No Appointment'));
    }
    return patientList;
  }


  Calendar.prototype.nextMonth = function() {
    this.current.add('months', 1);
    this.next = true;
    this.draw();
  }

  Calendar.prototype.prevMonth = function() {
    this.current.subtract('months', 1);
    this.next = false;
    this.draw();
  }

  window.Calendar = Calendar;

  function createElement(tagName, className, innerText) {
    var ele = document.createElement(tagName);
    if(className) {
      ele.className = className;
    }
    if(innerText) {
      ele.innderText = ele.textContent = innerText;
    }
    return ele;
  }

  Calendar.prototype.getEventByMonth = function() {
    var thisMonthEvents = [];
    var endOfMonth = this.current.clone().endOf('month').date();
    // init time slots
    for(var idx=0; idx<endOfMonth; idx+=1){
      thisMonthEvents.push({eventName: 'Not Available', calendar: 'Not Available', color: 'red', d: idx+1, count: 0, tid: 0});
      thisMonthEvents.push({eventName: 'Not Available', calendar: 'Not Available', color: 'red', d: idx+1, count: 0, tid: 0});
    }
    // fetching registed time from backend
    var preparedData = getPrepareData(this);

    preparedData.forEach(function(pd){
      thisMonthEvents[((2*pd.date - 2)) + pd.period].eventName = thisMonthEvents[((2*pd.date - 2)) + pd.period].calendar = 'Available';
      thisMonthEvents[((2*pd.date - 2)) + pd.period].color = 'green';
      thisMonthEvents[((2*pd.date - 2)) + pd.period].count = pd.count;
      thisMonthEvents[((2*pd.date - 2)) + pd.period].tid = pd.tid;
    });
    // console.log(thisMonthEvents);
    return thisMonthEvents;
  }

function getPrepareData(date) {
    var  preparedData = [];
    ajaxSetup();
    $.ajax({
      type: "GET",
      url: "/app/gettimetable/",
      data : {
          "month": (date.current.month()+1),
          "year": date.current.year()
        },
      success: function(e){
        // console.log(e);
        e.forEach(function(pd){
          preparedData.push({tid: pd.pk, date: pd.fields.date, period: pd.fields.period == 'm'? 0 : 1, count: pd.fields.patientnum})
        })
        // console.log(preparedData);
      },
      error: function(rs, e){
         console.log(rs.responseText);
         console.log('Can\'t get your timetable');
      },
      async:false,
    })
    return preparedData;
  }

  function getPatientList(date, d) {
    var  preparedData = [];
    $.ajax({
      type: "GET",
      url: "/app/getpatientlist/",
      data : {
        "month": (date.current.month()+1),
        "year": date.current.year(),
        "date" : d
      },
      success: function(e){
        preparedData = e;
      },
      error: function(rs, e){
        console.log(rs.responseText);
     },
     async:false,
   })
return preparedData;
}

function getPatientAppointment(pid, tid) {
    ajaxSetup();
    var  preparedData = [];
    $.ajax({
      type: "POST",
      url: "/app/getpatientappointment/",
      data : {
        "pid" : pid,
        "tid" : tid
      },
      success: function(e){
        preparedData = e;
      },
      error: function(rs, e){
        console.log(rs.responseText);
     },
     async:false,
   })
return preparedData;
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



    }();

    !function() {

      function addDate(ev) {

      }

      var calendar = new Calendar('#calendar');

    }();

