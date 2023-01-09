/*!
 * Simple JS plugin for generating a basic cookie consent notice easily
 *
 * Copyright (c) 2022 @louisho5
 * Under the MIT license.
 *
 * @version 1.0.0
 */

let cookieBar = function (options) {
    this.options = options;
    if (this.options == undefined) {
        this.options = {}
    }
    // Set options to default value when not set manually
    if (this.options.selector == undefined) {
        this.options.selector = '#cookieBar';
    }
    if (this.options.expire == undefined) {
        this.options.expire = 24;
    }

    const cookie_bar = document.getElementById("cookie-bar");

    let ccExpire = this.options.expire;

    // Check if cookie has been accepted
    window.onload = function () {
        if (getCookie("cc-bar-cookies") != "accepted") {
            cookie_bar.style.display = "flex";
        } else {
            cookie_bar.style.display = "none";
        }
        // Update cookies when clicked button
        const element = document.getElementById("cookie-btn");
        element.addEventListener("click", function (e) {
            e.preventDefault();
            setCookie("cc-bar-cookies", "accepted", ccExpire);
            cookie_bar.style.animation =
                "cc-bar-fadeOut 0.5s ease both";
            setTimeout(function () {
                cookie_bar.style.display = "none";
            }, 500);
        });
    }

    // Cookies Controls
    let setCookie = function (name, value, expireHrs) {
        let d = new Date();
        d.setTime(d.getTime() + expireHrs * 60 * 60 * 1000);
        document.cookie = name + "=" + value + ";" + "expires=" + d.toUTCString() + ";path=/";
    }

    let getCookie = function (name) {
        function escape(s) {
            return s.replace(/([.*$(){}|\[\]\/\\])/g, "\\$1");
        }

        var match = document.cookie.match(
            RegExp("(?:^|;\\s*)" + escape(name) + "=([^;]*)")
        );
        return match ? match[1] : null;
    }
}
