const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function(event) {

        const selectedSkills =
            document.querySelectorAll(
                'input[name="skills"]:checked'
            );

        if (selectedSkills.length === 0) {

            event.preventDefault();

            alert(
                "⚠️ Please select at least one skill!"
            );

        }

    });

}