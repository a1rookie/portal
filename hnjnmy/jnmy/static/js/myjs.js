	
$(function() {	
$(".lang_div").click(function(){
	$(".drop_down").slideToggle();
});
$(".ph_nav").click(function(){
	$(".mymenu").stop(false,true).slideToggle();
});
	$(".mymenu li>a").click(function(e){
		console.log("1");
		if($(this).siblings(".nav_er").find("a").length > 0 && $(window).width() < 768){
			e.preventDefault();
			$(this).siblings(".nav_er").slideToggle().parents("li").siblings("li").find(".nav_er").slideUp();
			console.log("2");
		}
	});
$(".ph_search").click(function(){
	$(".search_inp").stop(false,true).slideToggle();
});
//搜索条
$(".search_btn").click(function(){
			$(".search_inp").slideToggle();
			})
	
	
    if($(window).width()>1024){
    	$(".contact_xinzeng .inp_div:nth-child(2n)").css("margin-right","0")
    	
   var index_n=$(".zy_toolbar a.active").index();
// alert(index_n)
	$(".zy_toolbar a").hover(function(){	
		$(this).addClass("active").siblings().removeClass("active");
	},function(){		
		$(this).removeClass("active");		
		$(".zy_toolbar  a").eq(index_n).addClass("active");
	})
    };
    
    $(".meeting_box:nth-child(2n)").css("margin-right","0");
    $(".rencai_dl dl:nth-child(2n)").css("margin-right","0");
    $(".strategy_div li:nth-child(3n)").css("margin-right","0");
    $(".Agriculture_ul li:nth-child(3n)").css("margin-right","0");
     $(".resp_ul li:nth-child(3n)").css("margin-right","0");
  
    $(window).scroll(function () {  
    if ($(document).scrollTop() + $(window).height() >= $(document).height()-50) {  
       $(".goto_top").fadeIn() ; 
    } else{
    	 $(".goto_top").fadeOut() ; 
    }
}); 
var bb=$(window).height();
$(".video-box_bg").height(bb);

$(".video_div").click(function(){
	$(".video-box_bg").fadeIn();
	$(".video-box").fadeIn();
	$(".video-box").find("video")[0].play();
})

$(".video-box_bg").click(function(){
	$(".video-box_bg").fadeOut();
	$(".video-box").fadeOut();
	$(".video-box").find("video")[0].pause();
})

function init(){
			$(".disloc").each(function() {
			var self = $(this);
				setTimeout(function(){
					var offsetTop = self.offset().top;
					  if (offsetTop >= $(window).scrollTop() && offsetTop < ($(window).scrollTop()+$(window).height()+40)) {
							var lisx = offsetTop-$(window).height();
							if($(window).scrollTop()>lisx){
							  self.addClass("p_add");
							}
						}
				},300);
			});
		}
		$(window).scroll(function(){
		 init()
		}).scroll();
		
		$(".top").animate({top:"0px"},1200,'easeOutBounce');
		$(".index_news_right").animate({right:"0px"},1200,'easeOutBounce');
		$(".index_news_left").animate({left:"0px"},1200,'easeOutBounce');
			})
		