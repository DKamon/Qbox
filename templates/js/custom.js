


jQuery(function($) {
  "use strict";
/* ==============================================
   Countdown
=============================================== */
  // Create a countdown instance. Change the launchDay according to your needs.
  // The month ranges from 0 to 11. I specify the month from 1 to 12 and manually subtract the 1.
  // Thus the launchDay below denotes 7 May, 2014.
  var launchDay = new Date(2018, 12-1, 8);
  $('#timer').countdown({
  until: launchDay
  });

/* ----------------------------------------------------------- */
   /*  Animation
   /* ----------------------------------------------------------- */
        new WOW().init();


    /* === jQuery for page scrolling feature - requires jQuery Easing plugin === */
    (function () {
        $('a.scroll').on('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
        });
    }());



});