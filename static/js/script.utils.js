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

document.addEventListener("DOMContentLoaded", function(event) {
  var btn_state_span = document.getElementById('btn_state');
  setInterval(function() {
    if (!btn) {
      btn_state_span.innerHTML = "Кнопка нажата";
    } else {
      btn_state_span.innerHTML = "Кнопка не нажата";
    }
  }, 100);
});
