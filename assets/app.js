/* LARGAMS FITNESS — reveal on scroll, mobile menu, spotlight, counters, WhatsApp form. No backend. */
(function(){
  var btn=document.querySelector('.hamburger'), nav=document.querySelector('.main-nav');
  if(btn&&nav){btn.addEventListener('click',function(){var open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',open?'true':'false');});}
  document.querySelectorAll('.main-nav a').forEach(function(a){a.addEventListener('click',function(){if(nav)nav.classList.remove('open');});});

  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});

  // Cursor spotlight, desktop pointer only
  var spot=document.querySelector('.spotlight');
  if(spot && window.matchMedia('(pointer:fine)').matches){
    var raf=null;
    document.addEventListener('mousemove',function(e){
      if(raf)return; raf=requestAnimationFrame(function(){spot.style.left=e.clientX+'px';spot.style.top=e.clientY+'px';raf=null;});
    });
  }
  // Buttons: press feedback is in CSS (scale .97). No magnetic drag on touch.

  // Animated counters — only for real, countable site facts (2 brands, 6 steps, 6 programs, 12 ABROFIT services)
  var cio=new IntersectionObserver(function(es){es.forEach(function(e){
    if(!e.isIntersecting)return; cio.unobserve(e.target);
    var end=parseInt(e.target.getAttribute('data-count'),10)||0, cur=0;
    var t=setInterval(function(){cur+=1; e.target.textContent=String(cur).padStart(2,'0'); if(cur>=end)clearInterval(t);},60);
  });},{threshold:.5});
  document.querySelectorAll('[data-count]').forEach(function(el){cio.observe(el);});

  // Contact form -> prefilled WhatsApp (no fake backend; stated on the contact page)
  var form=document.getElementById('enquiry-form');
  if(form){form.addEventListener('submit',function(ev){
    ev.preventDefault();
    var f=function(id){var el=document.getElementById(id);return el?el.value.trim():'';};
    var msg="Hi ABROFIT, new enquiry:%0AName: "+encodeURIComponent(f('f-name'))
      +"%0APhone: "+encodeURIComponent(f('f-phone'))
      +"%0AEmail: "+encodeURIComponent(f('f-email'))
      +"%0ACountry: "+encodeURIComponent(f('f-country'))
      +"%0AService: "+encodeURIComponent(f('f-service'))
      +"%0AMessage: "+encodeURIComponent(f('f-message'));
    window.open("https://wa.me/918137008663?text="+msg,"_blank");
  });}

  // Keep any data-wa elements in sync with config.js messages
  if(window.LARGAMS_CONFIG && window.waLink){
    document.querySelectorAll('[data-wa]').forEach(function(el){
      var key=el.getAttribute('data-wa');
      var msg=window.LARGAMS_CONFIG.messages[key]||window.LARGAMS_CONFIG.messages.general;
      el.setAttribute('href',window.waLink(msg));
    });
  }
  var y=document.getElementById('year'); if(y)y.textContent=new Date().getFullYear();
})();

/* v2: dropdown toggles (mobile accordion) + BMI calculator */
(function(){
  document.querySelectorAll('.drop-toggle').forEach(function(btn){
    btn.addEventListener('click', function(ev){
      ev.preventDefault(); ev.stopPropagation();
      var drop = btn.closest('.drop');
      var open = drop.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  var form = document.getElementById('bmi-form');
  if (form) {
    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var h = parseFloat(document.getElementById('bmi-height').value);
      var w = parseFloat(document.getElementById('bmi-weight').value);
      var out = document.getElementById('bmi-result');
      if (!h || !w || h < 50 || h > 250 || w < 20 || w > 400) {
        out.innerHTML = '<p>Please enter a height between 50–250 cm and a weight between 20–400 kg.</p>';
        return;
      }
      var bmi = w / ((h / 100) * (h / 100));
      var cat = bmi < 18.5 ? 'Underweight' : bmi < 25 ? 'Healthy weight' : bmi < 30 ? 'Overweight' : 'Obesity';
      var bands = ['Underweight: below 18.5', 'Healthy weight: 18.5 – 24.9', 'Overweight: 25 – 29.9', 'Obesity: 30 and above'];
      out.innerHTML = '<p>Your BMI</p><b>' + bmi.toFixed(1) + '</b><p>Category: <strong>' + cat + '</strong></p>'
        + '<div class="band">' + bands.map(function(b){
            return '<span class="' + (b.split(':')[0] === cat ? 'hit' : '') + '">' + b + '</span>';
          }).join('') + '</div>'
        + '<p class="small">General information only — not medical advice. For a plan built around your body and goals, book a free ABROFIT consultation.</p>';
    });
  }
})();

(function(){
  document.querySelectorAll('.drop-parent').forEach(function(b){
    b.addEventListener('click', function(){
      var drop = b.closest('.drop'); var open = drop.classList.toggle('open');
      var t = drop.querySelector('.drop-toggle'); if (t) t.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
})();

/* v6: Phase 1 — U-04 dropdown keyboard model + U-13 gallery lightbox */
(function(){
  // U-04: Escape closes every open dropdown and returns focus to its toggle (or parent button)
  document.addEventListener('keydown', function(ev){
    if (ev.key !== 'Escape') return;
    document.querySelectorAll('.drop.open').forEach(function(drop){
      drop.classList.remove('open');
      var t = drop.querySelector('.drop-toggle') || drop.querySelector('.drop-parent');
      if (t) { t.setAttribute('aria-expanded','false'); t.focus(); }
    });
  });
  // Keep aria-expanded in sync when a drop-parent button toggles (mobile accordion)
  document.querySelectorAll('.drop-parent').forEach(function(b){
    b.addEventListener('click', function(){
      var drop = b.closest('.drop');
      b.setAttribute('aria-expanded', drop.classList.contains('open') ? 'true' : 'false');
    });
  });
  // U-13: native <dialog> lightbox on the gallery page only (dialog exists only there)
  var dlg = document.getElementById('lightbox');
  if (!dlg) return;
  var img = document.getElementById('lightbox-img'), cap = document.getElementById('lightbox-caption'), lastFocus = null;
  function openFrom(fig){
    var im = fig.querySelector('img'); if (!im) return;
    var src = im.getAttribute('src');
    if (src && src.indexOf('images.unsplash.com') !== -1) src = src.replace(/w=\d+/, 'w=1600');
    img.setAttribute('src', src || ''); img.setAttribute('alt', im.getAttribute('alt') || '');
    var fc = fig.querySelector('figcaption'); cap.textContent = fc ? fc.textContent : (im.getAttribute('alt') || '');
    lastFocus = fig; dlg.showModal();
  }
  document.querySelectorAll('.masonry figure').forEach(function(fig){
    fig.addEventListener('click', function(){ openFrom(fig); });
    fig.addEventListener('keydown', function(ev){
      if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); openFrom(fig); }
    });
  });
  // Native Escape closes the dialog; returning focus to the figure that opened it
  dlg.addEventListener('close', function(){ if (lastFocus) lastFocus.focus(); });
})();
