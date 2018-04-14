bundles = {
    
    # Abstract assets
    'jquery': {
        'js': ('/static/js/jquery-1.5.2.min.js'),
    },
    'tinymce': {
        'import': 'jquery',
        'js': ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/jquery.tinymce.js', '/static/admin/js/FilebrowserTinymce.js'),
    },
    'facebox': {
        'import': 'jquery',
        'js':   ('/static/js/facebox/facebox.js', '/static/js/facebox-config.js'),
        'css':  '/static/js/facebox/facebox.css',   
    },
    
    
    # Concrete assets
    'base': {
        'css': ('/static/css/basic.css', '/static/css/base.css', '/static/css/content.css'),
    },
    'simplepage': {},
    'googlemaps': {
        'import': 'jquery',
        'js': ('http://maps.google.com/maps/api/js?sensor=false', '/static/js/googlemaps.js'),
        'css': '/static/css/googlemaps.css',
    },
    'contact_form': {
        'css':  '/static/css/contact_form.css',
    },
    'search_form': {
        'css':  '/static/css/search_form.css',
    },
    'contributors': {
        'css': '/static/css/contributors.css',
    },
    
    'contributor': {
        'import': ('simplepage', 'listing'),
        'css': '/static/css/contributor.css',
    },
    
    'film': {
        'import': 'listing',
        'css': '/static/css/film.css',
    },
    
    'analysis': {
        'css': '/static/css/analysis.css',
    },
           
    'listing':{
        'css': '/static/css/listing.css',
    },
    
    # Admin assets
    'admin.form': {
        'import': ('tinymce'),
        'js': ('/static/admin/js/forms.js'),
    },
    'simplepage_form': {'import': 'admin.form'}
}