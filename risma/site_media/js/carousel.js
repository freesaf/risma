var instance = 0;
var Ncarousel = function(options) {
	instance++;
	 settings = { parent: "carousel", reportoire_media:"/site_media/", type_alignement:"horizontal"  ,diaporama : false, effet : "slide"  , auto_start : 1 , 
		 auto_play : true , ratio_autoplay : 2.5  , delay : 1500 , type_navigation : "cercle", pourcentage_redimensionement : 0.8 };
	     jQuery.extend(settings, options); 
		 // l'objet principale de carousel
		 var $carousel = {
				 parent : "",
				 start : "",
				 width_parent : "" ,
				 width_arrow : "" ,
				 height_arrow : "" ,
				 bloc_description : "" ,
				 auto_Play : "" ,
				 delay : "" ,
				 ratio_autoplay : "" ,
				 type_navigation : "" ,
				 result_type_nav : "" ,
				 effet : "" ,
				 nav_parent : "" ,
				 play_parent : "" ,
				 repertoire_media : "" ,
				 type_alignement : "" ,
				 width_thumb : "" ,
				 images_ncarousel : "",
				 nav_ncarousel : "",
				 sous_images_nav : "",
				 id_parent : "",
				 next_id : "",
				 prev_id : "",
				 diaporama : "",
				 start_declenche : false,
				 pourcentage_redimensionement : 0,
				 init : function() {
					 $carousel.parent = $("#"+settings.parent);
					 $carousel.start = settings.auto_start;
					 $carousel.width_parent = $($carousel.parent).find("li").eq(0).width();
					 $carousel.height_parent = $($carousel.parent).height();
					 $carousel.width_arrow= 51;
					 $carousel.height_arrow = 51;
					 $carousel.bloc_description = $("#description_"+settings.parent);
					 $carousel.auto = settings.auto_play;
					 $carousel.delay = settings.delay;
					 $carousel.ratio_autoplay = settings.ratio_autoplay;
					 $carousel.type_navigation = settings.type_navigation;
					 $carousel.result_type_nav;
					 $carousel.effet = settings.effet;
					 $carousel.nav_parent = $("#navigation_"+settings.parent);
					 $carousel.play_parent = $("#player_"+settings.parent);
					 $carousel.repertoire_media = settings.reportoire_media;
					 $carousel.type_alignement = settings.type_alignement;
					 $carousel.width_thumb = 10;
					 $carousel.next_id = $("#next_"+settings.parent);
					 $carousel.prev_id = $("#prev_"+settings.parent);
					 $carousel.diaporama = settings.diaporama;
					 $carousel.pourcentage_redimensionement = settings.pourcentage_redimensionement;
					 lightbox = settings.lightbox;
					 $carousel.Auto_start();
		         },
				 // cette function c'est la function d'initialisation de l'objet carousel
		         Auto_start : function() {
			        	 $carousel.create_conteneur();
			        	 $carousel.current = $carousel.start;
			        	 $carousel.start_declenche = true;
			        	 if(settings.effet == "slide_boucle"){
							$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).addClass("act");
						  } 
			        	 if($carousel.type_navigation == "cercle" ) {
			        		 $("."+$carousel.nav_ncarousel).find("ul").find("li").eq($carousel.current-1).addClass('cercle_active');
			        		 $(".cercle_active").html("<img src="+$carousel.repertoire_media+"images/cercle_active.png alt='cercle_active' />");
			        	 }
			        	 if($carousel.current==1){
		        			$($carousel.prev_id).hide(); 
		        		 }
		        		 else {
		        			$($carousel.prev_id).show();
		        		 }
			        	 //$carousel.auto_play($carousel.auto);
			        	 if($carousel.effet == "fade" ){
			        		 $("."+$carousel.images_ncarousel).find("li").hide();
			        		 $("."+$carousel.images_ncarousel).find("li").eq($carousel.current).show();
			        	 }
			        	 $carousel.current_function();
			        	 $carousel.description_content = $($carousel.parent).find("."+$carousel.images_ncarousel).find("ul").find("li").eq($carousel.current-1).find("img").attr("alt");
				         $($carousel.bloc_description).html($carousel.description_content);
		         },
				 nombre_images : 0,
				 current : 1 ,
				 description_content : "",
				 pas : 0,
				 width_sous_li : 0,
				 margin : 10,
				 class_active : "",
				 timer : "",
				 portrait : false,
				 arrow_current : "",
				 etat_img_clic : false,
				 repertoire_media :"",
		         // function qui est responsable de creation la partie dynamique de html de carousel 
				 create_conteneur : function(){
		        	    $carousel.id_parent = $carousel.parent.attr("id");
		        	    $carousel.images_ncarousel = "images_"+$carousel.id_parent; 
		        	    $carousel.nav_ncarousel = "nav_"+$carousel.id_parent;
		        	    sous_images_nav = ".sous_images_nav_"+$carousel.id_parent;
			 			$($carousel.parent).find('ul').wrap("<div class='"+$carousel.images_ncarousel+"' />");
			 			var images_div = $($carousel.parent).find("."+$carousel.images_ncarousel);
			 			$carousel.nombre_images = $carousel.parent.find("li").length;
			        	$carousel.pas = $carousel.parent.find("li").width();
						if( $carousel.pas == 0 ) {
							$carousel.pas = $("#back").width();
						}
						console.log($carousel.pas);
			        	repertoire_media =  $carousel.reportoire;
			        	if( $carousel.effet != "fade" ) {
			        		$(images_div).width($carousel.nombre_images * $carousel.pas+1000);
			        	}	
			 			$carousel.create_navigation();
			 			$carousel.create_play_btn();
			 			if($carousel.effet == "slide_boucle"){
			 				$($carousel.parent).find("."+$carousel.images_ncarousel).find("li").css("position" , "absolute");
			 				for(var i=0;i<$carousel.nombre_images;i++){
				 				$("."+$carousel.images_ncarousel).find("li").eq(i).css("left" ,$carousel.width_parent );
				 			}
				 			$("."+$carousel.images_ncarousel).find("li").eq(0).css("left" , 0);
				 			$('#next_carousel').hide();
			 				$('#prev_carousel').hide();	
						}
			 			else {
			 				$carousel.create_arrow();
			 				
			 			}
			 			if($carousel.effet == "fade"){
			 				$($carousel.parent).find("."+$carousel.images_ncarousel).find("li").fadeOut(10);
			 				$($carousel.parent).find("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).fadeIn($carousel.delay, function(){
			 					
			 				});
			 			}
			 			if($carousel.effet == "slide_vertical"){
			 				$($carousel.parent).find("."+$carousel.images_ncarousel).width($carousel.width_parent);
			 			}
						if($carousel.type_alignement == "vertical"){
			 				$($carousel.parent).css("float" , "left");
			 				$($carousel.nav_parent).find("."+$carousel.nav_ncarousel).width($carousel.width_thumb);
			 			}
						else {
							//$carousel.create_arrow();
						}
						
		         },
		         // cette function qui créer les fleche de navigation de carousel
		         create_arrow : function() {
			        	var arrow_left = "<div class='prev_carousel'></div>";
			        	var arrow_right = "<div class='next_carousel'></div>";
			        	$($carousel.prev_id).append(arrow_left);
			        	$($carousel.next_id).append(arrow_right);
			        	var width_arrow = $($carousel.prev_id).width();
			        	var height_arrow = $($carousel.prev_id).height();
			        	$($carousel.prev_id).html("<img src="+$carousel.repertoire_media+"images/pixel.gif width="+width_arrow+" height ="+height_arrow+" />");
			        	$($carousel.next_id).html("<img src="+$carousel.repertoire_media+"images/pixel.gif width="+width_arrow+" height ="+height_arrow+" />");
			        	$carousel.click_arrow ();
		         },
		         // cette function qui contient les listeners de l'evenement click sur les fleches de navigation de carousel
		         click_arrow : function() {
			        	 $($carousel.next_id).click(function(){
			        		 $carousel.arrow_current = $(this);
			        		 $carousel.click_next();
			        	 });
			        	 $($carousel.prev_id).click(function(){
			        		 $carousel.arrow_current = $(this);
			        		 $carousel.click_prev();
			        	 })
		         },
		         delay_retrun : function(time, callback){
		 				//var timer_delay = setTimeout(""+callback+"", time);
		 				jQuery.fx.step.delay = function(){};
		 				return $(this).stop(true, false).animate({delay:1}, time, callback);
		         },
		         // cette function qui gere le passage de l'image suivant 
		         click_next : function() {
		        	 if($carousel.current < $carousel.nombre_images){
	        			 $carousel.current++;
	        			 $(this).fadeIn(500);
	        			 $($carousel.prev_id).fadeIn(500);
	        			 // $carousel.pausing_click();
	        			 $carousel.auto = false;
	        			 $carousel.current_function();	 
	        			 $carousel.delay_retrun($carousel.delay*2, function(){
	        				 $carousel.auto = true;
	        				 $carousel.auto_play($carousel.auto);
	        				 //$carousel.current_function();
	        			 });
	        		 }
	        		 else {
	        			 $($carousel.next_id).fadeOut(500);
	        		 }
		        	 if($carousel.current == $carousel.nombre_images){
		        		  $($carousel.next_id).fadeOut(500);
		        		  $($carousel.prev_id).fadeIn(500);
		        	 }
		         },
		         // cette function qui gere le passage de l'image precedant
		         click_prev : function() {
		        	 if($carousel.current > 1){
	        			 $($carousel.arrow_current).fadeIn(500);
	        			 $($carousel.next_id).fadeIn(500);
	        			 $carousel.current--;
	        			// $carousel.pausing_click();
	        			 $carousel.current_function();
	        			 $carousel.auto = false;
	        			$carousel.delay_retrun($carousel.delay*2, function(){
	        				 $carousel.auto = true;
	        				 $carousel.current_function();
	        			 });	 
	        		 }
	        		 else {
	        			 $($carousel.prev_id).fadeOut(500);
	        		 }
		        	 if($carousel.current == 1){
		        		  $($carousel.prev_id).fadeOut(500);
		        		  $($carousel.next_id).fadeIn(500);
		        	 }
		         },
		         // cette function qui créer la conteneur de la navigation de carousel
		         create_navigation : function() {
		        	 var div_nav = "<div class="+$carousel.nav_ncarousel+"></div>";
				      $($carousel.nav_parent).html(div_nav); 
				        	 var nav_elem = $("."+$carousel.nav_ncarousel);
				        	 $(nav_elem).append("<ul></ul>");
				        	 for(var i = 0;i<$carousel.nombre_images;i++){
				        		 switch ($carousel.type_navigation) {
						     		case "number":
						     			  $carousel.result_type_nav = (i+1);
						     			  $carousel.class_active = "nav_active";
						     			break;
						     		case "cercle" : 
						     			 $carousel.result_type_nav = "<img src='"+$carousel.repertoire_media+"images/cercle.png' alt='cercle' class='cercle' />";
						     			 $carousel.class_active = "cercle_active";
						     			break;
						     		case "thumb" : 
						     			var src_img = $($carousel.parent).find("."+$carousel.images_ncarousel).find("ul").find("li").eq(i).find("img").attr("src");
						     			$carousel.result_type_nav = "<img src='"+src_img+"' alt='thumb' class='thumb' />";
						     			$(".thumb").parent("li").css("opacity" , 0.5);
						     			$carousel.class_active = "thumb_active";
						     			$carousel.width_thumb = $("."+$carousel.nav_ncarousel).find("li").width();
						     			var player_carousel = $($carousel.play_parent).width();
						     			var nav_carousel_width = $($carousel.nav_parent).parent("div").width();
						     			var diff = nav_carousel_width - player_carousel;
						     			if($carousel.width_thumb*($carousel.nombre_images+2)>diff){
						     				$(nav_elem).children("ul").wrap("<div id=mini_images_"+$carousel.id_parent+" />");
						     				//$("#mini_images_"+$carousel.id_parent).width($carousel.width_thumb*($carousel.nombre_images+3));
						     				//$(nav_elem).width(diff- ($carousel.width_thumb*2));
						     				$(nav_elem).css({"overflow" : "hidden" , "position" : "relative"});
						     			}
						     			else {
						     				$(nav_elem).width($carousel.width_thumb*($carousel.nombre_images+2));
						     			}
						     			break;
						     		default:
						     			$carousel.result_type_nav = (i+1);
						     			break;
						     	}
				        		
				        		$(nav_elem).find("ul").append("<li id=nav_"+(i+1)+">"+$carousel.result_type_nav+"</li>");
			        	    }
			        	 var nav_elem_width = $(nav_elem).width();
		        		 if(nav_elem_width > $carousel.width_parent){
		        			 // creer un sous galerie pour le thumbnails
		        			 var n_s = $carousel.sous_images_nav;
		        			 var n_s_n = n_s.substring(1,n_s.length);
		        			 $(nav_elem).find("ul").wrap("<div class="+n_s_n+" />");
		        			 $carousel.width_sous_li = $(nav_elem).find("li").width()+ $carousel.margin;
		        			 //$(nav_elem).width($carousel.width_parent - ($carousel.width_sous_li-$carousel.margin));
		        			 $($carousel.sous_images_nav).width($carousel.nombre_images * ($carousel.width_sous_li));
		        			 $(nav_elem).css("overflow" , "hidden");
		        		 }
			        	$carousel.nav_click();
		         },
		         // cette function qui créer les boutons play et pause pour l'autoplay du carousel
		         create_play_btn : function() {
		        	 if($carousel.diaporama){
		        		 var play_diaporama_html = "<li class='play'><img src='"+$carousel.repertoire_media+"images/pixel.gif' width='13' height='14' title='play'  alt='play' /></li>" +
		        		 		"<li class='pause'><img src='"+$carousel.repertoire_media+"images/pixel.gif' width='13' height='14' alt='pause' title='pause' /></li>" +
		        		 		"<li class='stop'><img src='"+$carousel.repertoire_media+"images/pixel.gif' width='13' height='14'  alt='stop' /></li>";
		        		 $($carousel.play_parent).find("ul").html(play_diaporama_html);
		        		 $carousel.stop_btn($carousel.play_parent);
		        		 if($carousel.auto_Play){  
			        		  $carousel.pause_btn($carousel.play_parent);
			        	 }
			        	 else {
			        		 $carousel.play_btn($carousel.play_parent);
			        	 }
		        	 }
		        	 else {
		        		 var play_div = "<div class='play_btn'> <span class=play_"+$carousel.id_parent+"><img src="+$carousel.repertoire_media+"images/play.png /></span></div>";
		        		 var pause_div = "<div class='play_btn'><span class=pause_"+$carousel.id_parent+"><img src="+$carousel.repertoire_media+"images/pause.png /></span></div>";
		        		 playbtns_html = play_div+pause_div;
			        	if($carousel.auto_Play){
				        	 $($carousel.play_parent).append(pause_div);
				        	 $carousel.pause_btn($carousel.play_parent);
				        }
				         else {
				        	$($carousel.play_parent).append(play_div);
				        	$carousel.play_btn($carousel.play_parent);
				        }
		        	  } 
		         },
		         // cette function contient le listeners de click sur le bouton play pour demarrer l'autoplay du carousel
		         play_btn : function(pr) {
		        	 var pl_btn;
		        	 if($carousel.diaporama){
		        		 pl_btn = $(pr).find(".play");
		        	 }
		        	 else {
		        		 pl_btn = $(pr).find(".play_"+$carousel.id_parent);
		        	 }
		        	 $(pl_btn).click(function(){
		        		$carousel.playing_click(pr);
		        		$carousel.on_play = true;
		        		$carousel.onPlay("");
		        	 });
		         },
		         // cette function contient le listeners de click sur le bouton pause pour annuler l'autoplay du carousel
		         pause_btn : function(pr) {
		        	 var pl_btn;
		        	 if($carousel.diaporama){
		        		 pl_btn = $(pr).find(".pause")
		        	 }
		        	 else {
		        		 pl_btn =  $(pr).find(".pause_"+$carousel.id_parent)
		        	 }
		        	$(pl_btn).click(function(){
		        		  $carousel.pausing_click(pr);
		        		  $carousel.on_pause = true;
			        	  $carousel.onPause("");
		        	 });
		         },
		         // cette function qui declenche l'autoplay apres le click sur le bouton Play
		         playing_click : function(pr) {
		        	 if($carousel.diaporama){
		        		 $(pr).find(".play").css("opacity" ,0.5 );
		        		 $(pr).find(".pause").css("opacity" ,1 );
		        		 $(pr).find(".stop").css("opacity" ,1 );
		        	 }
		        	 else {
		        		 $(pr).find(".play_btn").html("<span class=pause_"+$carousel.id_parent+"><img src="+$carousel.repertoire_media+"images/pause.png /></span>");
		        	 }
		        		$carousel.auto = true;
		        	    $carousel.auto_play($carousel.auto);
		        		$carousel.pause_btn(pr);
		         },
		         // cette function qui stopper l'autoplay apres le click sur le bouton Pause
		         pausing_click : function(pr) {
		        	    if($carousel.diaporama){
		        	    	 $(pr).find(".play").css("opacity" ,1 );
			        		 $(pr).find(".pause").css("opacity" ,0.5 );
			        		 $(pr).find(".stop").css("opacity" ,1 );
			        	 }
		        	    else {
		        	    	$($carousel.play_parent).find(".play_btn").html("<span class=play_"+$carousel.id_parent+"><img src="+$carousel.repertoire_media+"images/play.png /></span>");
		        	    }
		        	    $carousel.auto = false;
		        	    $carousel.auto_play($carousel.auto);
		        		$carousel.play_btn(pr);
		         },
		         current_nav : 0,
		         avance : true,
		         animer : true,
		         // cette function qui gere l'autoplay
		         auto_play : function(auto) {
	        	     if(auto){
		        		$carousel.timer = setTimeout($carousel.timing,$carousel.delay*$carousel.ratio_autoplay);
		        		$carousel.avance = true;
	        		 }
	        	     else {
	        	    	 clearTimeout($carousel.timer);
	        	     }
		         },
		         timing : function() { 
		        	 if($carousel.current < $carousel.nombre_images){	
	        			 $carousel.current++;
	    			     //$carousel.autoPlaying();
	        			 $carousel.current_function()
	    			     $carousel.avance = true;
	        			 $($carousel.next_id).fadeIn(500);
	        			 $($carousel.prev_id).fadeIn(500);
    			     }
        			else {
        				$carousel.current = 1;
        				$carousel.avance = false;
        				clearTimeout($carousel.timer);
        				$carousel.current_function();
        				//$($carousel.next_id).fadeOut(500);
        			}
		        	 if($carousel.current == $carousel.nombre_images){
		        		  $($carousel.next_id).fadeOut(500);
		        		  $($carousel.prev_id).fadeIn(500);
		        	 }
		        	 if($carousel.current == 1){
		        		  $($carousel.prev_id).fadeOut(500);
		        		  $($carousel.next_id).fadeIn(500);
		        	 }
		         },      
		         // cette function qui gere les click sur les elements de navigation du carousel
		         nav_click : function() {
		        	 $carousel.avance = true;
			        	  $("."+$carousel.nav_ncarousel).find("ul li").click(function(){
				        	        $carousel.animer = true; 
				        	        //clearInterval($carousel.timer);
						        	var elem_this = $(this);
						            var pr_this = $(elem_this).parent("ul");
						            var crnt = $(pr_this).find("li").index(this);
						        	$carousel.current_nav = $carousel.current;
						        	$carousel.current = parseInt(crnt+1);
						        	if($carousel.current > $carousel.nombre_images){
						        		$carousel.current = 1;	
				    			     }
						        	if(!elem_this.hasClass("cercle_active")){
						        		if($carousel.current < $carousel.current_nav) {$carousel.avance = false;}
							        	else {
							        		$carousel.avance = true;
							        	}
						        	} 
						        	$carousel.auto = false;
					        		$carousel.current_function();
						        	
						        	/*$carousel.pausing_click($carousel.play_parent);
					        		setTimeout(function(){
					        			$carousel.playing_click($carousel.play_parent);
					        		},1000);*/
			        	 });
		         },
		         // cette function qui est responsable sur la partie animation du carousel et elle gere aussi les differents types d'effet du carousel pour l'adapter ce qui est demande par l'utilisateur
		         current_function : function() {
		        	 
		        	 		$("."+$carousel.nav_ncarousel).find("ul").find("li").removeClass($carousel.class_active);
		        	 		$("."+$carousel.nav_ncarousel).find("ul").find("li").eq($carousel.current-1).addClass($carousel.class_active);
		        	        $($carousel.sous_images_nav).animate({ left : - (($carousel.current-1) * $carousel.width_sous_li) }, $carousel.delay);
		        	        $("#mini_images_"+$carousel.id_parent).animate({ left : - (($carousel.current-1) * ($carousel.width_thumb+10)) }, $carousel.delay);
				        	$carousel.description_content = $($carousel.parent).find("."+$carousel.images_ncarousel).find("ul").find("li").eq($carousel.current-1).find("img").attr("alt");
				        	$($carousel.bloc_description).html($carousel.description_content);
				        	if($carousel.type_navigation == "cercle"){
				        		$("."+$carousel.nav_ncarousel).find("ul").find("li").html("<img src="+$carousel.repertoire_media+"images/cercle.png alt='cercle' />");
				        		$(".cercle_active").html("<img src="+$carousel.repertoire_media+"images/cercle_active.png alt='cercle' />");
				        	}
				        	else {
					        		$("."+$carousel.nav_ncarousel).find("ul").find("li").animate({opacity : 0.5},300, function() {
					        			//$("."+$carousel.nav_ncarousel).find("ul").find("li").eq($carousel.current-1).animate({ opacity : 1 },300);
					        		});
					        		$("."+$carousel.nav_ncarousel).find("ul").find("li").eq($carousel.current-1).animate({ opacity : 1 },200);
					        		$("."+$carousel.nav_ncarousel).find("ul").find("li").removeClass("elem_active");
					        		$("."+$carousel.nav_ncarousel).find("ul").find("li").eq($carousel.current-1).addClass("elem_active");
				        	}
				        	switch ($carousel.effet){
					        	case "slide" :
					        		//$("."+$carousel.images_ncarousel).find('li').animate({ opacity : 0.2 },$carousel.delay/2);
					        		//$("."+$carousel.images_ncarousel).find('li').eq($carousel.current-1).animate({ opacity : 1 },$carousel.delay/2);
					        		$("."+$carousel.images_ncarousel).animate({ left : - (($carousel.current-1) * $carousel.pas) }, $carousel.delay, function(){
					        			$carousel.auto_play($carousel.auto);
					        		});
					        	break;
					        	case "slide_boucle" :
					        		var cr = $carousel.current;
									
					        		/*if($carousel.avance){
					        			for(var i=$carousel.current-1;i<$carousel.nombre_images;i++){
					        				$("."+$carousel.images_ncarousel).find("li").eq(i).css('left' , $carousel.width_parent );
					        			}
					        			$("."+$carousel.images_ncarousel).find(".act").animate({ left : -$carousel.width_parent }, $carousel.delay, function() {
						        			$carousel.current = cr;
						        			$("."+$carousel.images_ncarousel).find("li").removeClass("act");
						        			$("."+$carousel.images_ncarousel).find("li").css('left' , $carousel.width_parent );
						        			$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).addClass("act");
						        			$carousel.auto_play($carousel.auto);
						        			
						        			$("."+$carousel.images_ncarousel).find("li").css('left' , $carousel.pas );
						        			
						        		});
						        		$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).animate({ left : 0 }, $carousel.delay, function() {});
					        		}*/
									if ($carousel.avance) {
									}
									var n = $carousel.nombre_images+1;
										if( $carousel.current <= $carousel.nombre_images ) {
											
											$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).animate({ left : 0 }, $carousel.delay, function() {});
											$carousel.current = cr;
						        			$("."+$carousel.images_ncarousel).find("li").removeClass("act");
						        				
						        			$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).addClass("act");
											
						        			$carousel.auto_play($carousel.auto);
											//console.log($carousel.current + "  - "+ $carousel.nombre_images);
											
											
										 }
										 if ($carousel.current == 1 ){
										 	$("."+$carousel.images_ncarousel).find("li").eq(0).css('left' , $carousel.pas );
											$("."+$carousel.images_ncarousel).find("li").eq(0).css('left' , $carousel.pas );
											for(var i=0;i<$carousel.nombre_images;i++){
												if(! $("."+$carousel.images_ncarousel).find("li").eq(i).hasClass('act')  ) {
													$("."+$carousel.images_ncarousel).find("li").eq(i).css('left' , $carousel.pas );
												}
					        				}
											//   $("."+$carousel.images_ncarousel).find(".act").eq(i).css('left' , 0 );
											//$carousel.auto_play($carousel.auto);
											
											}
										
										//$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-2).addClass("act");
					        			
						        		
					        		
									
					        		/*else {
					        			$carousel.avance = true;
					        			for(var j=$carousel.current-1;j<-1;j--){
					        				$("."+$carousel.images_ncarousel).find("li").eq(j).css('left' , $carousel.width_parent );
					        			}
					        			$("."+$carousel.images_ncarousel).find(".act").animate({ left : -$carousel.width_parent }, $carousel.delay, function() {
						        			$carousel.current = cr;
						        			$("."+$carousel.images_ncarousel).find("li").removeClass("act");
						        			$("."+$carousel.images_ncarousel).find("li").css('left' , $carousel.width_parent );
						        			$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).addClass("act");
						        			$carousel.auto_play($carousel.auto);
						        		});
						        		$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).animate({ left : 0 }, $carousel.delay, function() {});
					        		}*/
					        	break;
					        	case "fade" :
					        		$("."+$carousel.images_ncarousel).find("li").css("position" , "absolute");
					        		if( $carousel.start_declenche){
					        			$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).fadeIn($carousel.delay);
					        			$carousel.start_declenche = false;
					        			$carousel.auto_play($carousel.auto);
					        		}
					        		else {
					        			$("."+$carousel.images_ncarousel).find("li").fadeOut($carousel.delay);
					        			$("."+$carousel.images_ncarousel).find("li").eq($carousel.current-1).fadeIn($carousel.delay, function(){
					        				$carousel.auto_play($carousel.auto);
					        			});
					        		}
					        	break;
					        	case "slide_vertical" : 
					        		$("."+$carousel.images_ncarousel).animate({ top : - (($carousel.current-1) * ($carousel.height_parent)) }, $carousel.delay);
					        	break;
					        	default : 
					        		$("."+$carousel.images_ncarousel).animate({ left : - (($carousel.current-1) * $carousel.width_parent) }, $carousel.delay);
					        	break;
				        	}
		         }
		 }
		 // declencheur de l'objet carousel par la function auto_start()
		 $carousel.init();		 
		 return $carousel;
}