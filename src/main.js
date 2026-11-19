// Conxegal — interacciones ligeras, sin dependencias
(function () {
  document.documentElement.classList.remove('no-js');

  // Menú móvil
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // Aparición suave al hacer scroll
  var items = document.querySelectorAll('.reveal');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!('IntersectionObserver' in window) || reduce) {
    items.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  }

  // Vídeo de cabecera: pausa/reproducción accesible y respeto a "reducir movimiento"
  var vid = document.querySelector('.page-hero video');
  var vbtn = document.querySelector('.video-ctrl');
  if (vid && vbtn) {
    if (reduce) { vid.removeAttribute('autoplay'); vid.pause(); }
    var sync = function () { vbtn.textContent = vid.paused ? vbtn.dataset.play : vbtn.dataset.pause; };
    vbtn.addEventListener('click', function () { if (vid.paused) { vid.play(); } else { vid.pause(); } sync(); });
    vid.addEventListener('play', sync); vid.addEventListener('pause', sync); sync();
  }

  // Formulario de muestras: compone un correo (web estática, sin servidor)
  var form = document.getElementById('sample-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var labels = JSON.parse(form.dataset.labels);
      var lines = [];
      Object.keys(labels).forEach(function (k) {
        var v = (d.get(k) || '').toString().trim();
        if (v) lines.push(labels[k] + ': ' + v);
      });
      var subject = form.dataset.subject + ' — ' + (d.get('empresa') || '');
      var href = 'mailto:' + form.dataset.to + '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(lines.join('\n'));
      window.location.href = href;
      var msg = document.getElementById('form-msg');
      if (msg) msg.textContent = form.dataset.ok;
    });
  }
})();
