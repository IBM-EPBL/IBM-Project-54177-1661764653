= {
  GREEN: 0,
  YELLOW: 1,
  RED: 2
}

var TrafficLight = function () {

  var count = 0

  // default state = red
  var currentState = 0;

  this.change = function(state) {
    if (count++ >= 10 ) return
    currentState = state
    this.go(currentState)
  }
  this.go = function(state) {
    if (currentState == LightState.GREEN) {
      console.log("Green --> for 1 minute")
      this.change(LightState.YELLOW)
    } 
    else if (currentState == LightState.YELLOW) {
      console.log("Yellow --> for 10 seconds")
      this.change(LightState.RED)
    } else if (currentState == LightState.RED) {
      console.log("Red --> for 1 minute");
      this.change(LightState.GREEN)
    } else {
      throw Error("Invalid State")
    }
  }
  this.start = function() {
    this.change(LightState.GREEN)
  }
}
