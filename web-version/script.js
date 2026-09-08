// ============================================
// STUDYFLOW STUDENT TO-DO APP
// ============================================

let tasks = JSON.parse(
    localStorage.getItem("studyflow_tasks")
) || [];


// ============================================
// DOM ELEMENTS
// ============================================

const modal = document.getElementById("taskModal");

const taskForm = document.getElementById("taskForm");

const taskTitle = document.getElementById("taskTitle");

const taskSubject = document.getElementById("taskSubject");

const taskPriority = document.getElementById("taskPriority");

const taskDate = document.getElementById("taskDate");

const taskTime = document.getElementById("taskTime");

const taskNotes = document.getElementById("taskNotes");


// ============================================
// NAVIGATION
// ============================================

document.querySelectorAll(".nav-item").forEach(button => {

    button.addEventListener("click", () => {

        const page = button.dataset.page;

        showPage(page);

    });

});


document.querySelectorAll(".text-button").forEach(button => {

    button.addEventListener("click", () => {

        showPage(button.dataset.page);

    });

});


function showPage(pageName) {

    document.querySelectorAll(".page").forEach(page => {

        page.classList.remove("active");

    });


    document.querySelectorAll(".nav-item").forEach(button => {

        button.classList.remove("active");

    });


    const page = document.getElementById(pageName);

    if (page) {

        page.classList.add("active");

    }


    const navButton =
        document.querySelector(
            `.nav-item[data-page="${pageName}"]`
        );

    if (navButton) {

        navButton.classList.add("active");

    }


    if (pageName === "calendar") {

        renderCalendar();

    }

}


// ============================================
// MODAL
// ============================================

document
    .getElementById("openTaskModal")
    .addEventListener("click", openModal);


document
    .getElementById("openTaskModal2")
    .addEventListener("click", openModal);


document
    .getElementById("closeModal")
    .addEventListener("click", closeModal);


document
    .getElementById("cancelTask")
    .addEventListener("click", closeModal);


function openModal() {

    modal.classList.add("show");

    taskDate.value =
        new Date().toISOString().split("T")[0];

    taskTitle.focus();

}


function closeModal() {

    modal.classList.remove("show");

    taskForm.reset();

}


modal.addEventListener("click", event => {

    if (event.target === modal) {

        closeModal();

    }

});


// ============================================
// ADD TASK
// ============================================

taskForm.addEventListener("submit", event => {

    event.preventDefault();


    const task = {

        id: Date.now(),

        title: taskTitle.value.trim(),

        subject: taskSubject.value,

        priority: taskPriority.value,

        date: taskDate.value,

        time: taskTime.value,

        notes: taskNotes.value.trim(),

        completed: false,

        createdAt: new Date().toISOString()

    };


    tasks.push(task);

    saveTasks();

    closeModal();

    renderAll();

});


// ============================================
// LOCAL STORAGE
// ============================================

function saveTasks() {

    localStorage.setItem(
        "studyflow_tasks",
        JSON.stringify(tasks)
    );

}


// ============================================
// TOGGLE TASK
// ============================================

function toggleTask(id) {

    const task = tasks.find(
        task => task.id === id
    );

    if (!task) return;

    task.completed = !task.completed;

    saveTasks();

    renderAll();

}


// ============================================
// DELETE TASK
// ============================================

function deleteTask(id) {

    tasks = tasks.filter(
        task => task.id !== id
    );

    saveTasks();

    renderAll();

}


// ============================================
// FORMAT DATE
// ============================================

function formatDate(dateString) {

    if (!dateString) return "";

    const date = new Date(dateString + "T00:00:00");

    return date.toLocaleDateString(
        "en-US",
        {
            month: "short",
            day: "numeric"
        }
    );

}


// ============================================
// TASK CARD
// ============================================

