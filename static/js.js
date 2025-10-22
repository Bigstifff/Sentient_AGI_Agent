document.addEventListener("DOMContentLoaded", () => {
    if (document.body.id === "layout") {
        
    }
    
    // js for the home page
    else if (document.body.id === "home") {
        let suggest = document.querySelectorAll(".suggest div");
        let input = document.querySelector("#querry input");
        let submit = document.querySelector("#querry button");
        let roboText = document.querySelector(".roboText .textArea")
        let form = document.querySelector("#querry");

        for (let i = 0; i < suggest.length; i++) {
            suggest[i].addEventListener("click", (e) => {
                let x = e.target;

                input.value = x.textContent;
            })
        }

        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            let newForm = new FormData(form);
            let queryText = newForm.get("q");

            let payload = {
                query: queryText
            };

            try {
                let response = await fetch("http://127.0.0.1:8080/assist", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(payload)
                });
                let data = await response.json()

                console.log(JSON.stringify(data))
            }
            catch (error) {
                console.log(error)
            }
        })
    }
})