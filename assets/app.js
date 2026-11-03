/* ABROFIT site JS: nav, dropdowns, reveal, year, BMI calculator. No dependencies. */
(function () {
  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  var burger = document.querySelector(".hamburger");
  var nav = document.querySelector(".main-nav");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Dropdowns: toggle buttons work on mobile; Escape closes and returns focus.
  document.querySelectorAll(".drop").forEach(function (drop) {
    var toggle = drop.querySelector(".drop-toggle");
    var parent = drop.querySelector(".drop-parent");
    if (toggle) {
      toggle.addEventListener("click", function (e) {
        e.stopPropagation();
        var wasOpen = drop.classList.contains("open");
        document.querySelectorAll(".drop.open").forEach(function (d) { d.classList.remove("open"); });
        if (!wasOpen) drop.classList.add("open");
        toggle.setAttribute("aria-expanded", wasOpen ? "false" : "true");
      });
    }
    drop.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        drop.classList.remove("open");
        (toggle || parent).focus();
      }
    });
  });
  document.addEventListener("click", function () {
    document.querySelectorAll(".drop.open").forEach(function (d) { d.classList.remove("open"); });
  });

  document.querySelectorAll(".main-nav a").forEach(function (a) {
    a.addEventListener("click", function () { nav.classList.remove("open"); });
  });

  var spot = document.querySelector(".spotlight");
  if (spot && window.matchMedia("(pointer:fine)").matches) {
    var raf = null;
    document.addEventListener("mousemove", function (e) {
      if (raf) return;
      raf = requestAnimationFrame(function () {
        spot.style.left = e.clientX + "px";
        spot.style.top = e.clientY + "px";
        raf = null;
      });
    });
  }

  // Reveal on scroll.
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  // BMI calculator (calculator.html only).
  var btn = document.getElementById("bmi-btn");
  if (btn) {
    btn.addEventListener("click", function () {
      var h = parseFloat(document.getElementById("bmi-h").value);
      var w = parseFloat(document.getElementById("bmi-w").value);
      var out = document.getElementById("bmi-out");
      if (!h || !w || h <= 0 || w <= 0) { out.textContent = "Please enter a valid height and weight."; return; }
      var bmi = w / ((h / 100) * (h / 100));
      var cat = bmi < 18.5 ? "underweight range" : bmi < 25 ? "healthy range" : bmi < 30 ? "overweight range" : "obesity range";
      out.textContent = "Your BMI is " + bmi.toFixed(1) + " (" + cat + ").";
    });
  }
})();
