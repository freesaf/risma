 // cette function qui est responsable sur la partie de gestion les evenement des touches de clavier  
		         gestion_clavier : function() {
		        	 $(window).keydown(function(event){
		        		//console.log(event.keyCode);
		 				switch (event.keyCode) {
			 				case 39: 
			 					if($carousel.current < $carousel.nombre_images){
			 						$carousel.click_next();
			 					}
			 				break;
			 				case 37 : 
			 					if($carousel.current > 1){
                                  	$carousel.click_prev();
			 					}
				 			break;
			 				case 80 : 
			 					if(!$carousel.etat_img_clic){
			 						if($carousel.play_parent!=""){
			 							$carousel.playing_click($carousel.play_parent);
			 						}
			 						else {
			 							$carousel.playing_click($carousel.parent);
			 						}
			 					}
				 			break;
			 				case 79 : 
			 					if($carousel.play_parent!=""){
		 							$carousel.pausing_click($carousel.play_parent);
		 						}
		 						else {
		 							$carousel.pausing_click($carousel.parent);
		 						}
				 			break;
			 				case 83 : 
			 					if($carousel.play_parent!=""){
		 							$carousel.pausing_click($carousel.play_parent);
		 						}
		 						else {
		 							$carousel.pausing_click($carousel.parent);
		 						}
				 			break;
			 				case 27 : 
			 					$("#overlay").hide();
			 					$("#conteneur_modal").hide();
			 					$carousel.pausing_click();
			 					$carousel.etat_img_clic = false;
			 				break;
			 				case 32 :
			 					 if($carousel.etat_img_clic){
			 						$carousel.etat_img_clic = false;
			 						$carousel.on_close = true;
			 						$carousel.onClose("");
			 						return false;
			 					}
			 					 else {
			 						 return false;
			 					 }
			 				break;
			 				case 38 : 
			 					if($carousel.current < $carousel.nombre_images){
			 						$carousel.click_next();
			 					}
			 				break;
			 				case 40 : 
			 					if($carousel.current > 1){
                                  	$carousel.click_prev();
			 					}
			 				break;
			 				default : 
			 					
				 			break;
		 				}
		 			});
		         },
		         adaptation : function() {
						var widthWindow = $("#conteneur_modal").width();
						var heightWindow = $("#conteneur_modal").height();
						var pi;
						var width_img = $("#modal").find("img").width();
						var height_img = $("#modal").find("img").height();
						if(width_img>widthWindow*$carousel.pourcentage_redimensionement || height_img>heightWindow*$carousel.pourcentage_redimensionement ) {
							
						     ratioWindow = widthWindow/heightWindow; 
						     ratioImage = width_img/height_img;
							 if(ratioWindow>=ratioImage) {
								pi = heightWindow/height_img;
							 }
							 if(ratioWindow<=ratioImage) {
								pi =widthWindow/width_img;
							 }
				             resultatW = $carousel.pourcentage_redimensionement*pi*width_img;
				             resultatH = $carousel.pourcentage_redimensionement*pi*height_img;
							 $("#modal").animate({opacity : 1, width :resultatW , height : resultatH+20}, 500);
							 $("#modal").find("img").animate({ opacity : 1, width :resultatW , height : resultatH }, 500);
						     $("#modal").css("top" , (heightWindow-(height_img+55+20))/2);
					      }
					      else {
					           $("#modal").animate({ width : width_img , height : height_img+20 }, 500);
					           $("#modal").find("img").animate({ opacity : 1 }, 500);
					      }
			 },
			// cette function fait le calcul pour adapter les images non compatible au niveau de taille par la taille de conteneur de carousel adaptable
	         adaptataion_images : function() {
	        	 var images_li = $($carousel.parent).find("."+$carousel.images_ncarousel).find("li");
	        	 var li_img_width;
	        	 var li_img_height; 
	        	 for(var n_img = 0; n_img<$carousel.nombre_images;n_img++ ){
	        		 li_img_width = $(images_li).eq(n_img).find("img").width();
	        		 li_img_height = $(images_li).eq(n_img).find("img").height();
	        		 if(li_img_height>li_img_width){
	        			 $carousel.portrait = true;
	        		 }
	        		 else {
	        			$carousel.portrait = false; 
	        		 }
	        		 if($carousel.portrait){
	        			  if(li_img_height>$carousel.$carousel.height_parent){
	        				 // $(images_li).eq(n_img).find('img').width(width_parent);
	        				  if(li_img_height>li_img_width){
	        					  $(images_li).eq(n_img).find('img').height($carousel.height_parent);
	        				  }
	        				  else {
	        					  $(images_li).eq(n_img).find('img').width($carousel.width_parent);
	        				  }  
	        			  }
	        		 }
	        		 else {
	        			 if(li_img_width>$carousel.width_parent){
	        				 if(li_img_width>$carousel.width_parent){
	        					 $(images_li).eq(n_img).find('img').width($carousel.width_parent);
	        				 }
	        				 if(li_img_height>$carousel.height_parent) {
	        					 if(li_img_width>li_img_height ){
                                      $(images_li).eq(n_img).find('img').width("");
			        				  $(images_li).eq(n_img).find('img').height($carousel.height_parent);
			        			  }
		        				 else {
		        					 $(images_li).eq(n_img).find('img').width($carousel.width_parent);
		        				 }
	        				 }
	        			 }
	        		 }
	        	 }
	         },
	        	/* if($carousel.current>1){
    		 
        	 }
        	 else {
        		 $carousel.current_function();
        		 if($carousel.type_navigation == "cercle"){
		        		$("."+$carousel.nav_ncarousel).find("ul").find("li").eq(0).addClass("cercle_active");
		        		$(".cercle_active").html("<img src="+$carousel.repertoire_media+"images/cercle_active.png alt='cercle' />");
		        	}
        	 }*/ 