function productDetail(product_id) {
    $.ajax({
        type: 'GET',
        url: '/detail/',
        dataType: 'json',
        data: {'product_id':product_id},
        success: function (data) {
            var images = '';
            //console.log(data[4][0]);
            if(data[4].length>1)
            {
                for(var i=1;i<data[4].length;i++)
                {
                       //console.log(data[4][i]);
                       images='<img src="'+data[4][i]+'" />';
                }
            }
            //console.log(images);
            var html = '<div class="modal-dialog" style="width:80%">' +
                       '<div class="modal-content">' +
                       '<div class="modal-header">' +
                            '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>' +
                        '</div>' +
                        '<div class="modal-body row">' +
                            <!--图片展示 START-->
                            '<div class="pic_show col-md-6 col-sm-6">' +
                                '<div class="wai">' +
                                    '<div class="one">' +
                                    '<img src="'+data[4][0]+'" />' +
                                    '<span></span>' +
                                '</div>' +
                                '<div class="two">' +
                                    '<img class="active" src="'+data[4][0]+'" />' +
                                    images+
                                '</div>' +
                                '</div>' +
                                '<div class="the">' +
                                    '<img src="'+data[4][0]+'" />' +
                                '</div>' +
                            '</div>' +
                            <!--图片展示 END-->
                            <!--商品详情 START-->
                            '<div class="detail col-md-6 col-sm-6">' +
                                '<p class="name">'+data[0]+'</p>' +
                                '<p class="goodsdate">发布时间： '+data[1]+'&nbsp;&nbsp;浏览量： '+data[2]+'</p>' +
                                data[3] +
                            '</div>' +
                            <!--商品详情 END-->
                        '</div>' +
                    '</div><!-- /.modal-content -->' +
                '</div><!-- /.modal -->';

            $("#myModal").html(html);

            var ione = $(".one"),
		ithe = $(".the"),
		itwo = $(".two img"),
		tthe = $(".the img");

	var arr = data[4];
	var oarr = data[4];
	itwo.each(function(i){
		$(this).click(function(){
			$(".one img").attr("src",arr[i])
			tthe.attr("src",oarr[i])
			itwo.removeClass("active")
			$(this).addClass("active")
		})

		ione.mousemove(function(a){
			var evt = a || window.event
			ithe.css('display','block')
			var ot = evt.clientY-($(".one").offset().top- $(document).scrollTop())-87;
			var ol = evt.clientX-($(".one").offset().left- $(document).scrollLeft())-87;
			if(ol<=0){
				ol = 0;
			}
			if(ot<=0){
				ot = 0;
			}
			if(ol>=175){
				ol=175
			}
			if(ot>=175){
				ot=175
			}
			$("span").css({'left':ol,'top':ot})
			var ott = ot/350*800
			var oll = ol/350*800
			tthe.css({'left':-oll,'top':-ott})
		})
		ione.mouseout(function(){
			ithe.css('display','none')
		})

	})
        }
    });

}