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
    var unitInputs = form.querySelectorAll('input[name="bmi-unit"]');
    var metricFields = document.getElementById('bmi-metric-fields');
    var imperialFields = document.getElementById('bmi-imperial-fields');
    function syncUnits(){
      var u = form.querySelector('input[name="bmi-unit"]:checked');
      var imp = u && u.value === 'imperial';
      if (metricFields) metricFields.style.display = imp ? 'none' : 'block';
      if (imperialFields) imperialFields.style.display = imp ? 'block' : 'none';
    }
    unitInputs.forEach(function(r){ r.addEventListener('change', syncUnits); });
    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var out = document.getElementById('bmi-result');
      var checked = form.querySelector('input[name="bmi-unit"]:checked');
      var imp = checked && checked.value === 'imperial';
      var hCm, wKg;
      if (imp) {
        var ft = parseFloat(document.getElementById('bmi-height-ft').value);
        var inch = parseFloat(document.getElementById('bmi-height-in').value);
        var lb = parseFloat(document.getElementById('bmi-weight-lb').value);
        if (isNaN(ft) || isNaN(inch) || isNaN(lb)) { out.innerHTML = '<p>Please enter your height (ft and in) and weight (lb).</p>'; return; }
        hCm = (ft * 12 + inch) * 2.54; wKg = lb * 0.45359237;
      } else {
        hCm = parseFloat(document.getElementById('bmi-height').value);
        wKg = parseFloat(document.getElementById('bmi-weight').value);
        if (!hCm || !wKg) { out.innerHTML = '<p>Please enter your height (cm) and weight (kg).</p>'; return; }
      }
      if (hCm < 50 || hCm > 250 || wKg < 20 || wKg > 400) {
        out.innerHTML = '<p>Please enter a height between 50\u2013250 cm and a weight between 20\u2013400 kg.</p>';
        return;
      }
      var hm = hCm / 100;
      var bmi = wKg / (hm * hm);
      var cat = bmi < 18.5 ? 'Underweight' : bmi < 25 ? 'Healthy weight' : bmi < 30 ? 'Overweight' : 'Obesity';
      var low = 18.5 * hm * hm, high = 24.9 * hm * hm;
      var diff = bmi < 18.5 ? 'Gain ' + (low - wKg).toFixed(1) + ' kg to reach the healthy range.' : bmi >= 25 ? 'Lose ' + (wKg - high).toFixed(1) + ' kg to reach the healthy range.' : 'You are in the healthy range.';
      var pct = Math.max(0, Math.min(100, (bmi - 14) / 26 * 100));
      var genderEl = document.getElementById('bmi-gender');
      var gender = genderEl ? genderEl.value : '';
      var waist = parseFloat(document.getElementById('bmi-waist') ? document.getElementById('bmi-waist').value : '');
      var neck = parseFloat(document.getElementById('bmi-neck') ? document.getElementById('bmi-neck').value : '');
      var hip = parseFloat(document.getElementById('bmi-hip') ? document.getElementById('bmi-hip').value : '');
      var hIn = hCm / 2.54;
      var bf = null;
      if (gender === 'male' && waist && neck && waist > neck) {
        bf = 86.010 * Math.log10((waist - neck) / 2.54) - 70.041 * Math.log10(hIn) + 36.76;
      } else if (gender === 'female' && waist && neck && hip && (waist + hip - neck) > 0) {
        bf = 163.205 * Math.log10((waist + hip - neck) / 2.54) - 97.684 * Math.log10(hIn) - 78.387;
      }
      var bfHtml = '';
      if (bf !== null && bf > 2 && bf < 60) {
        bfHtml = '<div><span>Estimated body fat (Navy method)</span><b>' + bf.toFixed(1) + '%</b></div>';
      } else if (gender) {
        bfHtml = '<div><span>Estimated body fat</span><b>Add waist + neck (and hip for women) to see an estimate.</b></div>';
      }
      var bands = ['Underweight: below 18.5', 'Healthy weight: 18.5 \u2013 24.9', 'Overweight: 25 \u2013 29.9', 'Obesity: 30 and above'];
      out.innerHTML = '<p>Your BMI</p><b class="big">' + bmi.toFixed(1) + '</b><p>Category: <strong>' + cat + '</strong></p>'
        + '<div class="gauge"><div class="gauge-marker" style="left:' + pct.toFixed(1) + '%"></div></div>'
        + '<div class="gauge-labels"><span>Underweight</span><span>Healthy</span><span>Overweight</span><span>Obesity</span></div>'
        + '<div class="calc-grid"><div><span>Healthy weight range</span><b>' + low.toFixed(1) + ' \u2013 ' + high.toFixed(1) + ' kg</b></div><div><span>To healthy range</span><b>' + diff + '</b></div>' + bfHtml + '</div>'
        + '<div class="band">' + bands.map(function(b){ return '<span class="' + (b.split(':')[0] === cat ? 'hit' : '') + '">' + b + '</span>'; }).join('') + '</div>'
        + '<p class="small">General information only \u2014 not medical advice. Body-fat figures are estimates, not medical measurements. For a plan built around your body and goals, book a free ABROFIT consultation.</p>';
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

