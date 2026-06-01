/* ==========================================================================
   MIT Medical Tower — interacciones
   Mega menú (desktop) · menú móvil con acordeón · scroll reveal · form
   ========================================================================== */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {

    /* ---------- Mega menú (desktop): hover + click + teclado ---------- */
    var hasMega = document.querySelector('.has-mega');
    if (hasMega) {
      var trigger = hasMega.querySelector('button');
      var closeTimer;

      var openMega = function () { clearTimeout(closeTimer); hasMega.classList.add('open'); if (trigger) trigger.setAttribute('aria-expanded', 'true'); };
      var closeMega = function () { hasMega.classList.remove('open'); if (trigger) trigger.setAttribute('aria-expanded', 'false'); };
      var closeSoon = function () { closeTimer = setTimeout(closeMega, 140); };

      // Solo activar hover en pantallas grandes (desktop)
      var isDesktop = function () { return window.matchMedia('(min-width:1024px)').matches; };

      hasMega.addEventListener('mouseenter', function () { if (isDesktop()) openMega(); });
      hasMega.addEventListener('mouseleave', function () { if (isDesktop()) closeSoon(); });

      if (trigger) {
        trigger.addEventListener('click', function (e) {
          e.preventDefault();
          hasMega.classList.contains('open') ? closeMega() : openMega();
        });
      }

      // Cerrar con Escape o al hacer click fuera
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMega(); });
      document.addEventListener('click', function (e) { if (!hasMega.contains(e.target)) closeMega(); });
    }

    /* ---------- Menú móvil ---------- */
    var toggle = document.querySelector('.nav-toggle');
    var mobileNav = document.querySelector('.mobile-nav');
    var backdrop = document.querySelector('.nav-backdrop');

    var setMobile = function (open) {
      if (!mobileNav) return;
      mobileNav.classList.toggle('open', open);
      if (toggle) { toggle.classList.toggle('active', open); toggle.setAttribute('aria-expanded', open ? 'true' : 'false'); }
      if (backdrop) backdrop.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    };

    if (toggle) toggle.addEventListener('click', function () { setMobile(!mobileNav.classList.contains('open')); });
    if (backdrop) backdrop.addEventListener('click', function () { setMobile(false); });
    // Cerrar al navegar a un ancla
    if (mobileNav) {
      mobileNav.querySelectorAll('a[href]').forEach(function (a) {
        a.addEventListener('click', function () { setMobile(false); });
      });
    }

    /* ---------- Acordeón "Especialidades" dentro del menú móvil ---------- */
    document.querySelectorAll('.mobile-acc > button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var acc = btn.parentElement;
        var isOpen = acc.classList.toggle('open');
        btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
    });

    /* ---------- Sombra de header al hacer scroll ---------- */
    var header = document.querySelector('.site-header');
    var onScroll = function () {
      if (!header) return;
      header.classList.toggle('scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    /* ---------- Scroll reveal ---------- */
    var revealEls = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window && revealEls.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) { entry.target.classList.add('in'); io.unobserve(entry.target); }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      revealEls.forEach(function (el) { io.observe(el); });
    } else {
      revealEls.forEach(function (el) { el.classList.add('in'); });
    }

    /* ---------- Formulario de contacto (demo, sin backend) ---------- */
    var form = document.querySelector('#contact-form');
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var status = form.querySelector('.form-status');
        var data = new FormData(form);
        var nombre = (data.get('nombre') || '').toString().trim();
        var msg = 'Hola, soy ' + (nombre || 'un paciente') +
          '. ' + ((data.get('mensaje') || '').toString().trim() || 'Me gustaría más información.');
        // Por ahora redirige a WhatsApp con el mensaje precargado (reemplazable por backend real)
        var wa = 'https://wa.me/525528380715?text=' + encodeURIComponent(msg);
        if (status) { status.textContent = 'Abriendo WhatsApp para enviar tu mensaje…'; status.style.color = 'var(--green-600)'; }
        window.open(wa, '_blank', 'noopener');
        form.reset();
      });
    }

    /* ---------- Mapa: cargar iframe solo al hacer click (facade) ---------- */
    var mapFacade = document.querySelector('#map-facade');
    if (mapFacade) {
      var loadBtn = mapFacade.querySelector('.map-load');
      if (loadBtn) {
        loadBtn.addEventListener('click', function () {
          var src = mapFacade.getAttribute('data-map');
          var iframe = document.createElement('iframe');
          iframe.src = src;
          iframe.title = 'Ubicación MIT Medical Tower';
          iframe.loading = 'lazy';
          iframe.referrerPolicy = 'no-referrer-when-downgrade';
          mapFacade.innerHTML = '';
          mapFacade.appendChild(iframe);
        });
      }
    }

    /* ---------- Año dinámico en footer ---------- */
    document.querySelectorAll('[data-year]').forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  });
})();
