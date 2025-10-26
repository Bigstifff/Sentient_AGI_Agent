document.addEventListener("DOMContentLoaded", () => {
    if (document.body.id === "layout") {
        
    }
    
    // js for the home page
    else if (document.body.id === "home") {
        let suggest = document.querySelectorAll(".suggest div");
        let input = document.querySelector("#querry input");
        let submit = document.querySelector("#querry button");
        let form = document.querySelector("#querry");
        let chatArea = document.querySelector(".chatArea");

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
            console.log(queryText)
            input.value = "";

            let payload = {
                query: queryText
            };

            try {
                let response = await fetch("/testing?q=" + queryText);
                let data = await response.json();
                console.log(data.msg);

                let userArea = document.createElement("div");
                userArea.classList.add("userArea");
                let userText = document.createElement("div");
                userText.classList.add("userText");
                userText.textContent = queryText;
                let roboText = document.createElement("div");
                roboText.classList.add("roboText")
                let gif = document.createElement("img");
                gif.classList.add("gif");
                gif.style.display = "block";
                gif.src = "static/gif/loader.gif"
                roboText.appendChild(gif);

                userArea.appendChild(userText);
                chatArea.appendChild(userArea);
                chatArea.appendChild(roboText);

                setTimeout(() => {
                    gif.style.display = "none";
                    let img = document.createElement("img");
                    img.src = "static/images/robo_pfp_w.png";
                    roboText.appendChild(img);
                    let textArea = document.createElement("div");
                    textArea.classList.add("textArea");
                    textArea.textContent = data.msg;
                    roboText.appendChild(textArea);
                }, 2000);


            }
            catch (error) {
                console.log(error)
            }
        })
    }
})