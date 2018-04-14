var tinymce_conf = {
	body_id:		'content',
	content_css:	'/static/css/fontface.css,/static/css/basic.css,/static/css/content.css,/static/admin/css/tinymce.css',
	language: 		'fr',
	theme: 			'advanced',
	plugins:		'fullscreen,advlink,table,template,nonbreaking',
	theme_advanced_toolbar_location: 'top',
	theme_advanced_toolbar_align : 'left',
	theme_advanced_resizing:	true,
	theme_advanced_buttons1:	'bold,italic,bullist,numlist,hr,|,formatselect,styleselect,removeformat,nonbreaking,|,link,unlink,anchor,|,image,template,|,fullscreen,|,code',
	theme_advanced_buttons2:	'',
	theme_advanced_buttons3:	'',
	convert_urls:	false,
	theme_advanced_blockformats : 'p,h1,h2,h3,blockquote',
    file_browser_callback: 'CustomFileBrowser',
    entity_encoding: 'named', // previous : 'raw'
    entities: '160,nbsp',
    template_templates : []
};
var tinymce_conf_italic = {
		body_id:		'content',
		language: 		'fr',
		mode: 'exact',
		theme: 			'advanced',
		theme_advanced_toolbar_location: 'top',
		theme_advanced_toolbar_align : 'left',
		theme_advanced_resizing:	false,
		theme_advanced_buttons1:	'italic',
		theme_advanced_buttons2:	'',
		theme_advanced_buttons3:	'',
		convert_urls:	false,
	    entity_encoding : 'raw',
	    height: 20
	};

$(document).ready(function($){
	$('#id_body').tinymce(tinymce_conf);
	$('.filmography-playreference #id_description').tinymce(tinymce_conf);
	$('.filmography-playreference #id_quotation').tinymce(tinymce_conf);
    $('#film_form #id_source').tinymce(tinymce_conf_italic);
    $('#analysis_form #id_title').tinymce(tinymce_conf_italic);
});