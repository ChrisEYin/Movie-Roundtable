
// Dropdown menu when selecting Login or Register
//
$(document).ready(function(){
  $('#navigation #register').hide();
  $('#navigation #cork').hide();

var callRegistration = function(){  
  $('#navigation li:first-child a').click(function() {
		if ($('#navigation #register').is(':visible')) {
			$('#navigation #register').hide()
			} else { ($('#navigation #register').show() && $('#navigation #cork').hide())}
  });
  }

var callLogin = function(){  
  $('#navigation li:last-child a').click(function() {
		if ($('#navigation #cork').is(':visible')) {
			$('#navigation #cork').hide()
			} else { ($('#navigation #cork').show() && $('#navigation #register').hide())}
  });
  }
  
callRegistration();
callLogin();

// Hide when click elsewhere
 $('html').click(function() {
   $('#navigation #register').hide();
  $('#navigation #cork').hide();
 });
 $('#navigation').click(function(event){
     event.stopPropagation();
 });
});

//Carousel with arrows
//
$(document).ready(function() {
    //move images
    $('.content_covers li:first').before($('.content_covers li:last')); 
    $('.rightarrow').click(function(){
		var item_width = $('.content_covers li').outerWidth();
        var left_indent = parseInt($('.content_covers').css('left')) - item_width;
		$('.content_covers:not(:animated)').animate({'left' : left_indent},500,function(){    
		$('.content_covers li:last').after($('.content_covers li:first')); 
		$('.content_covers').css({'left' : '0'});
        }); 
    });

    $('.leftarrow').click(function(){
        var item_width = $('.content_covers li').outerWidth();
        var left_indent = parseInt($('.content_covers').css('left')) + (item_width * 4);
		$('.content_covers:not(:animated)').animate({'left' : left_indent},500,function(){    
        $('.content_covers li:first').before($('.content_covers li:last')); 
		$('.content_covers').css({'left' : '0'});
        });
	});
		
	//move the text
    $('.content_names li:first').before($('.content_names li:last')); 
		$('.rightarrow').click(function(){
			var item_width = $('.content_names li').outerWidth() ;
			var left_indent = parseInt($('.content_names').css('left')) - item_width;
			$('.content_names:not(:animated)').animate({'left' : left_indent},500,function(){    
			$('.content_names li:last').after($('.content_names li:first')); 
			$('.content_names').css({'left' : '0'});
			}); 
		});
        
        $('.leftarrow').click(function(){
			var item_width = $('.content_names li').outerWidth();
			var left_indent = parseInt($('.content_names').css('left')) + (item_width);
			$('.content_names:not(:animated)').animate({'left' : left_indent},500,function(){    
			$('.content_names li:first').before($('.content_names li:last')); 
            $('.content_names').css({'left' : '0'});
            });
        });	
		
});

//loginLightbox TO ADD MOVIE
$(document).ready(function() {
	$('.block3 a').click(function() {
		
                //Getting the variable's value from a link 
		var newMovie = $(this).attr('href');

		//Fade in the Popup
		$(newMovie).fadeIn(300);
		
		//Set the center alignment padding + border see css style
		var popMargTop = ($(newMovie).height() + 24) / 2; 
		var popMargLeft = ($(newMovie).width() + 24) / 2; 
		
		$(newMovie).css({ 
			'margin-top' : -popMargTop,
			'margin-left' : -popMargLeft
		});
		
		// Add the mask to body
		$('body').append('<div id="mask"></div>');
		$('#mask').fadeIn(300);
		
		return false;
	});
	
	// When clicking on the mask layer the popup closed
	$('#mask').live('click', function() { 
	  $('#mask , .addmovie-popup').fadeOut(300 , function() {
		$('#mask').remove();  
	}); 
	return false;
	});
	
	// Clicking on X popup closes
	$('.close').click(function() {
	  $('#mask , .addmovie-popup').fadeOut(300 , function() {
		$('#mask').remove();  
	  }); 
	return false;
	});
});

// load Add Movie when click questions via Ajax
$(document).ready(function() {
	$('.block3 a').click(function(ev) {
		ev.preventDefault();
		var url = $(this).attr('href');
		$('#login-box').load('warm-oasis-9454.herokuapp.com/home/add_movie/');
	});
});	

