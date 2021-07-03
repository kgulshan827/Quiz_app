console.log("hello ")
const url=window.location.href
console.log(url)
const timerbox=document.getElementById('timer-box')
const activatetimer= (time) =>{
    console.log(time)
    if(time.toString().length<2)
    {
        timerbox.innerHTML=`<b>0${time}:00</b>`
    }
    else{
        timerbox.innerHTML=`<b>${time}:00</b>`
    }

    let second=60
    let minutes=time-1
    let displayseconds,displayminutes
    const timer= setInterval(() => {
        second--;
        if(second<0)
        {
            second=59
            minutes--;
        }
        if(minutes.toString().length<2)
        {
            displayminutes='0'+minutes
        }
        else{
            displayminutes=minutes
        }

        if(second.toString().length<2)
        {
            displayseconds='0'+second
        }
        else{
            displayseconds=second
        }
        if (minutes === 0 && second === 0) {
            timerbox.innerHTML = "<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert('Time over')
                sendata()
            }, 500)
        }
        timerbox.innerHTML=`<b>${displayminutes}:${displayseconds}<b>`
         console.log("Running")
    },1000);
}
$.ajax({
    type:'GET',
    url:`${url}/data`,
    success: function(response){
       const data=response.data
       const quizbox=document.getElementById('quiz-box')
        data.forEach(el => {
            for(const [questions,answers] of Object.entries(el)){
                console.log(questions)
              quizbox.innerHTML+=`
              <hr>
              <div class="mb-2">
              <b>${questions} </b>
              </div>
              `
             answers.forEach(ans =>{
                 quizbox.innerHTML+=`
                 <div>
                 <input type="radio" class="answer"  name="${questions}" id="${questions}-${ans}" value="${ans}">
                 <label for="${questions}">${ans}</label>
                 </div>
                 `
             })

            }
            
        });
        console.log(response)
    activatetimer(response.time)
    },
    error: function(error){
        console.log(error)
    }
})


const quiz_form=document.getElementById('quiz-form')
const csrf=document.getElementsByName('csrfmiddlewaretoken')
const sendata= () =>{
    const elements=[...document.getElementsByClassName("answer")]
    const data={}
    const url1=window.location.href
   data['csrfmiddlewaretoken']=csrf[0].value
   elements.forEach(el =>{
       if(el.checked)
       {
           data[el.name]=el.value
       }
       else{
           if(!data[el.name])
           {
               data[el.name]=null
           }
       }
   })
   $.ajax({
    type:'POST',
    url:`${url1}/save`,
    data: data,
    success:function(response){
         console.log(response)
         const result=response.score
         console.log(result)
         quiz_form.classList.add('not-visible')
         window.location.href=url+'/'+result+'/result/'
    },
    error: function(error){
    console.log(error)
    }

})
}

quiz_form.addEventListener('submit',e=>{
    e.preventDefault()
    sendata()

})
