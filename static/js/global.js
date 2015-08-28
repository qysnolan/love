// Make the current url active
$(document).ready(function()  {
    /* SHOW ACTIVE TAB AND MAINTAIN CORRECT SIZE */
    $('.sidebar-nav li a').filter(function() {
        return window.location.toString().indexOf(this.href.toString()) != -1;
    }).parent().addClass('current');
});

// Toogle the sidebar menu
$("#menu-close").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggleClass("active");
});

$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggleClass("active");
});

$('#scrollup').click(function () {
    $("html, body").animate({
        scrollTop: 0
    }, 600);
    return false;
});

// Scrolls to the selected menu item on the page
$(function() {
    $('a[href*=#]:not([href=#])').click(function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });
});

// Google translate
function googleTranslateElementInit() {
    new google.translate.TranslateElement({
            pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
            autoDisplay: false},
        'google_translate_element');
}

var googleTranslateScript = document.createElement('script');
googleTranslateScript.type = 'text/javascript';
googleTranslateScript.async = true;
googleTranslateScript.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0] ).appendChild(googleTranslateScript);
googleTranslateScript.async = true;

var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-37132105-1']);
_gaq.push(['_trackPageview']);
(function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();