/* Use this script if you need to support IE 7 and IE 6. */

window.onload = function() {
	function addIcon(el, entity) {
		var html = el.innerHTML;
		el.innerHTML = '<span style="font-family: \'life_symbols\'">' + entity + '</span>' + html;
	}
	var icons = {
			'life_icons-movie' : '&#xe000;',
			'life_icons-beer' : '&#xe001;',
			'life_icons-place' : '&#xe002;',
			'life_icons-run' : '&#xe003;',
			'life_icons-hike' : '&#xe004;',
			'life_icons-camera' : '&#xe020;',
			'life_icons-movie-2' : '&#xe026;',
			'life_icons-tv' : '&#xe027;',
			'life_icons-music' : '&#xe02f;',
			'life_icons-gamepad' : '&#xe035;',
			'life_icons-cog' : '&#xe036;',
			'life_icons-bug' : '&#xe039;',
			'life_icons-globe' : '&#xe03c;',
			'life_icons-binocular' : '&#xe046;',
			'life_icons-bookmark' : '&#xe04e;',
			'life_icons-pencil' : '&#xe055;',
			'life_icons-gift' : '&#xe060;',
			'life_icons-lamp' : '&#xe061;',
			'life_icons-settings' : '&#xe062;',
			'life_icons-medicine' : '&#xe064;',
			'life_icons-cone' : '&#xe065;',
			'life_icons-key' : '&#xe068;',
			'life_icons-timer' : '&#xe06b;',
			'life_icons-food' : '&#xe005;',
			'life_icons-cup' : '&#xe06e;',
			'life_icons-drink' : '&#xe06f;',
			'life_icons-truck' : '&#xe006;',
			'life_icons-car' : '&#xe007;'
		},
		els = document.getElementsByTagName('*'),
		i, attr, html, c, el;
	for (i = 0; i < els.length; i += 1) {
		el = els[i];
		attr = el.getAttribute('data-icon');
		if (attr) {
			addIcon(el, attr);
		}
		c = el.className;
		c = c.match(/life_icons-[^\s'"]+/);
		if (c && icons[c[0]]) {
			addIcon(el, icons[c[0]]);
		}
	}
};