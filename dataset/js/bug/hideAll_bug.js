
function hideAll(name, config) {
    if (name && Y.Transition) {
      if (typeof config === "function") {
        config = null;
      }
  
      if (!name.push) {
        if (typeof config === "function") {
          config = name;
        }
        name = "HIDE_TRANSITION";
      }
      this.transition(name, config);
    } else {
      this.hide();
    }
    return this;
  }