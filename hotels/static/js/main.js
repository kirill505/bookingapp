$(document).ready(function(){

	$('.hotel-slider').owlCarousel({
	    loop:false,
	    responsiveClass:true,
	    responsive:{
	        0:{
	            items:1,
	            nav:false,
	            dots:false,
	            loop:true
	        },
	        600:{
	            items:1,
	            nav:false,
	            dots:false,
	            loop:true
	        },
	        1000:{
	            items:3,
	            nav:false,
	            dots:false,
	            loop:false
	        }
	    },
	});

	$('.card-description-more').on('click',function()
	{
		$('.card-description').toggleClass('open');
	});

});