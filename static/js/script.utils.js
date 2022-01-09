var onMobile;
onMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);


function waitFor(variable, callback) {
  var interval = setInterval(function() {
    if (window[variable] || last_data !== undefined) {
      clearInterval(interval);
      callback();
    }
  }, 200);
}