/* How It Works stepper, Program Finder quiz, FAQ search, session timer — all client-side, nothing saved. */
(function(){
  var st=document.getElementById('hiw-stepper');
  if(st){var tabs=st.querySelectorAll('.stepper-tab'),panels=st.querySelectorAll('.stepper-panel'),fill=document.getElementById('hiw-fill'),count=document.getElementById('hiw-count'),prev=document.getElementById('hiw-prev'),next=document.getElementById('hiw-next'),cur=0;
  function setStep(i){cur=i;tabs.forEach(function(t,j){t.setAttribute('aria-selected',j===i?'true':'false');});panels.forEach(function(p,j){p.classList.toggle('active',j===i);});if(fill)fill.style.width=((i+1)/panels.length*100)+'%';if(count)count.textContent='Step '+(i+1)+' of '+panels.length;if(prev)prev.disabled=(i===0);if(next)next.disabled=(i===panels.length-1);}
  tabs.forEach(function(t){t.addEventListener('click',function(){setStep(+t.getAttribute('data-step'));});});
  if(prev)prev.addEventListener('click',function(){if(cur>0)setStep(cur-1);});
  if(next)next.addEventListener('click',function(){if(cur<panels.length-1)setStep(cur+1);});
  setStep(0);}
  var qz=document.getElementById('quiz');
  if(qz){var go=document.getElementById('quiz-go'),res=document.getElementById('quiz-result'),warn=document.getElementById('quiz-warn');
  var progs={trial:{t:'One-Day Free Trial',w:'Try one full day free first, then decide with your coach.',m:'I would like to try the one-day free trial.'},personal:{t:'One-to-One Online Coaching',w:'Your own coach and your own plan, with daily personal guidance.',m:'I would like to know more about your One-to-One Online Coaching.'},change:{t:'90-Day Transformation Challenge',w:'A full 90 days of structured coaching for lasting change.',m:'I would like to know more about your 90-Day Transformation Challenge.'},habit:{t:'30-Day Online Fitness Program',w:'Thirty days to build the daily habit, with guided training and nutrition.',m:'I would like to know more about your 30-Day Online Fitness Program.'}};
  function val(n){var c=qz.querySelector('input[name="'+n+'"]:checked');return c?c.value:null;}
  function lab(n){var c=qz.querySelector('input[name="'+n+'"]:checked');if(!c)return '';var l=c.closest('label');return l?l.textContent.trim():c.value;}
  go.addEventListener('click',function(){var g=val('q-goal'),t=val('q-time'),e=val('q-exp');if(!g||!t||!e){warn.hidden=false;res.hidden=true;return;}warn.hidden=true;var p=progs[g]||progs.habit;document.getElementById('quiz-title').textContent='Suggested for you: '+p.t;document.getElementById('quiz-why').textContent=p.w;var cfg=window.ABROFIT_CONFIG||{};var base=cfg.whatsappUrl||'https://wa.me/918137008663';var msg='Hi ABROFIT, the Program Finder suggested '+p.t+' for me. '+p.m+' (Time: '+lab('q-time')+'; Experience: '+lab('q-exp')+'.)';document.getElementById('quiz-wa').href=base+'?text='+encodeURIComponent(msg);res.hidden=false;});}
  var fs=document.getElementById('faq-search');
  if(fs){var none=document.getElementById('faq-none');fs.addEventListener('input',function(){var q=fs.value.trim().toLowerCase(),shown=0;document.querySelectorAll('details').forEach(function(d){var txt=((d.querySelector('summary')?d.querySelector('summary').textContent:'')+' '+(d.textContent||''));var ok=!q||txt.toLowerCase().indexOf(q)!==-1;d.style.display=ok?'':'none';if(ok)shown++;});if(none)none.hidden=(shown>0);});}
  var td=document.getElementById('timer-display');
  if(td){var mins=document.getElementById('timer-mins'),start=document.getElementById('timer-start'),pause=document.getElementById('timer-pause'),reset=document.getElementById('timer-reset'),done=document.getElementById('timer-done'),left=0,iv=null,running=false;
  function fmt(s){var m=Math.floor(s/60),ss=s%60;return m+':'+(ss<10?'0':'')+ss;}
  function setLeft(){left=parseInt(mins.value,10)*60;td.textContent=fmt(left);done.hidden=true;}
  function tick(){if(left<=0){clearInterval(iv);iv=null;running=false;td.textContent='0:00';done.hidden=false;return;}left--;td.textContent=fmt(left);if(left<=0){clearInterval(iv);iv=null;running=false;done.hidden=false;}}
  start.addEventListener('click',function(){if(running)return;if(left<=0)setLeft();running=true;done.hidden=true;iv=setInterval(tick,1000);});
  pause.addEventListener('click',function(){if(iv)clearInterval(iv);iv=null;running=false;});
  reset.addEventListener('click',function(){if(iv)clearInterval(iv);iv=null;running=false;setLeft();});
  mins.addEventListener('change',function(){if(iv)clearInterval(iv);iv=null;running=false;setLeft();});
  setLeft();}
})();
