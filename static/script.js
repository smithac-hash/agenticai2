const form = document.getElementById("careerForm");

const results =
    document.getElementById("results");

const loading =
    document.getElementById("loading");


// ============================================================
// ESCAPE HTML
// ============================================================

function escapeHTML(value) {

    return String(value).replace(

        /[&<>"']/g,

        function (character) {

            const characters = {

                "&": "&amp;",

                "<": "&lt;",

                ">": "&gt;",

                '"': "&quot;",

                "'": "&#039;"

            };

            return characters[character];

        }

    );

}


// ============================================================
// DISPLAY CHIPS
// ============================================================

function displayChips(
    elementId,
    items,
    isGap = false
) {

    const element =
        document.getElementById(elementId);

    if (!items || items.length === 0) {

        element.innerHTML = `
            <span class="chip">
                No major items identified
            </span>
        `;

        return;

    }


    element.innerHTML = items.map(

        function (item) {

            return `

                <span class="chip ${isGap ? "gap" : ""}">

                    ${escapeHTML(item)}

                </span>

            `;

        }

    ).join("");

}


// ============================================================
// FORM SUBMISSION
// ============================================================

form.addEventListener(
    "submit",

    async function (event) {

        event.preventDefault();


        const button =
            document.getElementById("analyzeBtn");


        const payload = {

            name:
                document.getElementById("name").value,

            education:
                document.getElementById("education").value,

            skills:
                document.getElementById("skills").value,

            interests:
                document.getElementById("interests").value,

            goal:
                document.getElementById("goal").value,

            experience:
                document.getElementById("experience").value,

            projects:
                document.getElementById("projects").value,

            plan_days:
                document.getElementById("planDays").value

        };


        button.disabled = true;

        button.textContent =
            "🧠 Creating Your Career Plan...";


        loading.classList.remove(
            "hidden"
        );


        try {


            const response =
                await fetch(

                    "/api/analyze",

                    {

                        method: "POST",

                        headers: {

                            "Content-Type":
                                "application/json"

                        },

                        body:
                            JSON.stringify(payload)

                    }

                );


            const result =
                await response.json();


            if (!result.success) {

                throw new Error(
                    result.message
                );

            }


            renderReport(
                result.data
            );


            results.classList.remove(
                "hidden"
            );


            results.scrollIntoView({

                behavior: "smooth"

            });


        }

        catch (error) {

            alert(

                "Error: " +
                error.message

            );

        }

        finally {


            loading.classList.add(
                "hidden"
            );


            button.disabled = false;


            button.textContent =
                "✨ Generate My Personalized Career Plan";

        }

    }

);


// ============================================================
// RENDER REPORT
// ============================================================

function renderReport(data) {


    const profile =
        data.master_profile;


    // --------------------------------------------------------
    // TITLE
    // --------------------------------------------------------

    document.getElementById(
        "reportTitle"
    ).textContent =

        profile.student +
        "'s Career Development Report";


    // --------------------------------------------------------
    // SCORE CARDS
    // --------------------------------------------------------

    document.getElementById(
        "targetRole"
    ).textContent =

        profile.target_role;


    document.getElementById(
        "matchScore"
    ).textContent =

        profile.career_match_score +
        "%";


    document.getElementById(
        "completion"
    ).textContent =

        data.skill_gap.completion_percent +
        "%";


    // --------------------------------------------------------
    // PROFESSIONAL SUMMARY
    // --------------------------------------------------------

    document.getElementById(
        "summary"
    ).textContent =

        data.professional_summary;


    // --------------------------------------------------------
    // STRENGTHS
    // --------------------------------------------------------

    displayChips(

        "strengths",

        profile.strengths

    );


    // --------------------------------------------------------
    // SKILL GAPS
    // --------------------------------------------------------

    displayChips(

        "gaps",

        profile.skill_gaps,

        true

    );


    // --------------------------------------------------------
    // CAREER SCORES
    // --------------------------------------------------------

    const scoresContainer =
        document.getElementById(
            "scores"
        );


    scoresContainer.innerHTML =
        data.career_scores.map(

            function (score) {

                return `

                    <div class="bar-row">

                        <span>

                            ${escapeHTML(score.role)}

                        </span>


                        <div class="bar">

                            <div

                                class="fill"

                                style="
                                    width:
                                    ${score.score}%
                                "

                            ></div>

                        </div>


                        <strong>

                            ${score.score}%

                        </strong>

                    </div>

                `;

            }

        ).join("");


    // --------------------------------------------------------
    // ROADMAP INTRODUCTION
    // --------------------------------------------------------

    document.getElementById(
        "roadmapIntro"
    ).textContent =

        `Your personalized ${profile.plan_days}-day learning plan was generated based on your current skills, missing skills and target role: ${profile.target_role}.`;


    // --------------------------------------------------------
    // ROADMAP
    // --------------------------------------------------------

    const roadmap =
        document.getElementById(
            "roadmap"
        );


    roadmap.innerHTML =
        data.learning_roadmap.map(

            function (item) {

                return `

                    <div class="roadmap-item">

                        <div class="step">

                            ${item.day}

                        </div>


                        <div>

                            <span class="phase">

                                ${escapeHTML(
                                    item.phase
                                )}

                            </span>


                            <h4>

                                ${escapeHTML(
                                    item.skill
                                )}

                            </h4>


                            <p>

                                ${escapeHTML(
                                    item.task
                                )}

                            </p>

                        </div>

                    </div>

                `;

            }

        ).join("");


    // --------------------------------------------------------
    // PROJECTS
    // --------------------------------------------------------

    document.getElementById(
        "projectsList"
    ).innerHTML =

        data.recommended_projects.map(

            function (project) {

                return `

                    <li>

                        ${escapeHTML(project)}

                    </li>

                `;

            }

        ).join("");


    // --------------------------------------------------------
    // INTERVIEW QUESTIONS
    // --------------------------------------------------------

    const interview =
        data.interview_preparation;


    document.getElementById(
        "interview"
    ).innerHTML = `


        <div class="question-group">

            <h4>
                Common Questions
            </h4>

            <ul>

                ${interview.common.map(

                    question =>

                        `<li>
                            ${escapeHTML(question)}
                        </li>`

                ).join("")}

            </ul>

        </div>


        <div class="question-group">

            <h4>
                Technical Questions
            </h4>

            <ul>

                ${interview.technical.map(

                    question =>

                        `<li>
                            ${escapeHTML(question)}
                        </li>`

                ).join("")}

            </ul>

        </div>


        <div class="question-group">

            <h4>
                Personalized Questions
            </h4>

            <ul>

                ${interview.personalized.map(

                    question =>

                        `<li>
                            ${escapeHTML(question)}
                        </li>`

                ).join("")}

            </ul>

        </div>

    `;


    // --------------------------------------------------------
    // CONSISTENCY NOTE
    // --------------------------------------------------------

    document.getElementById(
        "consistency"
    ).textContent =

        data.consistency_note;

}