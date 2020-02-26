jQuery('document').ready(function(){

    /* обработка нажатий кнопок 
	jQuery('#alert1').on('click',function(){
        $.post('/print');
	});*/

	jQuery('#btn1').on('click',function(){
        $.post('/price')
	});
	
	jQuery('#tab1').on('mouseover','td',function(){
		jQuery(this).addClass('cl_tab2');
	});
	
	jQuery('#tab1').on('mouseout','td',function(){
		jQuery(this).removeClass('cl_tab2');
	});



var tt = true;
function func() {

    if(tt==true)
    {
        jQuery('#rez1').addClass('cl_tab2');
        tt = false;
    }
    else
    {
        jQuery('#rez1').removeClass('cl_tab2');
        tt = true;
    }
    
}

});
