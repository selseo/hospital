!function () {
    'use strict';
    var today = moment();

    function Calendar(selector) {
        //console.log(events);
        this.el = document.querySelector(selector);
        this.changelist = [];
        this.current = moment().date(1);
        this.events = this.getEventByMonth();
        this.draw();
        var current = document.querySelector('.today');
        if (current) {
            var self = this;
            window.setTimeout(function () {
                self.openDay(current);
            }, 500);
        }
    }

    Calendar.prototype.draw = function () {
        //Create Header
        this.drawHeader();

        //Draw Month
        this.drawMonth();

        this.drawLegend();

        this.drawChanges();
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
      // TODO : checkout this
      todaysEvents.forEach(function(ev, index) {
        var evSpan = createElement('span', ev.color);
        evSpan.id =  'ev' + ((2*ev.d-1) + (index % 2));
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

      var toggleButtonSection = createElement('section', 'toggle-button');
      var toggleButtonDiv = createElement('div', 'checkbox');
      var toggleButtonInput = createElement('input','');
      toggleButtonInput.type = 'checkbox';
      var patientSlot = createElement('span', '', ev.count + '/15');
      if(ev.eventName == 'Available')
        toggleButtonInput.checked = 'checked';
      
      toggleButtonInput.addEventListener('click', function(){
        if($(this).is(":checked")) {
          $(this).parent().parent().next().html('Available');
          if($(this).parent().parent().parent().is(':first-child')){
            $('#ev'+ (2*ev.d-1)).removeClass('red').addClass('green');
            ev.eventName = 'Available';
            console.log(ev.d);
            self.changelist[(2*ev.d-1)] = 'Available';
            if(ev.calendar == 'Not Available')
             self.changelist[(2*ev.d-1)] = 'Available';
           else 
            delete self.changelist[(2*ev.d-1)];
        } else {
         $('#ev'+ ((2*ev.d-1)+1)).removeClass('red').addClass('green');
         ev.eventName = 'Available';
         self.changelist[(2*ev.d-1)+1] = 'Available';
         if(ev.calendar == 'Not Available')
           self.changelist[(2*ev.d-1)+1] = 'Available';
         else 
          delete self.changelist[(2*ev.d-1)+1];
      }
    } else {
      $(this).parent().parent().next().html('Not Available');
      if($(this).parent().parent().parent().is(':first-child')){
            // change dot color
            $('#ev'+ (2*ev.d-1)).removeClass('green').addClass('red');
            ev.eventName = 'Not Available';
            if(ev.calendar == 'Available')
              self.changelist[(2*ev.d-1)] = 'Not Available';
            else 
              delete self.changelist[(2*ev.d-1)];
          } else {
           $('#ev'+ ((2*ev.d-1)+1)).removeClass('green').addClass('red');
           ev.eventName = 'Not Available';
           if(ev.calendar == 'Available')
            self.changelist[(2*ev.d-1)+1] = 'Not Available';
          else 
            delete self.changelist[(2*ev.d-1)+1];
        }
      }
      self.drawChanges();
    })
var toggleButtonLabel = createElement('label', '');

toggleButtonDiv.appendChild(toggleButtonInput);
toggleButtonDiv.appendChild(toggleButtonLabel);
toggleButtonSection.appendChild(toggleButtonDiv);
div.appendChild(toggleButtonSection);
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

Calendar.prototype.drawChanges = function() {
    // Change List
    $("#change-list-div").empty();
    var self = this;
    var changes = createElement('ul', 'change-list');
    // TODO : edit changelist
    this.changelist.forEach(function(cl, index){
     var tmp = createElement('li', '', (self.current.year() + '/' + (self.current.month()+1) + 
      '/' + (Math.floor((index+1)/2)) + (index%2==1? ' - Morning ' : ' - Afternoon ') + 'is set to ' + cl));
     changes.appendChild(tmp);
   })
    var heading = createElement('h3', '', 'Patient List');

    $('#change-list-div').append(heading);
    $('#change-list-div').append(changes);
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
      thisMonthEvents.push({eventName: 'Not Available', calendar: 'Not Available', color: 'red', d: idx+1, count: 0});
      thisMonthEvents.push({eventName: 'Not Available', calendar: 'Not Available', color: 'red', d: idx+1, count: 0});
    }
    // fetching patient details from server-side
    var preparedData = loadData(this);
    this.markAvailable(preparedData.available);
    this.listPatient(preparedData.patients)
    return thisMonthEvents;
  }

  Calendar.prototype.markAvailable = function(available) {
    // this function will mark all available periods in currently selected month regarding to data loaded

    available.forEach(function(pd){
      thisMonthEvents[((2*pd.date - 2)) + pd.period].eventName = thisMonthEvents[((2*pd.date - 2)) + pd.period].calendar = 'Available';
      thisMonthEvents[((2*pd.date - 2)) + pd.period].color = 'green';
    });
  }

  Calendar.prototype.listPatient = function(patients, date) {
    // this function will list all patients appointed in currently selected date on patient-list-div
  }

function loadData(date) {
    let preparedData = [];
    // $.ajax({
    //   type: "GET",
    //   url: "/checktimetable/getdata/",
    //   data : {
    //       "month": (date.current.month()+1),
    //       "year": date.current.year()
    //     },
    //   success: function(e){
    //     // TODO : do some logic here by adding results to preparedData's array
    //     // should get two kinds of data -> 1. doctor available period for red/green dot in calendar and
    //     //                                 2. patient details for each period
    //     console.log(preparedData);
    //   },
    //   error: function(e){
    //      alert('Can\'t fetch your timetable');
    //      console.log(e);
    //   },
    //   async:false,
    // })
    preparedData = {
      'available' : [
        {date: '', period: ''}
      ],
      'patients' : [
        {date: '', period: '', patients: []}
      ]
    }
    return preparedData;
  }

    }();

    !function() {
      var calendar = new Calendar('#calendar');
    }();

