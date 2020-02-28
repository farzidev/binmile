( function() {
	function addCombo( editor, comboName, styleType, lang, entries, defaultLabel, styleDefinition, order ) {
		var config = editor.config,style = new CKEDITOR.style( styleDefinition );
		var names = entries.split( ';' ),values = [];
		var styles = {};
		for ( var i = 0; i < names.length; i++ ) {
			var parts = names[ i ];
			if ( parts ) {
				parts = parts.split( '/' );
				var vars = {},name = names[ i ] = parts[ 0 ];
				vars[ styleType ] = values[ i ] = parts[ 1 ] || name;
				styles[ name ] = new CKEDITOR.style( styleDefinition, vars );
				styles[ name ]._.definition.name = name;
			} else
				names.splice( i--, 1 );
		}
		editor.ui.addRichCombo( comboName, {
			label: editor.lang.lineheight.title,
			title: editor.lang.lineheight.title,
			toolbar: 'styles,' + order,
			allowedContent: style,
			requiredContent: style,
			panel: {
				css: [ CKEDITOR.skin.getPath( 'editor' ) ].concat( config.contentsCss ),
				multiSelect: false,
				attributes: { 'aria-label': editor.lang.lineheight.title }
			},
			init: function() {
				this.startGroup(editor.lang.lineheight.title);
				for ( var i = 0; i < names.length; i++ ) {
					var name = names[ i ];
					this.add( name, styles[ name ].buildPreview(), name );
				}
			},
			onClick: function( value ) {
				editor.focus();
				editor.fire( 'saveSnapshot' );
				var style = styles[ value ];
				editor[ this.getValue() == value ? 'removeStyle' : 'applyStyle' ]( style );
				editor.fire( 'saveSnapshot' );
			},
			onRender: function() {
				editor.on( 'selectionChange', function( ev ) {
					var currentValue = this.getValue();
					var elementPath = ev.data.path,elements = elementPath.elements;
					for ( var i = 0, element; i < elements.length; i++ ) {
						element = elements[ i ];
						for ( var value in styles ) {
							if ( styles[ value ].checkElementMatch( element, true, editor ) ) {
								if ( value != currentValue )
									this.setValue( value );
								return;
							}
						}
					}
					this.setValue( '', defaultLabel );
				}, this );
			},
			refresh: function() {
				if ( !editor.activeFilter.check( style ) )
					this.setState( CKEDITOR.TRISTATE_DISABLED );
			}
		} );
	}
	CKEDITOR.plugins.add( 'lineheight', {
		requires: 'richcombo',
		lang: 'ar,de,en,es,fr,ko,pt',
		init: function( editor ) {
			var config = editor.config;
			addCombo( editor, 'lineheight', 'size', editor.lang.lineheight.title, config.line_height, editor.lang.lineheight.title, config.lineheight_style, 40 );
		}
	} );
} )();
// CKEDITOR.config.line_height = '1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60;61;62;63;64;65;66;67;68;69;70;71;72';
CKEDITOR.config.line_height = '1.0;1.5;2.0;2.5;3.0;3.5;4.0;4.5;5.0;5.5;6.0;6.5;7.0;7.5;8.0;8.5;9.0;9.5;10.0;10.5;11.0;11.5;12.0;12.5;13.0;13.5;14.0;14.5;15.0;15.5;16.0;16.5;17.0;17.5;18.0;18.5;19.0;19.5;20.0;20.5;21.0;21.5;22.0;22.5;23.0;23.5;24.0;24.5;25.0;25.5;26.0;26.5;27.0;27.5;28.0;28.5;29.0;29.5;30.0;30.5;31.0;31.5;32.0;32.5;33.0;33.5;34.0;34.5;35.0;35.5;36.0;36.5;37.0;37.5;38.0;38.5;39.0;39.5;40.0;40.5;41.0;41.5;42.0;42.5;43.0;43.5;44.0;44.5;45.0;45.5;46.0;46.5;47.0;47.5;48.0;48.5;49.0;49.5;50.0';
CKEDITOR.config.lineheight_style = {
	element: 'span',
	styles: { 'line-height': '#(size)' },
	overrides: [ {
		element: 'line-height', attributes: { 'size': null }
	} ]
};
