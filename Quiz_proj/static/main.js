console.log("hello")
const modlbttns=[...document.getElementsByClassName("modal-button")]
modalbody=document.getElementById('quiz-start-confirm')
const start=document.getElementById('start-button')
const url=window.location.href
modlbttns.forEach(modlbttn=>modlbttn.addEventListener('click',()=>{
    const pk=modlbttn.getAttribute('data-pk')
    const name=modlbttn.getAttribute('data-name')
    const topic=modlbttn.getAttribute('data-topic')
    const number=modlbttn.getAttribute('data-number')
    const score=modlbttn.getAttribute('data-score')
    const time=modlbttn.getAttribute('data-time')
    const difficulty=modlbttn.getAttribute('data-difficulty')
        
    modalbody.innerHTML=`
    <div class="h5 mb-3">Are you sure you want to start  <b>${name}</b>?</div>
    <div class="text-muted">
    <ul>
    <li>Topic: <b>${topic} </b></li>
    <li>Time: <b>${time}</b> min</li>
    <li>Difficulty: <b>${difficulty} </b></li>
    <li>Passing  score: <b>${score}</b></li>

    </ul> 
    `

start.addEventListener('click', ()=>{
    window.location.href=url+pk
})
}))