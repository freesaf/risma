var LightBox = function(options) {
	 settings = {parent : "" , el : "li",  content : "", padding : 30 , pourcentage_redimensionement : 0.8, delay : 1000, type : "thumb" , width_thumb : 90, min_width : 500  };
	 jQuery.extend(settings, options);
	 var $lightbox = {
		parent : "",
		el : "",
		content : "",
		padding : "",
		photo : new Image(),
		width_img : 0,
		height_img : 0,
		pourcentageImage : 0,
		delay : 0,
		nombre_img : "",
		current : 0,
		current_elem:"",
		src : "",
		img_p : "",
		padding_bottom : "",
		description : "",
		instance : 0,
		idparent : "",
		id_overlay : "overlay",
		id_box : "",
		id_photo : "",
		id_description : "",
		id_nav : "",
		id_navigation : "",
		id_fermer : "",
		type : "",
		width_thumb : 0,
		width_minigallery : 0,
		init : function() {
		    $lightbox.parent = $("#"+settings.parent);
		    $lightbox.el = settings.el;
		    $lightbox.content = settings.content;
		    $lightbox.padding = settings.padding;
		    $lightbox.pourcentageImage = settings.pourcentage_redimensionement;
		    $lightbox.delay = settings.delay;
		 	$lightbox.nombre_img = $($lightbox.parent).find($lightbox.el).length;
		 	var description_img;
		 	var src_img;
		 	$lightbox.idparent = settings.parent;
		 	$lightbox.id_overlay  = "#overlay_"+$lightbox.idparent;
		 	$lightbox.id_box  = "#box_"+$lightbox.idparent;
		 	$lightbox.id_photo  = "#photo_"+$lightbox.idparent;
		 	$lightbox.id_description  = "#description_"+$lightbox.idparent;
		 	$lightbox.id_nav  = "#nav_"+$lightbox.idparent;
		 	$lightbox.id_navigation  = "#navigation_"+$lightbox.idparent;
		 	$lightbox.id_fermer  = "#fermer_"+$lightbox.idparent;
		 	$lightbox.type = settings.type;
		 	$lightbox.width_thumb = settings.width_thumb;
		 	var id_overlay_  = "overlay_"+$lightbox.idparent;
		 	var id_box_  = "box_"+$lightbox.idparent;
		 	var id_photo_  = "photo_"+$lightbox.idparent;
		 	var id_description_  = "description_"+$lightbox.idparent;
		 	var id_nav_  = "nav_"+$lightbox.idparent;
		 	var plus_info = "infos_"+$lightbox.idparent;
		 	var id_navigation_  = "navigation_"+$lightbox.idparent;
		 	var id_fermer_  = "fermer_"+$lightbox.idparent;
		 	var overlay_box = "<div class='overlay' id="+id_overlay_+"> <div class='box' id="+id_box_+">" +
		 	"<div class='photo_lb' id="+id_photo_+"></div>  <div class='nav_lb' id="+id_nav_+">" +
		 	"<div id="+id_description_+" class='description_lb'></div>" +
		 	"<div class='navigation_lb right' id="+id_navigation_+">" +
		 	"<ul><li class='prev_lb'></li><li class='thumbnails_photos thumbnails_"+$lightbox.idparent+"'></li><li class='next_lb'></li></ul>" +
		 	"</div> <div class='clr'></div><!--<span class='description_lb' id="+id_description_+"></span>--><span class='fermer_lb' id="+id_fermer_+"><img src='/site_media/images/pixel.gif' width='25' height='25' /></span></div></div>  </div>";
		 	$("body").prepend(overlay_box);
		 	for(var i=0;i<$lightbox.nombre_img;i++){
		 		description_img = $($lightbox.parent).find($lightbox.el).eq(i).find("img").attr("alt");
		 		src_img = $($lightbox.parent).find($lightbox.el).eq(i).find("img").attr("src");
		 		$($lightbox.parent).find("li").eq(i).find("a").attr("title" , description_img);
		 		var class_li = $($lightbox.parent).find($lightbox.el).eq(i).attr("class");
		 		if(class_li != "video"){
		 			//$($lightbox.parent).find("li").eq(i).find("a").attr("rel" , src_img);	
		 		}
		 	}
		 	$lightbox.listeners();
		 	 if( $lightbox.type == "thumb" ) {
				 $lightbox.createMiniGallery();
			 }
		 	$lightbox.gestion_clavier();
		 },
		 onReady : function(ready) {
        	 if(typeof ready == 'function'){
        		 ready.call(this, "");
        	  }  
         },
		 fermer_box : function()  {
			 $($lightbox.id_overlay).fadeOut($lightbox.delay/2);
			 $($lightbox.id_photo).html('');
		 },
		 modal : function() {
			 if(content!=""){
			 		var content_html = $($lightbox.content).html();
			 		$($lightbox.id_overlay).fadeIn($lightbox.delay/2);
			 		var cont_html = "<div id=box_html_"+$lightbox.idparent+">"+content_html+"</div>";
			 		$($lightbox.id_photo).html(cont_html); 
			 		$($lightbox.id_box).width(700);
			 		$($lightbox.id_box).height("auto");
			 		var height_box = $($lightbox.id_box).height();
			 		if(height_box > 600){
			 			height_box = 600;
			 			$($lightbox.id_box).height(height_box);
			 		}
			 		$($lightbox.id_box).css("overflow" , "auto");
			 		$($lightbox.id_navigation).hide();
			 		$($lightbox.id_description).html("");
			 		$("#infos_lightbox_edition").html("<h1 class='font23 uppercase'>D INFOS <br />SUR <span class='artiste_color'>CHEB KHALED</span></h1>");
				 }
		 },
		 listeners : function() {
			 $lightbox.click_img();
		 	$($lightbox.id_fermer).click(function(){
		 		$lightbox.fermer_box();
		 	});
		 	/*$($lightbox.id_box).mouseleave(function(){
		 		$($lightbox.id_overlay).click(function(){
		 			$lightbox.fermer_box();
		 		})
		 	})*/
		 	$($lightbox.id_navigation).find("li").click(function() {
		 		var class_this = $(this).attr("class");
		 		switch (class_this){
			 		case "prev_lb" : 
			 			$lightbox.prev_img();	
			 		break;
			 		case "next_lb" : 
			 			$lightbox.next_img();
			 		break;
			 		default : 	
			 		break;
		 		}
		 	});
		 	
		 },
		 gestion_clavier : function() {
        	 $(window).keydown(function(event){
        		//console.log(event.keyCode);
 				switch (event.keyCode) {
	 				case 39: 
	 					//if($lightbox.current < $lightbox.nombre_img-1)$lightbox.next_img();
	 				break;
	 				case 37 : 
	 					///if($lightbox.current > 0)$lightbox.prev_img();
		 			break;
	 				case 27 : 
	 					$lightbox.fermer_box();
	 				break;
	 				default : 
	 					//$($lightbox.id_overlay).fadeOut($lightbox.delay/2);
		 			break;
 				}
 			});
         },
		 click_img : function() {
			 $($lightbox.parent).find($lightbox.el).click(function(evt){
				 var index = $($lightbox.parent).find($lightbox.el).index(this);
				 $lightbox.current = index;
				 $lightbox.current_elem = $(this);
				 if( $lightbox.type == "thumb" ){
					 $lightbox.scroller_miniGallery($lightbox.current);
					 $('.thumb').removeClass('active_thumb'); 
					 $('.thumb').eq($lightbox.current).addClass('active_thumb'); 
				 }
				 $($lightbox.id_photo).html('<span class="loading"></span>');
				 var height_box = $($lightbox.id_box).height();
				 $($lightbox.id_photo).find('.loading').height(height_box);
				 $lightbox.load_image();
				 if( index < $lightbox.nombre_img-1){
					  $(".next_lb").animate({ opacity : 1 });
					  $(".prev_lb").animate({ opacity : 1 });
				  }
				  else {
					  $(".next_lb").animate({ opacity : 0 });
				  }
				  if( index > 0){
					  $(".next_lb").animate({ opacity : 1 });
					  $(".prev_lb").animate({ opacity : 1 });
				  }
				  else {
					   $(".prev_lb").animate({ opacity : 0 });
				  }
				  /*if($lightbox.current == 0){
						 $(".next_lb").animate({ opacity : 1 });
						 $(".prev_lb").animate({ opacity : 0 });
				  }
				  if($lightbox.current == $lightbox.nombre_img-1){
					  $(".next_lb").animate({ opacity : 0 });
						 $(".prev_lb").animate({ opacity : 1 });
				  }*/
				  evt.preventDefault();
			 });
		 },
		 widthBox : 0,
		 load_image : function() { 
			 $lightbox.src = $($lightbox.current_elem).find("a").attr("rel");
			 var class_elem = $($lightbox.current_elem).hasClass("video");
			 $($lightbox.id_nav).hide(); 
			 $('.thumb').removeClass('active_thumb'); 
			 $('.thumb').eq($lightbox.current).addClass('active_thumb');
			 console.log(class_elem);
			 if(class_elem) {
					$($lightbox.id_overlay).fadeIn($lightbox.delay/2);
					$($lightbox.id_navigation).show();
					$($lightbox.id_photo).html($lightbox.src);
					var find_object = $($lightbox.id_photo).find("object").width();
					var find_iframe = $($lightbox.id_photo).find("iframe").width();
					var cible_find;
					if(find_object>0){
						cible_find = "object";
					}
					if(find_iframe>0){
						cible_find = "iframe";
					}
					$lightbox.width_img = $($lightbox.id_box).find(cible_find).width();
					$lightbox.height_img = $($lightbox.id_box).find(cible_find).height(); 
					$lightbox.padding_bottom = $($lightbox.id_nav).height();
					$($lightbox.id_photo).html($lightbox.src);
					$lightbox.widthBox = $lightbox.width_img+$lightbox.padding;
					if($lightbox.widthBox<settings.min_width){
						$lightbox.widthBox = settings.min_width;
					}
				    $($lightbox.id_box).animate({ width : $lightbox.widthBox , height : $lightbox.height_img+$lightbox.padding+$lightbox.padding_bottom }, $lightbox.delay); 
				    $lightbox.finalise_box();
				    $lightbox.description = $($lightbox.current_elem).find("a").attr("title");
				    $($lightbox.id_description).html($lightbox.description+" ("+($lightbox.current+1)+"/"+$lightbox.nombre_img+")");
			  }
			  else {
					$lightbox.img_p = "<img src='"+$lightbox.src+"' alt='' />";	
					$($lightbox.id_description).html("");
					$lightbox.description = $($lightbox.current_elem).find("a").attr("title");
					//$(".infos_lightbox_edition").html("<h1 class='font23 uppercase'>D'INFOS <br />SUR <span class='artiste_color'>CHEB KHALED</span></h1>");
					 $lightbox.photo = new Image();
					$lightbox.photo.onload = function() {
				    	 $($lightbox.id_overlay).fadeIn($lightbox.delay/2);
				    	 $($lightbox.id_navigation).show();
				    	 $lightbox.padding_bottom = $($lightbox.id_nav).height();
					     $($lightbox.id_photo).html($lightbox.src); 
						 $($lightbox.id_photo).html($lightbox.img_p);
						 $($lightbox.id_box).find("img").eq(0).css("opacity" , 0);
						 $lightbox.width_img = this.width;
						 $lightbox.height_img = this.height;
						 $lightbox.adaptation();
					}			
					$lightbox.photo.src=$lightbox.src;
			  } 
		 },
		createMiniGallery : function(){
			 var src_thumb;
			 var images_gallery_class = "images_mini_"+$lightbox.idparent;
			 var galleryHTML = '<div class="images_mini '+images_gallery_class+'"><ul class="horizontal"></ul></div>';
			 $('.thumbnails_'+$lightbox.idparent).html(galleryHTML);
			 var thumb_w = $lightbox.width_thumb+45;
			 $("."+images_gallery_class).width($lightbox.nombre_img*thumb_w);
			 for( var i=0;i<$lightbox.nombre_img;i++ ){
				 src_thumb = $($lightbox.parent).find($lightbox.el).eq(i).find('img').attr("src");
				 $('.thumbnails_'+$lightbox.idparent).children("."+images_gallery_class).children('ul').append('<li class="thumb"> <img src='+src_thumb+' /></li>');
			 }
			 $lightbox.click_thumbs();
		 },
		 click_thumbs : function(){
			  $('.thumbnails_'+$lightbox.idparent).find('li').children('img').click(function(){
				  var index = $('.thumbnails_'+$lightbox.idparent).find('li').children("img").index(this);
				  $lightbox.current = index;
				  $('.thumb').removeClass('active_thumb'); 
				  $(this).parent('.thumb').addClass('active_thumb'); 
				  $lightbox.current_elem = $($lightbox.parent).find($lightbox.el).eq($lightbox.current);
				  $($lightbox.id_photo).html('<span class="loading"></span>');
					 var height_box = $($lightbox.id_box).height();
					 $($lightbox.id_photo).find('.loading').height(height_box);
				  $lightbox.load_image(); 
				  $lightbox.scroller_miniGallery(index);
				  if( index < $lightbox.nombre_img-1){
					  $(".next_lb").animate({ opacity : 1 });
					  $(".prev_lb").animate({ opacity : 1 });
				  }
				  else {
					  $(".next_lb").animate({ opacity : 0 });
				  }
				  if( index > 0){
					  $(".next_lb").animate({ opacity : 1 });
					  $(".prev_lb").animate({ opacity : 1 });
				  }
				  else {
					   $(".prev_lb").animate({ opacity : 0 });
				  }
			  })
		 },
		 scroller_miniGallery : function(index){
			 var images_gallery_class = "images_mini_"+$lightbox.idparent;
			 var mini_imagesGallery = $("."+images_gallery_class).width();
			 var width_minigallery = $('.thumbnails_'+$lightbox.idparent).width();
			 var thumb_w = $lightbox.width_thumb+10;
			 if( mini_imagesGallery > width_minigallery){
				 $("."+images_gallery_class).animate({ left : -thumb_w*index },500)
			 }
		 },
		adaptation : function() {
					widthWindow = $(".overlay").width();
					heightWindow = $(".overlay").height();
					var pi;
					var height_total = ((heightWindow*$lightbox.pourcentageImage)-110);
					if($lightbox.width_img>widthWindow || $lightbox.height_img > height_total ) {
					     ratioWindow = widthWindow/heightWindow; 
					     ratioImage = $lightbox.width_img/$lightbox.height_img;
						 if(ratioWindow>=ratioImage) {
							pi = heightWindow/$lightbox.height_img;
						 }
						 if(ratioWindow<=ratioImage) {
							pi =widthWindow/widthLi;
						 }
			             resultatW = $lightbox.pourcentageImage*pi*$lightbox.width_img;
			             resultatH = $lightbox.pourcentageImage*pi*$lightbox.height_img;
			             $lightbox.width_img = resultatW;
			             $lightbox.height_img = resultatH;
			             $lightbox.widthBox = resultatW+$lightbox.padding;
				    	 if($lightbox.widthBox<settings.min_width){
							$lightbox.widthBox = settings.min_width;
						 }
						 $($lightbox.id_box).animate({ width : $lightbox.widthBox , height : resultatH+$lightbox.padding+$lightbox.padding_bottom}, $lightbox.delay);
					     $($lightbox.id_box).css("top" , (heightWindow-($lightbox.height_img+110))/5);
					     $($lightbox.id_box).find("img").eq(0).animate({ opacity : 1, width :resultatW , height : resultatH - $lightbox.padding }, $lightbox.delay);
					     $lightbox.finalise_box();
				      }
				      else {
				    	  $lightbox.widthBox = $lightbox.width_img+$lightbox.padding
				    	  if($lightbox.widthBox<settings.min_width){
								$lightbox.widthBox = settings.min_width;
							}
				           $($lightbox.id_box).animate({ width : $lightbox.widthBox , height : $lightbox.height_img+$lightbox.padding+$lightbox.padding_bottom }, $lightbox.delay);
				           $($lightbox.id_box).find("img").eq(0).animate({ opacity : 1 }, $lightbox.delay);
				           $lightbox.finalise_box();
				      }
		 },
		finalise_box : function() {
			 $($lightbox.id_nav).fadeIn($lightbox.delay);
			 $($lightbox.id_description).fadeIn($lightbox.delay);
			 $($lightbox.id_description).html($lightbox.description+" ("+($lightbox.current+1)+"/"+$lightbox.nombre_img+")");
		 },
		next_img : function(){
			 if($lightbox.current < $lightbox.nombre_img-1){
				 $lightbox.current++;
				 if( $lightbox.type == "thumb" ){
					 $lightbox.scroller_miniGallery($lightbox.current);
				 }
				 $lightbox.current_elem = $($lightbox.parent).find($lightbox.el).eq($lightbox.current);
				 $($lightbox.id_photo).html('<span class="loading"></span>');
				 var height_box = $($lightbox.id_box).height();
				 $($lightbox.id_photo).find('.loading').height(height_box);
				 $lightbox.load_image();
				 $(".next_lb").animate({ opacity : 1 });
				 $(".prev_lb").animate({ opacity : 1 });
			 }
			 else {
				 $(".next_lb").animate({ opacity : 0 });
    		 }
			/* if($lightbox.current == $lightbox.nombre_img){
				 $(".next_lb").hide();
				 $(".prev_lb").show();
			 }*/
			 
		 },
		prev_img : function() {
			 if($lightbox.current > 0){
				 $lightbox.current--;
				 if( $lightbox.type == "thumb" ){
					 $lightbox.scroller_miniGallery($lightbox.current);
				 }
				 $lightbox.current_elem = $($lightbox.parent).find($lightbox.el).eq($lightbox.current);
				 $($lightbox.id_photo).html('<span class="loading"></span>');
				 var height_box = $($lightbox.id_box).height();
				 $($lightbox.id_photo).find('.loading').height(height_box);
				 $lightbox.load_image();
				 $(".next_lb").animate({ opacity : 1 });
				 $(".prev_lb").animate({ opacity : 1 });
			 }
			 else {
				 $(".prev_lb").animate({ opacity : 0 });
    		 }
			/* if($lightbox.current == 1){
				 $(".next_lb").show();
				 $(".prev_lb").hide();
			 }*/
		 }
	 }
	 $lightbox.init();
	 return $lightbox;
}