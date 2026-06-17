/* ==========================================================================
   MIT Medical Tower — Layout compartido (única fuente de verdad)
   Inyecta header (topbar + nav + mega menú), drawer móvil, footer y WhatsApp.
   Se incluye ANTES de main.js en todas las páginas.
   Rutas root-relativas (/...) — el sitio se sirve desde la raíz del dominio.
   ========================================================================== */

/* Google Analytics 4 — dispara en todas las páginas del sitio */
(function () {
  var GA_ID = 'G-61S9GSVGWE';
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', GA_ID);
})();

(function () {
  'use strict';

  /* Orden de especialidades según el menú de referencia del cliente */
  var SPECIALTIES = [
    { slug: 'dermatologia',            name: 'Dermatología',              desc: 'Piel, cabello y uñas',        gridDesc: 'Cuidado de la piel, cabello y uñas, clínico y estético.' },
    { slug: 'pediatria',               name: 'Pediatría',                 desc: 'Salud infantil',              gridDesc: 'Atención médica integral para bebés, niños y adolescentes.' },
    { slug: 'oncologia',               name: 'Oncología',                 desc: 'Tratamiento del cáncer',      gridDesc: 'Diagnóstico, tratamiento y acompañamiento en el cuidado del cáncer.' },
    { slug: 'neurologia',              name: 'Neurología',                desc: 'Sistema nervioso',            gridDesc: 'Atención de padecimientos del sistema nervioso central y periférico.' },
    { slug: 'otorrinolaringologia',    name: 'Otorrinolaringología',      desc: 'Oído, nariz y garganta',      gridDesc: 'Cuidado del oído, la nariz, la garganta y estructuras relacionadas.' },
    { slug: 'nefrologia',              name: 'Nefrología',                desc: 'Riñones',                     gridDesc: 'Cuidado y tratamiento de las enfermedades del riñón.' },
    { slug: 'gastroenterologia',       name: 'Gastroenterología',         desc: 'Aparato digestivo',           gridDesc: 'Diagnóstico y tratamiento del aparato digestivo.' },
    { slug: 'medicina-interna',        name: 'Medicina Interna',          desc: 'Infectología',                gridDesc: 'Manejo integral del paciente adulto y enfermedades infecciosas.' },
    { slug: 'ginecologia',             name: 'Ginecología',               desc: 'Salud femenina',              gridDesc: 'Salud integral de la mujer en todas las etapas de su vida.' },
    { slug: 'traumatologia-ortopedia', name: 'Traumatología y Ortopedia', desc: 'Huesos y articulaciones',     gridDesc: 'Tratamiento de lesiones de huesos, músculos y articulaciones.' },
    { slug: 'cirugia-plastica',        name: 'Cirugía Plástica',          desc: 'Estética y reconstrucción',   gridDesc: 'Procedimientos estéticos y reconstructivos en manos expertas.' },
    { slug: 'cardiologia',             name: 'Cardiología',               desc: 'Corazón y circulación',       gridDesc: 'Diagnóstico y tratamiento de enfermedades del corazón y la circulación.' },
    { slug: 'angiologia',              name: 'Angiología',                desc: 'Venas y arterias',            gridDesc: 'Atención de las enfermedades de venas, arterias y sistema linfático.' },
    { slug: 'urologia',                name: 'Urología',                  desc: 'Sistema urinario',            gridDesc: 'Cuidado del aparato urinario y la salud reproductiva.' },
    { slug: 'psicologia',              name: 'Psicología',                desc: 'Salud mental',                gridDesc: 'Acompañamiento profesional para tu salud mental y emocional.' }
  ];

  var ICONS = {
    cardiologia: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"/>',
    urologia: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M12 3.75s6 5.25 6 9.75a6 6 0 11-12 0c0-4.5 6-9.75 6-9.75z"/>',
    psicologia: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z"/>',
    ginecologia: '<circle cx="12" cy="8" r="4.5" stroke-width="1.6"/><path stroke-linecap="round" stroke-width="1.6" d="M12 12.5V21M9 18h6"/>',
    'traumatologia-ortopedia': '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M7 17l10-10M6.5 4.5a2.12 2.12 0 113 3L7 10 4 7l2.5-2.5zM17.5 19.5a2.12 2.12 0 01-3-3L17 14l3 3-2.5 2.5z"/>',
    neurologia: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M15.5 7.5A3.5 3.5 0 0012 4a3.5 3.5 0 00-3.5 3.5M8 9.5A3 3 0 005 12a3 3 0 003 3m8-5.5a3 3 0 013 2.5 3 3 0 01-3 3M12 4v16m0 0a3 3 0 003-3m-3 3a3 3 0 01-3-3"/>',
    nefrologia: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M8 4c-2.5 0-4 2-4 5s2 8 4 8 2.5-2 4-2 1.5 2 4 2 4-5 4-8-1.5-5-4-5-3 2-4 2-1.5-2-4-2z"/>',
    gastroenterologia: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M9 4v4a4 4 0 004 4h2a3 3 0 013 3v1a4 4 0 01-4 4 5 5 0 01-5-5V9"/>',
    angiologia: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M3 12h4l2-7 4 14 2-7h6"/>',
    otorrinolaringologia: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M7 9a5 5 0 0110 0c0 3-2 4-3 5s-1 3-3 3a3 3 0 01-3-3"/><circle cx="11.5" cy="9.5" r="1.5" stroke-width="1.6"/>',
    oncologia: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M12 21s-1-7 0-10c.7-2.1 3-3 4.5-1.5S17 14 12 21zM12 21s1-7 0-10C11.3 8.9 9 8 7.5 9.5S7 14 12 21z"/>',
    pediatria: '<circle cx="12" cy="7" r="3.5" stroke-width="1.6"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M6 21a6 6 0 0112 0"/>',
    dermatologia: '<circle cx="12" cy="12" r="4" stroke-width="1.6"/><path stroke-linecap="round" stroke-width="1.6" d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
    'cirugia-plastica': '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M12 4l1.6 4.4L18 10l-4.4 1.6L12 16l-1.6-4.4L6 10l4.4-1.6L12 4zM18 14l.8 2L21 17l-2.2.9L18 20l-.8-2.1L15 17l2.2-1L18 14z"/>',
    'medicina-interna': '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M6 4v5a4 4 0 008 0V4M10 17a4 4 0 008 0v-1.5"/><circle cx="18" cy="13.5" r="2" stroke-width="1.6"/>'
  };

  var WA = 'https://wa.me/525528380715';
  function svg(inner) { return '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24">' + inner + '</svg>'; }

  /* ---------- Mega menú (desktop) ---------- */
  var megaItems = SPECIALTIES.map(function (s) {
    return '<a class="mega-item" href="/especialidades/' + s.slug + '.html">' +
      '<span class="ic">' + svg(ICONS[s.slug]) + '</span>' +
      '<span class="tx"><strong>' + s.name + '</strong><span>' + s.desc + '</span></span></a>';
  }).join('');

  /* ---------- Acordeón (móvil) ---------- */
  var mobileItems = SPECIALTIES.map(function (s) {
    return '<a href="/especialidades/' + s.slug + '.html">' + s.name + '</a>';
  }).join('');

  var SOCIAL = {
    fb: '<path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/>',
    ig: '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>',
    wa: '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884"/>',
    tt: '<path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.27 6.27 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V8.94a8.17 8.17 0 004.78 1.53V7a4.85 4.85 0 01-1.01-.31z"/>'
  };
  function soc(fill) { return '<svg fill="currentColor" viewBox="0 0 24 24">' + fill + '</svg>'; }

  var headerHTML =
  '<header class="site-header">' +
    '<div class="topbar"><div class="container">' +
      '<div class="topbar-info">' +
        '<a href="tel:+525528380715">' + svg('<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>') + '(+52) 552 838 0715</a>' +
        '<span class="hide-sm">' + svg('<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>') + 'Prados de Aragón, Nezahualcóyotl</span>' +
        '<a href="mailto:mitmedicalt@yahoo.com" class="hide-sm">' + svg('<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>') + 'mitmedicalt@yahoo.com</a>' +
      '</div>' +
      '<div class="topbar-social">' +
        '<a href="https://www.facebook.com/MitMedicalTower" target="_blank" rel="noopener" aria-label="Facebook">' + soc(SOCIAL.fb) + '</a>' +
        '<a href="https://www.instagram.com/mit_medical_tower/" target="_blank" rel="noopener" aria-label="Instagram">' + soc(SOCIAL.ig) + '</a>' +
        '<a href="https://www.tiktok.com/@mit.medical.tower" target="_blank" rel="noopener" aria-label="TikTok">' + soc(SOCIAL.tt) + '</a>' +
        '<a href="' + WA + '" aria-label="WhatsApp">' + soc(SOCIAL.wa) + '</a>' +
      '</div>' +
    '</div></div>' +
    '<nav class="nav" aria-label="Principal"><div class="container">' +
      '<a href="/index.html" class="logo" aria-label="MIT Medical Tower — inicio">' +
        '<img src="/assets/logo-medica-400x160.png" alt="MIT Medical Tower" width="400" height="160"></a>' +
      '<ul class="nav-menu">' +
        '<li><a href="/index.html" data-nav="inicio">Inicio</a></li>' +
        '<li><a href="/nosotros.html" data-nav="nosotros">Nosotros</a></li>' +
        '<li class="has-mega">' +
          '<button type="button" aria-expanded="false" aria-haspopup="true" data-nav="especialidades">Especialidades' +
            '<svg class="caret" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button>' +
          '<div class="mega" role="menu" aria-label="Especialidades"><div class="mega-inner">' +
            '<div class="mega-grid">' + megaItems + '</div>' +
            '<aside class="mega-feature"><div><h4>¿No sabes con qué especialista acudir?</h4>' +
              '<p>Nuestro equipo de consulta general te orienta y te canaliza con el especialista indicado para tu caso.</p></div>' +
              '<a href="/servicios.html" class="btn btn-accent">Ver servicios</a></aside>' +
          '</div></div>' +
        '</li>' +
        '<li><a href="/servicios.html" data-nav="servicios">Servicios</a></li>' +
        '<li><a href="/instalaciones.html" data-nav="instalaciones">Instalaciones</a></li>' +
        '<li><a href="/blog/index.html" data-nav="blog">Blog</a></li>' +
        '<li><a href="#contacto">Contacto</a></li>' +
      '</ul>' +
      '<div class="nav-actions"><a href="#contacto" class="btn btn-primary">Contáctanos</a></div>' +
      '<button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="mobile-nav"><span></span><span></span><span></span></button>' +
    '</div></nav>' +
  '</header>' +
  '<div class="nav-backdrop"></div>' +
  '<div class="mobile-nav" id="mobile-nav">' +
    '<a href="/index.html">Inicio</a>' +
    '<a href="/nosotros.html">Nosotros</a>' +
    '<div class="mobile-acc"><button type="button" aria-expanded="false">Especialidades' +
      '<svg class="caret" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button>' +
      '<div class="mobile-acc-panel">' + mobileItems + '</div></div>' +
    '<a href="/servicios.html">Servicios</a>' +
    '<a href="/instalaciones.html">Instalaciones</a>' +
    '<a href="/blog/index.html">Blog</a>' +
    '<a href="#contacto">Contacto</a>' +
    '<a href="#contacto" class="btn btn-primary">Contáctanos</a>' +
  '</div>';

  var footerHTML =
  '<footer class="site-footer"><div class="container">' +
    '<div class="footer-grid">' +
      '<div class="footer-brand">' +
        '<a href="/index.html" class="logo"><img src="/assets/logo-medica-400x160.png" alt="MIT Medical Tower"></a>' +
        '<p>En MIT Medical Tower nos apasiona brindar una atención médica de calidad y poner a tu disposición los recursos más avanzados.</p></div>' +
      '<div><h4>Contacto</h4><ul class="footer-links">' +
        '<li>' + svg('<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>') + '<address>Blvrd Prados de Aragón 8B, Prados de Aragón, 57179 Cdad. Nezahualcóyotl, Méx.</address></li>' +
        '<li>' + svg('<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>') + '<a href="tel:+525528380715">+52 552 838 0715</a></li>' +
        '<li>' + svg('<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>') + '<a href="mailto:mitmedicalt@yahoo.com">mitmedicalt@yahoo.com</a></li>' +
        '<li>' + svg('<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>') + '<span>9:00 am – 5:00 pm · Lunes a Viernes</span></li>' +
      '</ul></div>' +
      '<div><h4>Síguenos</h4><div class="footer-social">' +
        '<a href="https://www.facebook.com/MitMedicalTower" target="_blank" rel="noopener" aria-label="Facebook">' + soc(SOCIAL.fb) + '</a>' +
        '<a href="https://www.instagram.com/mit_medical_tower/" target="_blank" rel="noopener" aria-label="Instagram">' + soc(SOCIAL.ig) + '</a>' +
        '<a href="https://www.tiktok.com/@mit.medical.tower" target="_blank" rel="noopener" aria-label="TikTok">' + soc(SOCIAL.tt) + '</a>' +
        '<a href="' + WA + '" aria-label="WhatsApp">' + soc(SOCIAL.wa) + '</a>' +
      '</div></div>' +
    '</div>' +
    '<div class="footer-bottom">' +
      '<p>La información de este sitio es únicamente informativa y no sustituye una consulta médica profesional. Los resultados pueden variar según cada caso.</p>' +
      '<p>© <span data-year>2026</span> MIT Medical Tower. Todos los derechos reservados.</p>' +
    '</div>' +
  '</div></footer>' +
  '<a href="' + WA + '?text=Hola%2C%20me%20gustar%C3%ADa%20agendar%20una%20cita" target="_blank" rel="noopener" class="wa-float" aria-label="Contactar por WhatsApp">' + soc(SOCIAL.wa) + '</a>';

  /* ---------- Rutas relativas según profundidad ---------- */
  /* Las páginas de /especialidades/ están un nivel abajo: prefijo "../".  */
  /* rel() convierte los enlaces internos absolutos ("/x") a relativos      */
  /* para que el sitio funcione abriendo el archivo (file://), en el        */
  /* servidor local y en el dominio real, sin importar la carpeta.          */
  var BASE = /\/(especialidades|blog)\//.test(location.pathname) ? '../' : '';
  function rel(html) { return html.replace(/(href|src)="\//g, '$1="' + BASE); }

  /* ---------- Inyección (síncrona, al final del body) ---------- */
  function inject(id, html) {
    var slot = document.getElementById(id);
    if (slot) slot.outerHTML = html;
  }
  inject('site-header', rel(headerHTML));
  inject('site-footer', rel(footerHTML));

  /* Grid de especialidades del home (si existe el contenedor) */
  var gridSlot = document.getElementById('spec-grid-slot');
  if (gridSlot) {
    var arrow = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/></svg>';
    gridSlot.innerHTML = rel(SPECIALTIES.map(function (s) {
      return '<a class="spec-card reveal" href="/especialidades/' + s.slug + '.html">' +
        '<span class="ic">' + svg(ICONS[s.slug]) + '</span>' +
        '<h3>' + s.name + '</h3>' +
        '<p>' + s.gridDesc + '</p>' +
        '<span class="more">Ver más ' + arrow + '</span></a>';
    }).join(''));
  }

  /* Marca el enlace activo según la página actual */
  var page = (location.pathname.split('/').pop() || 'index.html');
  var active = document.querySelector('.nav-menu [data-nav="' + (
    /especialidades/.test(location.pathname) ? 'especialidades' :
    /\/blog\//.test(location.pathname) ? 'blog' :
    page.replace('.html', '')
  ) + '"]');
  if (active) active.classList.add('active');
})();
