var inputs = document.querySelectorAll('input');
inputs.forEach(input =>{
    input.onfocus = ()=>{
        input.nextElementSibling.classList.add('fix');
    }
    input.onblur = ()=>{
        if(input.value.trim().length == 0)
        input.nextElementSibling.classList.remove('fix');
    }

});