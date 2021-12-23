var NavigationMenu = function(options) {
	 settings = {parent : "", type : "colors" };
	 jQuery.extend(settings, options);
	 var parent = settings.parent;
	 var type = settings.type;
	 var $menu = {
		hover : "",
		this_ : "",
		nombre_lien:"",
		init_var : "",
		init_offest : 0,
		init : function() {
		 $menu.nombre_lien = $(parent).find("ul > li").length;
		     $menu.hover = false;
		     $menu.init_var = true;
		     $menu.switcher();
			 $(parent).find("ul > li").hover(function() {
				 $menu.hover = true;
				 $menu.this_ = $(this);
				 $menu.switcher();
				},
				function() {
					$menu.hover = false;
					$menu.switcher();
					
			 });	 
		 },
		 switcher : function() {
			 switch (type) {
				 case "tracker" :
					 if($menu.init_var){
						 var back = "<span class='bg_move'></span>";
				         $(parent).append(back);
				         $menu.init_var = false;
					 }
					 $menu.track_type();
				 break;
				 case "colors" : 
					 if($menu.init_var){
						 var back = "<span class='bg_move'></span>";
				         $(parent).append(back);
				         $menu.init_var = false;
					 }
					 $menu.colors_type();
				 break;
				 case "vertical" :
					 if($menu.init_var){
						 for(var i=0;i<$menu.nombre_lien;i++){
				    		 var this_href = $(parent).find("li").eq(i).find("a").attr("href");
							 var this_text = $(parent).find("li").eq(i).find("a").text();
							 var clone_a = "<a href="+this_href+">"+this_text+"</a>";
							 $(parent).find("li").eq(i).append(clone_a);
							 $(parent).find("li").eq(i).find("a").eq(1).css("background" , "#db060c");
				    	 }
				         $menu.init_var = false;
					 }
					  $menu.vertical_type();
				 break;
				 case "background" : 
					  $menu.background_type();
				 break;
				 case "horizontal" : 
					  $menu.horizontal_type();
				 break;
				 case "background_horizontal" : 
					  $menu.backgroundHorizontal_type();
				 break;
				 default : 
					 $menu.track_type();
				 break;
			 }
		 },
		track_type : function() {
			
			var espace = 0;
			 if($menu.hover){
				 $(parent).find(".active").removeClass("activeS");
				 var offset = $($menu.this_).position();
				 if(offset.left != 0) {
				 	espace = 23;
				 }
				 var width_ = $($menu.this_).width();
				 if( $($menu.this_).hasClass("last") ) {
					 if(navigator.appName == 'Microsoft Internet Explorer') {
					 	//$(parent).find(".bg_move").stop().animate({ "left" : offset.left , "width" : width_ });
					 }
					 else {
					 	$(parent).find(".bg_move").stop().css({ "left" : offset.left+espace , "width" : width_ });
					 } 
				 }
				 else {
				 	if (navigator.appName == 'Microsoft Internet Explorer') {
						//$(parent).find(".bg_move").stop().animate({ "left" : offset.left , "width" : width_+20, "color" : "#425ea9"  });
					}
					else {
						$(parent).find(".bg_move").stop().css({ "left" : offset.left+espace , "width" : width_+20, "color" : "#425ea9"  });
					}
				 }	 
			 }
			 else {
				 if($(parent).find(".active").width() > 0) {
					 $(parent).find(".active").addClass("activeS");
					 var pos_active = $(parent).find(".active").position();
					  if(pos_active.left != 0) {
				 		espace = 23;
				 	}
					 var width_active = $(parent).find(".active").width();
					 var left_distance = pos_active.left;
					 if(left_distance == 0){
						 left_distance = $menu.init_offest;
					 }
					 if( $(parent).find(".active").hasClass("last") ) {
					 	if (navigator.appName == 'Microsoft Internet Explorer') { 
							//$(parent).find(".bg_move").stop().animate({ "left" : left_distance, "width" : width_active });
						}
						else {
							$(parent).find(".bg_move").stop().css({ "left" : left_distance+espace, "width" : width_active });
						}
					 }
					 else {
						 $(parent).find(".bg_move").stop().animate({ "left" : left_distance+espace, "width" : width_active+20 });
					 }
				 }
			 }
		 },
		colors_type : function() {
			if($menu.hover){
				var array_colors = ["#80cbd9","#ece380","#ea228f","#db060c","#3998e6","#f4ae2b","#f77b28","#b621e7"];
				var random = Math.round(Math.random()*8);
				var color_result = array_colors[random];
				 var offset = $($menu.this_).offset();
				 $(parent).find(".bg_move").stop().animate({ left : offset.left },"slow");
				 $(parent).find(".bg_move").css("background" , color_result);
			 }
			 else{
				 var pos_active = $(parent).find(".active").offset();
				 var left_distance = pos_active.left;
				 if(left_distance == 0){
					 left_distance = $menu.init_offest;
				 }
				 $(parent).find(".bg_move").stop().animate({ left : left_distance },"slow");
			 } 
		 },
		vertical_type : function() {
				if($menu.hover){
					$($menu.this_).find("a").eq(0).animate({ top : -32 }, "slow");
					$($menu.this_).find("a").eq(1).animate({ top : -32 }, "slow");
				 }
				 else{
					 $($menu.this_).find("a").eq(0).animate({ top : 0 }, "slow");
					 $($menu.this_).find("a").eq(1).animate({ top : 0 }, "slow");
				 } 
	   },
	   background_type : function() {
			if($menu.hover){
				$($menu.this_).stop().animate({ backgroundPosition : "0px 0px"}, 500);
			 }
			 else{
				 $($menu.this_).stop().animate({ backgroundPosition : "0 -65px" },500);
			 } 
      },
      backgroundHorizontal_type : function() {
			if($menu.hover){
				$($menu.this_).stop().animate({ backgroundPosition : "-88px 0px"}, 500);
			 }
			 else{
				 $($menu.this_).stop().animate({ backgroundPosition : "60 0px" },500);
			 } 
    },
      horizontal_type : function() {
			if($menu.hover){
				$($menu.this_).stop().animate({ width: 350,paddingLeft : 50}, 300);
			 }
			 else{
				 $($menu.this_).stop().animate({ width : 290,paddingLeft : 10 }, 300);
			 } 
      },
  } 
	 $menu.init();
	 return $menu;
}