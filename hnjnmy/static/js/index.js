$(function(){
    //菜单点击
   
    $(".J_menuItem").on('click',function(){
        var url = $(this).attr('href');
        $("#iframe-main").attr('src',url);
        return false;
    });
});