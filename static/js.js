document.addEventListener("DOMContentLoaded", () => {
    if (document.body.id === "layout") {
        
    }
    
    // js for the home page
    else if (document.body.id === "home") {
        let suggest = document.querySelectorAll(".suggest div");
        let input = document.querySelector("#querry input");
        let submit = document.querySelector("#querry button");

        submit.disabled = true;

        for (let i = 0; i < suggest.length; i++) {
            suggest[i].addEventListener("click", (e) => {
                let x = e.target;

                input.value = x.textContent;
            })
        }
    }
})