

// load Answers when click questions via Ajax
// load Answer when clicking question
	$(document).ready(function() {
		var url;
		var answerHeight = $(window).height();
		$('.question a').click(function(ev) {
			url = $(this).attr('href');

			$('.answers').load(url, function() {
				$('#AnswerBox textareas').addClass('mceEditor');
				 tinyMCE.init({ 
					theme : "advanced", 
					mode : "textareas", 
					plugins : "fullpage", 
					theme_advanced_buttons3_add : "fullpage" 
				  });
			}).hide().fadeIn("slow").css('height', answerHeight);    
		return false;
		});

	$('body').on('click', '#submitanswerbutton', function(ev) {
		var pathname = window.location.pathname;
		$('.answer-popup').load(url+'add_answer/');
	});
	return false;
});	

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

// add question
$(document).ready(function(){
  $('.addQuestionWindow').hide();

	var callQuestionWindow = function(){  
	  $('.questionbutton').click(function() {
			if ($('.addQuestionWindow').is(':visible')) {
				$('.addQuestionWindow').hide()
				} else { $('.addQuestionWindow').show()}
	  });
	  
	 }
 
callQuestionWindow();

});
	
	
//loginLightbox TO ATTACH TO ASK QUESTION SUBMIT BUTTON
$(document).ready(function() {
	$('.login-window').click(function() {
		
                //Getting the variable's value from a link 
		var loginBox = $(this).attr('href');

		//Fade in the Popup
		$('.login-popup').fadeIn(300);
		
		//Set the center alignment padding + border see css style
		var popMargTop = ($(loginBox).height() + 24) / 2; 
		var popMargLeft = ($(loginBox).width() + 24) / 2; 
		
		$(loginBox).css({ 
			'margin-top' : -popMargTop,
			'margin-left' : -popMargLeft
		});
		
		// Add the mask to body
		$('body').append('<div id="mask"></div>');
		$('#mask').fadeIn(300);
		
		return false;
	});
	
	// When clicking on the button close or the mask layer the popup closed
	$('a.close, #mask').live('click', function() { 
	  $('#mask , .login-popup').fadeOut(300 , function() {
		$('#mask').remove();  
	}); 
	return false;
	});
});

// load User Input questions
$(document).ready(function() {
	$('.questionbutton a').click(function(ev) {
		var pathname = window.location.pathname;
		$('#login-box').load(pathname+'add_question/');
	});
});

// Change question div color when hover
$(document).ready(function() {
	$('.question ul li, .answerandcomments').hover(function() {
		$(this).addClass('questionHover');
	}, function() {
		$(this).removeClass('questionHover');
	});
});



// Clicking on Ask a Question button on Answers page
$(document).ready(function() {
	$('body').on('click', '#submitanswerbutton', function(event){
			
                //Getting the variable's value from a link 
		var answerBox = $(this).attr('href');

		//Fade in the Popup
		$('.answer-popup').fadeIn(300);

		
		//Set the center alignment padding + border see css style
		var popMargTop = ($(answerBox).height() + 24) / 2; 
		var popMargLeft = ($(answerBox).width() + 24) / 2; 
		
		$(answerBox).css({ 
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
	  $('#mask , .answer-popup').fadeOut(300 , function() {
		$('#mask').remove();  
 		
	}); 
	return false;
	});
});

// Set question div to height
$(document).ready(function() {
	var questionHeight = $(window).height();
	console.log(questionHeight);
	$('.question').css('height', questionHeight * 0.878);
});

// custom jScrollbar
$(document).ready(function() {
	$('.question').jScrollPane(
		{
			arrowScrollOnHover: false
		}
	);
});
