function calculateOpenState() {
    var rank = 0;
    var today = new Date();
    var start = new Date(this.dateStarted);
    var end = new Date(this.dateCompleted);
  
    if (start <= today && today <= end) {
      rank = 5;
    } else {
      if (today < start) {
        rank = 1;
      } else if (today > end) {
        rank = 2;
      } else {
        rank = 3;
      }
    }
    return { state: STATES[rank], rank: rank };
  }