function createTaskCard(task) {

    const card = document.createElement("div");

    card.className = "task-card";


    card.innerHTML = `

        <div class="task-top">

            <div
                class="task-check ${task.completed ? "completed" : ""}"
                onclick="toggleTask(${task.id})"
            >
                ${task.completed ? "✓" : ""}
            </div>

        </div>


        <h4 class="${task.completed ? "completed-title" : ""}">
            ${escapeHTML(task.title)}
        </h4>


        <p>
            ${escapeHTML(task.notes || "No additional notes.")}
        </p>


        <div class="task-meta">

            <span class="tag">
                ${escapeHTML(task.subject)}
            </span>

            <span class="tag priority-${task.priority}">
                ${capitalize(task.priority)}
            </span>

            <span class="tag">
                ${formatDate(task.date)}
            </span>

        </div>

    `;


    return card;

}


// ============================================
// LIST TASK
// ============================================

function createListTask(task) {

    const item = document.createElement("div");

    item.className = "list-task";


    item.innerHTML = `

        <div
            class="task-check ${task.completed ? "completed" : ""}"
            onclick="toggleTask(${task.id})"
        >
            ${task.completed ? "✓" : ""}
        </div>


        <div class="list-task-content">

            <div class="
                list-task-title
                ${task.completed ? "completed-title" : ""}
            ">

                ${escapeHTML(task.title)}

            </div>


            <div class="list-task-info">

                <span class="tag">
                    ${escapeHTML(task.subject)}
                </span>

                <span class="tag priority-${task.priority}">
                    ${capitalize(task.priority)}
                </span>

                <span class="tag">
                    ${formatDate(task.date)}
                </span>

                ${
                    task.time
                    ? `<span class="tag">${task.time}</span>`
                    : ""
                }

            </div>

        </div>


        <button
            class="delete-task"
            onclick="deleteTask(${task.id})"
        >
            ×
        </button>

    `;


    return item;

}


// ============================================
// DASHBOARD
// ============================================

function renderDashboard() {

    const today =
        new Date().toISOString().split("T")[0];


    const todayTasks =
        tasks.filter(task =>
            task.date === today
        );


    const completed =
        todayTasks.filter(task =>
            task.completed
        );


    const highPriority =
        tasks.filter(task =>
            task.priority === "high" &&
            !task.completed
        );


    const percentage =
        todayTasks.length === 0
            ? 0
            : Math.round(
                completed.length /
                todayTasks.length *
                100
            );


    document.getElementById(
        "todayCount"
    ).textContent = todayTasks.length;


    document.getElementById(
        "progressCount"
    ).textContent =
        tasks.filter(task => !task.completed).length;


    document.getElementById(
        "completedCount"
    ).textContent =
        tasks.filter(task => task.completed).length;


    document.getElementById(
        "priorityCount"
    ).textContent =
        highPriority.length;


    document.getElementById(
        "progressPercentage"
    ).textContent =
        `${percentage}%`;


    document.getElementById(
        "progressFill"
    ).style.width =
        `${percentage}%`;


    const container =
        document.getElementById("todayTasks");


    container.innerHTML = "";


    if (todayTasks.length === 0) {

        showEmptyState(
            container,
            "You're all caught up",
            "No tasks scheduled for today."
        );

        return;

    }


    todayTasks.forEach(task => {

        container.appendChild(
            createTaskCard(task)
        );

    });

}


// ============================================
// ALL TASKS
// ============================================

function renderAllTasks() {

    const container =
        document.getElementById("allTasks");


    const search =
        document
            .getElementById("searchInput")
            .value
            .toLowerCase();


    const filter =
        document
            .getElementById("filterSelect")
            .value;


    let filtered =
        tasks.filter(task =>
            task.title
                .toLowerCase()
                .includes(search)
        );


    if (filter === "active") {

        filtered =
            filtered.filter(
                task => !task.completed
            );

    }


    if (filter === "completed") {

        filtered =
            filtered.filter(
                task => task.completed
            );

    }


    if (filter === "high") {

        filtered =
            filtered.filter(
                task => task.priority === "high"
            );

    }


    container.innerHTML = "";


    if (filtered.length === 0) {

        showEmptyState(
            container,
            "No tasks found",
            "Try adding a new task or changing your filter."
        );

        return;

    }


    filtered
        .sort((a, b) =>
            a.date.localeCompare(b.date)
        )
        .forEach(task => {

            container.appendChild(
                createListTask(task)
            );

        });

}


