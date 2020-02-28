// var $ = django.jQuery;

// console.log(django.jQuery)

////////////////////////////////
// ERROR: PLUGIN DOES NOT SHOW UP IN EDITOR
////////////////////////////////

(function($) {
  'use strict';
  $(document).ready(function() {
    // var myButton = '<div style="margin: 10px 0;"><a target="_blank" href="/admin/posts/blogimage/add/" style="background-color: #609ab6; padding: 12px; font-size: 0.8rem; color: white; border-radius: 4pxl; border: none; cursor: pointer;" type="button" id="addBlogImg">Add Blog Image</button></div>';
    // $(myButton).insertBefore($('label[for=id_content]').parent('div'));

    //Section 2 : Create the button and add the functionality to it


    CKEDITOR.plugins.add( 'addblogimage', {
      init: function( editor ) {
        var command = editor.addCommand( 'addblogimagecommand', {
          exec: function( editor ) {
            window.open(window.location.origin + '/admin/posts/blogimage/add/')
          }
        });
        editor.ui.addButton( 'Addblogimage', {
          label: 'Add blog image',
          command: 'addblogimagecommand',
          icon: this.path + 'plus.png'
        });
      }
    });
  });

})(django.jQuery);
