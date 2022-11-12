jQuery(document).ready(function ($) {

    'use strict';

    /* Detect Devices */
    var $window = $(window);
    var isMobile = navigator.userAgent.match(/Mobi/);
    var iOffset = ($window.width() > 1800) ? -200 : -80;

    // One Page Nav
    $('#nav').onePageNav();

    // Scroll Reveal
    window.sr = ScrollReveal();
    sr.reveal('.scroll-reveal', {
        duration: 1500,
        mobile: false,
        viewFactor: 0.3
    });

    // Swiper carousel - Main banner
    new Swiper('.swiper-container',
        {
            speed: 1000,
            direction: 'horizontal',
            navigation:
                {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
            pagination:
                {
                    el: '.swiper-pagination',
                    dynamicBullets: true,
                },
            zoom: true,
            keyboard:
                {
                    enabled: true,
                    onlyInViewport: false,
                },
            mousewheel:
                {
                    invert: true,
                },
            autoplay:
                {
                    delay: 4000,
                },
            loop: true,
        });

    // Magnific Popup
    $('.lightbox').magnificPopup({
        removalDelay: 300
    });
    $('.lightbox-gallery').magnificPopup({
        removalDelay: 300,
        gallery: {
            enabled: true,
            preload: [1, 1],
            navigateByImgClick: true,
            arrowMarkup: '<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>', // markup of an arrow button
            tPrev: 'Previous (Left arrow key)', // title for left button
            tNext: 'Next (Right arrow key)', // title for right button
            tCounter: '<span class="mfp-counter">%curr% of %total%</span>' // markup of counter
        }
    });

    // Check if input is filled
    $('.form-control').on('blur', function () {
        if (hasValue($(this))) {
            $(this).addClass('-hasvalue');
        } else {
            $(this).removeClass('-hasvalue');
        }
    });

    function hasValue(elem) {
        return $(elem).filter(function () {
            return $(this).val();
        }).length > 0;
    }

    // Do this only on desktop
    if (!isMobile) {

        /* Init Parallax */

        $('.parallax').parallaxie({
            speed: 0.5,
            size: 'cover',
            offset: iOffset
        });

        /* Text Parallax for Main Banner */
        $window.scroll(function () {
            $(".text-parallax").css("opacity", 1 - $(window).scrollTop() / 450);
        });

        /* 3D Tilt Effect */
        $('.js-tilt').tilt({
            perspective: 1000
        });

    } // !isMobile

    // Cookie consent bar
    new cookieBar();
});