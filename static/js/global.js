/**
 * Created by yunshengqi on 8/16/15.
 */
$(document).ready(function()  {
    /* SHOW ACTIVE TAB AND MAINTAIN CORRECT SIZE */
    $('ul.nav a').filter(function() {
        return this.href == window.location;
    }).parent().addClass('active');
});