// ============================================
// COMPLETED TASKS
// ============================================

function renderCompleted() {

    const container =
        document.getElementById(
            "completedTasks"
        );


    const completed =
        tasks.filter(
            task => task.completed
        );


    container.innerHTML = "";


    if (completed.length === 0) {

        showEmptyState(
            container,
            "Nothing completed yet",
            "Finished tasks will appear here."
        );

        return;

    }


    completed.forEach(task => {

        container.appendChild(
            createListTask(task)
        );

    });

}


// ============================================
// EMPTY STATE
// ============================================

function showEmptyState(
    container,
    title,
    description
) {

    container.innerHTML = `

        <div class="empty-state">

            <strong>${title}</strong>

            <span>${description}</span>

        </div>

    `;

}


// ============================================
// CALENDAR
// ============================================

let calendarDate = new Date();


function renderCalendar() {

    const year =
        calendarDate.getFullYear();

    const month =
        calendarDate.getMonth();


    const monthName =
        calendarDate.toLocaleDateString(
            "en-US",
            {
                month: "long",
                year: "numeric"
            }
        );


    document.getElementById(
        "calendarTitle"
    ).textContent = monthName;


    const firstDay =
        new Date(
            year,
            month,
            1
        ).getDay();


    const daysInMonth =
        new Date(
            year,
            month + 1,
            0
        ).getDate();


    const grid =
        document.getElementById(
            "calendarGrid"
        );


    grid.innerHTML = "";


    for (let i = 0; i < firstDay; i++) {

        const empty =
            document.createElement("div");

        empty.className = "calendar-day";

        grid.appendChild(empty);

    }


    for (let day = 1; day <= daysInMonth; day++) {

        const cell =
            document.createElement("div");

        cell.className = "calendar-day";


        const date =
            `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;


        const today =
            new Date()
                .toISOString()
                .split("T")[0];


        if (date === today) {

            cell.classList.add("today");

        }


        cell.innerHTML = `

            <div class="calendar-day-number">
                ${day}
            </div>

        `;


        const dayTasks =
            tasks.filter(task =>
                task.date === date
            );


        dayTasks.forEach(task => {

            const taskElement =
                document.createElement("div");

            taskElement.className =
                "calendar-task";

            taskElement.textContent =
                task.title;

            cell.appendChild(taskElement);

        });


        grid.appendChild(cell);

    }

}


document
    .getElementById("previousMonth")
    .addEventListener("click", () => {

        calendarDate.setMonth(
            calendarDate.getMonth() - 1
        );

        renderCalendar();

    });


document
    .getElementById("nextMonth")
    .addEventListener("click", () => {

        calendarDate.setMonth(
            calendarDate.getMonth() + 1
        );

        renderCalendar();

    });


// ============================================
// SEARCH
// ============================================

document
    .getElementById("searchInput")
    .addEventListener(
        "input",
        renderAllTasks
    );


document
    .getElementById("filterSelect")
    .addEventListener(
        "change",
        renderAllTasks
    );


// ============================================
// DARK MODE
// ============================================

document
    .getElementById("themeToggle")
    .addEventListener("click", () => {

        document.body.classList.toggle("dark");

        localStorage.setItem(
            "studyflow_dark",
            document.body.classList.contains("dark")
        );

    });


if (
    localStorage.getItem("studyflow_dark")
    === "true"
) {

    document.body.classList.add("dark");

}


// ============================================
// HELPERS
// ============================================

function capitalize(text) {

    return text.charAt(0).toUpperCase()
        + text.slice(1);

}


function escapeHTML(text) {

    const div =
        document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}


// ============================================
// RENDER EVERYTHING
// ============================================

function renderAll() {

    renderDashboard();

    renderAllTasks();

    renderCompleted();

    renderCalendar();

}


renderAll();