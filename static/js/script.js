// SIDEBAR

const allSideMenu = document.querySelectorAll('#sidebar .side-menu li a');

allSideMenu.forEach(item => {
    const li = item.parentElement;

    item.addEventListener('click', function(){
        allSideMenu.forEach(i => {
            i.parentElement.classList.remove('active')
        })

        li.classList.add('active');
    })
});

// END OF SIDEBAR


// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu')
const sidebar = document.getElementById('sidebar')

menuBar.addEventListener('click', function(){
    sidebar.classList.toggle('hide')
})
// END OF TOGGLE SIDEBAR



const searchButton = document.querySelector('#content nav form .form-input button')
const CloseSearchButton = document.querySelector('#content nav form .form-input button .bx')
const searchForm = document.querySelector('#content nav form')

// searchButton.addEventListener('click', function(e){
//     if(window.innerWidth < 576)
//         e.preventDefault()
//         searchForm.classList.toggle('show')
// })


if(window.innerWidth < 768) {
    sidebar.classList.add('hide')
} else if(window.innerWidth > 576) {
    CloseSearchButton.classList.replace('bx-x', 'bx-search')
    searchForm.classList.remove('show')
}


window.addEventListener('resize', function(){
    if(this.innerWidth > 576){
        CloseSearchButton.classList.replace('bx-x', 'bx-search')
        searchForm.classList.remove('show')
    }
})