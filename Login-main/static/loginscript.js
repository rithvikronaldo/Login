const  signinBtn=document.querySelector('.siginBtn');
         const signupBtn=document.querySelector('.signupBtn');
         const formBX = document.querySelector('.formBX');
         const body = document.querySelector('body');

        signupBtn.onclick = function(){
            formBX.classList.add('active')
            body.classList.add('active')
        }

        signinBtn.onclick = function(){
            formBX.classList.remove('active')
            body.classList.remove('active')
        }