$(document).ready(function()  {
    /* SHOW ACTIVE TAB AND MAINTAIN CORRECT SIZE */
    $('ul.nav a').filter(function() {
        return window.location.toString().indexOf(this.href.toString()) != -1;
    }).parent().addClass('active');
});

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