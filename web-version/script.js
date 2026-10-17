
const STORAGE_KEY = "taskflow_tasks_v1";
const THEME_KEY = "taskflow_theme_v1";

const $ = (selector) => document.querySelector(selector);

const elements = {
    taskList: $("#taskList"),
    taskForm: $("#taskForm"),
    taskModal: $("#taskModal"),
    taskTitle: $("#taskTitle"),
    taskDescription: $("#taskDescription"),
    taskCategory: $("#taskCategory"),
    taskPriority: $("#taskPriority"),
    taskDueDate: $("#taskDueDate"),
    taskDueTime: $("#taskDueTime"),
    modalTitle: $("#modalTitle"),
    saveTaskButton: $("#saveTaskButton"),
    searchInput: $("#searchInput"),
    clearSearch: $("#clearSearch"),
    priorityFilter: $("#priorityFilter"),
    sortTasks: $("#sortTasks"),
    toast: $("#toast")
};

let tasks = loadTasks();
let currentFilter = "all";
let currentCategory = null;
let editingTaskId = null;
let toastTimer;

const priorities = {
    High: 3,
    Medium: 2,
    Low: 1
};

// -------------------- STORAGE --------------------

function loadTasks() {
    try {
        const savedTasks = localStorage.getItem(STORAGE_KEY);

        if (!savedTasks) {
            return [];
        }

        const parsedTasks = JSON.parse(savedTasks);

        if (!Array.isArray(parsedTasks)) {
            return [];
        }

        return parsedTasks.filter(task =>
            task &&
            typeof task.id === "string" &&
            typeof task.title === "string" &&
            typeof task.completed === "boolean" &&
            ["High", "Medium", "Low"].includes(task.priority) &&
            ["Personal", "Work", "Study", "Other"].includes(task.category)
        ).map(task => ({
            id: task.id,
            title: task.title.slice(0, 120),
            description: typeof task.description === "string"
                ? task.description.slice(0, 500)
                : "",
            category: task.category,
            priority: task.priority,
            dueDate: typeof task.dueDate === "string" ? task.dueDate : "",
            dueTime: typeof task.dueTime === "string" ? task.dueTime : "",
            completed: task.completed,
            createdAt: typeof task.createdAt === "string"
                ? task.createdAt
                : new Date().toISOString(),
            completedAt: typeof task.completedAt === "string"
                ? task.completedAt
                : null
        }));
    } catch (error) {
        console.error("Could not load tasks:", error);
        return [];
    }
}

function saveTasks() {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
        return true;
    } catch (error) {
        console.error("Could not save tasks:", error);
        showToast("Unable to save. Browser storage may be full or unavailable.");
        return false;
    }
}

// -------------------- DATE HELPERS --------------------

function getLocalDateString(date = new Date()) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");

    return `${year}-${month}-${day}`;
}

function formatDate(dateString) {
    if (!dateString) {
        return "";
    }

    const parts = dateString.split("-").map(Number);

    if (parts.length !== 3 || parts.some(number => !number)) {
        return dateString;
    }

    const date = new Date(parts[0], parts[1] - 1, parts[2]);

    return date.toLocaleDateString("en-US", {
        month: "short",
        day: "numeric",
        year: "numeric"
    });
}

function isOverdue(task) {
    return Boolean(
        task.dueDate &&
        task.dueDate < getLocalDateString() &&
        !task.completed
    );
}

function isDueToday(task) {
    return Boolean(
        task.dueDate &&
        task.dueDate === getLocalDateString() &&
        !task.completed
    );
}

function isDueSoon(task) {
    if (!task.dueDate || task.completed) {
        return false;
    }

    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const due = new Date(task.dueDate + "T00:00:00");
    const days = (due - today) / 86400000;

    return days >= 0 && days <= 7;
}

function formatDueDate(task) {
    if (!task.dueDate) {
        return "";
    }

    let label = `Due ${formatDate(task.dueDate)}`;

    if (task.dueTime) {
        const [hours, minutes] = task.dueTime.split(":").map(Number);

        if (
            Number.isInteger(hours) &&
            Number.isInteger(minutes) &&
            hours >= 0 && hours <= 23 &&
            minutes >= 0 && minutes <= 59
        ) {
            const time = new Date();
            time.setHours(hours, minutes, 0, 0);

            label += `, ${time.toLocaleTimeString("en-US", {
                hour: "numeric",
                minute: "2-digit"
            })}`;
        }
    }

    return label;
}

// -------------------- TASK MANAGEMENT --------------------

function createId() {
    if (window.crypto && typeof window.crypto.randomUUID === "function") {
        return window.crypto.randomUUID();
    }

    return `${Date.now()}-${Math.random().toString(36).slice(2)}`;
}

function addTask(taskData) {
    const task = {
        id: createId(),
        title: taskData.title,
        description: taskData.description,
        category: taskData.category,
        priority: taskData.priority,
        dueDate: taskData.dueDate,
        dueTime: taskData.dueTime,
        completed: false,
        createdAt: new Date().toISOString(),
        completedAt: null
    };

    tasks.unshift(task);

    if (!saveTasks()) {
        tasks = tasks.filter(item => item.id !== task.id);
        return;
    }

    renderApp();
    showToast("Task created successfully.");
}

function updateTask(id, taskData) {
    const index = tasks.findIndex(task => task.id === id);

    if (index === -1) {
        showToast("Task could not be found.");
        return;
    }

    const oldTask = tasks[index];

    tasks[index] = {
        ...oldTask,
        title: taskData.title,
        description: taskData.description,
        category: taskData.category,
        priority: taskData.priority,
        dueDate: taskData.dueDate,
        dueTime: taskData.dueTime
    };

    if (!saveTasks()) {
        tasks[index] = oldTask;
        return;
    }

    renderApp();
    showToast("Task updated successfully.");
}

function toggleTask(id) {
    const task = tasks.find(item => item.id === id);

    if (!task) {
        return;
    }

    const oldCompleted = task.completed;
    const oldCompletedAt = task.completedAt;

    task.completed = !task.completed;
    task.completedAt = task.completed
        ? new Date().toISOString()
        : null;

    if (!saveTasks()) {
        task.completed = oldCompleted;
        task.completedAt = oldCompletedAt;
        return;
    }

    renderApp();

    showToast(
        task.completed
            ? "Great job! Task completed."
            : "Task marked as incomplete."
    );
}

function deleteTask(id) {
    const task = tasks.find(item => item.id === id);

    if (!task) {
        return;
    }

    const confirmed = window.confirm(
        `Delete "${task.title}"?\n\nThis action cannot be undone.`
    );

    if (!confirmed) {
        return;
    }

    const oldTasks = [...tasks];
    tasks = tasks.filter(item => item.id !== id);

    if (!saveTasks()) {
        tasks = oldTasks;
        return;
    }

    renderApp();
    showToast("Task deleted.");
}

function clearCompletedTasks() {
    const completed = tasks.filter(task => task.completed);

    if (completed.length === 0) {
        showToast("There are no completed tasks to clear.");
        return;
    }

    const confirmed = window.confirm(
        `Delete all ${completed.length} completed task(s)?`
    );

    if (!confirmed) {
        return;
    }

    const oldTasks = [...tasks];
    tasks = tasks.filter(task => !task.completed);

    if (!saveTasks()) {
        tasks = oldTasks;
        return;
    }

    renderApp();
    showToast("Completed tasks cleared.");
}

// -------------------- TASK FORM --------------------

function openTaskModal(task = null) {
    editingTaskId = task ? task.id : null;

    elements.taskForm.reset();

    elements.modalTitle.textContent = task
        ? "Edit task"
        : "Create a task";

    elements.saveTaskButton.textContent = task
        ? "Save changes"
        : "Save task";

    elements.taskTitle.value = task ? task.title : "";
    elements.taskDescription.value = task ? task.description : "";
    elements.taskCategory.value = task ? task.category : "Personal";
    elements.taskPriority.value = task ? task.priority : "Medium";
    elements.taskDueDate.value = task ? task.dueDate : "";
    elements.taskDueTime.value = task ? task.dueTime : "";

    elements.taskModal.hidden = false;
    document.body.style.overflow = "hidden";

    elements.taskTitle.focus();
}

function closeTaskModal() {
    elements.taskModal.hidden = true;
    document.body.style.overflow = "";
    editingTaskId = null;
}

function handleTaskSubmit(event) {
    event.preventDefault();

    const title = elements.taskTitle.value.trim();

    if (!title) {
        showToast("Please enter a task title.");
        elements.taskTitle.focus();
        return;
    }

    const dueDate = elements.taskDueDate.value;
    const dueTime = elements.taskDueTime.value;

    if (dueTime && !dueDate) {
        showToast("Please select a due date before adding a due time.");
        elements.taskDueDate.focus();
        return;
    }

    const taskData = {
        title,
        description: elements.taskDescription.value.trim(),
        category: elements.taskCategory.value,
        priority: elements.taskPriority.value,
        dueDate,
        dueTime
    };

    if (editingTaskId) {
        updateTask(editingTaskId, taskData);
    } else {
        addTask(taskData);
    }

    closeTaskModal();
}

// -------------------- FILTERING AND SORTING --------------------

function getFilteredTasks() {
    let filtered = [...tasks];

    if (currentFilter === "today") {
        filtered = filtered.filter(task =>
            task.dueDate === getLocalDateString() && !task.completed
        );
    } else if (currentFilter === "upcoming") {
        filtered = filtered.filter(task => isDueSoon(task));
    } else if (currentFilter === "completed") {
        filtered = filtered.filter(task => task.completed);
    }

    if (currentCategory) {
        filtered = filtered.filter(task =>
            task.category === currentCategory
        );
    }

    const query = elements.searchInput.value.trim().toLowerCase();

    if (query) {
        filtered = filtered.filter(task =>
            task.title.toLowerCase().includes(query) ||
            task.description.toLowerCase().includes(query) ||
            task.category.toLowerCase().includes(query) ||
            task.priority.toLowerCase().includes(query)
        );
    }

    const priority = elements.priorityFilter.value;

    if (priority !== "all") {
        filtered = filtered.filter(task => task.priority === priority);
    }

    const sort = elements.sortTasks.value;

    if (sort === "due") {
        filtered.sort((a, b) => {
            const aDate = a.dueDate || "9999-12-31";
            const bDate = b.dueDate || "9999-12-31";

            if (aDate !== bDate) {
                return aDate.localeCompare(bDate);
            }

            return (a.dueTime || "23:59").localeCompare(
                b.dueTime || "23:59"
            );
        });
    } else if (sort === "priority") {
        filtered.sort((a, b) =>
            priorities[b.priority] - priorities[a.priority]
        );
    } else if (sort === "alphabetical") {
        filtered.sort((a, b) =>
            a.title.localeCompare(b.title)
        );
    } else {
        filtered.sort((a, b) =>
            new Date(b.createdAt).getTime() -
            new Date(a.createdAt).getTime()
        );
    }

    return filtered;
}

function setFilter(filter, category = null) {
    currentFilter = filter;
    currentCategory = category;

    document.querySelectorAll(".nav-item").forEach(button => {
        button.classList.remove("active");
    });

    if (category) {
        const categoryButton = document.querySelector(
            `.category-filter[data-category="${category}"]`
        );

        if (categoryButton) {
            categoryButton.classList.add("active");
        }
    } else {
        const filterButton = document.querySelector(
            `.nav-item[data-filter="${filter}"]`
        );

        if (filterButton) {
            filterButton.classList.add("active");
        }
    }

    const headings = {
        all: ["Your tasks", "Manage your daily priorities.", "Overview"],
        today: ["My day", "Tasks scheduled for today.", "My Day"],
        upcoming: ["Upcoming tasks", "Tasks due within the next 7 days.", "Upcoming"],
        completed: ["Completed tasks", "Look at everything you've accomplished.", "Completed"]
    };

    let heading;
    let subtitle;
    let page;

    if (category) {
        heading = `${category} tasks`;
        subtitle = `Tasks organized in ${category.toLowerCase()}.`;
        page = category;
    } else {
        [heading, subtitle, page] = headings[filter];
    }

    $("#taskHeading").textContent = heading;
    $("#taskSubheading").textContent = subtitle;
    $("#currentPage").textContent = page;

    renderApp();
}

// -------------------- RENDER TASKS --------------------

function createTaskElement(task) {
    const article = document.createElement("article");
    article.className = `task-item${task.completed ? " is-completed" : ""}`;

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.className = "task-checkbox";
    checkbox.checked = task.completed;
    checkbox.setAttribute("aria-label", `Complete ${task.title}`);

    checkbox.addEventListener("change", () => toggleTask(task.id));

    const main = document.createElement("div");
    main.className = "task-main";

    const title = document.createElement("h3");
    title.className = "task-title";
    title.textContent = task.title;

    main.appendChild(title);

    if (task.description) {
        const description = document.createElement("p");
        description.className = "task-description";
        description.textContent = task.description;
        main.appendChild(description);
    }

    const meta = document.createElement("div");
    meta.className = "task-meta";

    const category = document.createElement("span");
    category.className = "tag";
    category.textContent = task.category;
    meta.appendChild(category);

    const priority = document.createElement("span");
    priority.className = `priority-badge priority-${task.priority.toLowerCase()}`;
    priority.textContent = `${task.priority} priority`;
    meta.appendChild(priority);

    if (task.dueDate) {
        const due = document.createElement("span");
        due.className = "task-due";
        due.textContent = formatDueDate(task);

        if (isOverdue(task)) {
            due.classList.add("overdue");
            due.textContent = `Overdue · ${formatDueDate(task)}`;
        } else if (isDueToday(task)) {
            due.classList.add("due-today");
            due.textContent = `Today · ${formatDueDate(task)}`;
        }

        meta.appendChild(due);
    }

    main.appendChild(meta);

    const actions = document.createElement("div");
    actions.className = "task-actions";

    const editButton = document.createElement("button");
    editButton.type = "button";
    editButton.className = "icon-button";
    editButton.textContent = "✎";
    editButton.title = "Edit task";
    editButton.setAttribute("aria-label", `Edit ${task.title}`);

    editButton.addEventListener("click", () => openTaskModal(task));

    const deleteButton = document.createElement("button");
    deleteButton.type = "button";
    deleteButton.className = "icon-button delete";
    deleteButton.textContent = "×";
    deleteButton.title = "Delete task";
    deleteButton.setAttribute("aria-label", `Delete ${task.title}`);

    deleteButton.addEventListener("click", () => deleteTask(task.id));

    actions.append(editButton, deleteButton);
    article.append(checkbox, main, actions);

    return article;
}

function renderTaskList() {
    const filteredTasks = getFilteredTasks();

    elements.taskList.replaceChildren();

    $("#visibleCount").textContent =
        `${filteredTasks.length} ${filteredTasks.length === 1 ? "task" : "tasks"}`;

    elements.clearSearch.hidden = !elements.searchInput.value;

    if (filteredTasks.length === 0) {
        const empty = document.createElement("div");
        empty.className = "empty-state";

        const icon = document.createElement("div");
        icon.className = "empty-icon";
        icon.textContent = elements.searchInput.value ? "⌕" : "✓";

        const heading = document.createElement("h3");
        heading.textContent = elements.searchInput.value
            ? "No matching tasks"
            : currentFilter === "completed"
                ? "Nothing completed yet"
                : currentFilter === "today"
                    ? "Your day is clear"
                    : currentFilter === "upcoming"
                        ? "No upcoming tasks"
                        : "No tasks yet";

        const description = document.createElement("p");
        description.textContent = elements.searchInput.value
            ? "Try a different search or change your filters."
            : currentFilter === "completed"
                ? "Complete a task and it will appear here."
                : currentFilter === "today"
                    ? "Tasks with today's due date will appear here."
                    : currentFilter === "upcoming"
                        ? "Tasks due in the next seven days will appear here."
                        : "Create your first task and start organizing your day.";

        empty.append(icon, heading, description);

        if (
            currentFilter === "all" &&
            !currentCategory &&
            !elements.searchInput.value
        ) {
            const button = document.createElement("button");
            button.type = "button";
            button.className = "primary-button";
            button.textContent = "＋ Create your first task";
            button.addEventListener("click", () => openTaskModal());
            empty.appendChild(button);
        }

        elements.taskList.appendChild(empty);
    } else {
        const fragment = document.createDocumentFragment();

        filteredTasks.forEach(task => {
            fragment.appendChild(createTaskElement(task));
        });

        elements.taskList.appendChild(fragment);
    }

    const completedCount = tasks.filter(task => task.completed).length;

    $("#listFooterText").textContent = tasks.length === 0
        ? "Your productivity journey starts here."
        : `${completedCount} of ${tasks.length} tasks completed`;
}

// -------------------- DASHBOARD STATISTICS --------------------

function renderStatistics() {
    const total = tasks.length;
    const completed = tasks.filter(task => task.completed).length;
    const pending = total - completed;
    const overdue = tasks.filter(task => isOverdue(task)).length;
    const today = tasks.filter(task =>
        task.dueDate === getLocalDateString() && !task.completed
    ).length;

    const percentage = total === 0
        ? 0
        : Math.round((completed / total) * 100);

    $("#totalTasks").textContent = total;
    $("#pendingTasks").textContent = pending;
    $("#completedTasks").textContent = completed;
    $("#overdueTasks").textContent = overdue;

    $("#allCount").textContent = total;
    $("#todayCount").textContent = today;

    $("#completionPercent").textContent = `${percentage}%`;
    $("#legendCompleted").textContent = completed;
    $("#legendPending").textContent = pending;

    const circumference = 2 * Math.PI * 57;
    const offset = circumference - (percentage / 100) * circumference;

    $("#circleValue").style.strokeDasharray = circumference;
    $("#circleValue").style.strokeDashoffset = offset;

    $("#sidebarPercent").textContent = `${percentage}%`;
    $("#sidebarProgress").style.width = `${percentage}%`;

    $("#sidebarProgressText").textContent = total === 0
        ? "Let's get things done!"
        : percentage === 100
            ? "Amazing! Everything is complete."
            : `${completed} completed, ${pending} to go.`;

    const priorityCounts = {
        High: tasks.filter(task => task.priority === "High" && !task.completed).length,
        Medium: tasks.filter(task => task.priority === "Medium" && !task.completed).length,
        Low: tasks.filter(task => task.priority === "Low" && !task.completed).length
    };

    const priorityContainer = $("#priorityBreakdown");
    priorityContainer.replaceChildren();

    const fragment = document.createDocumentFragment();

    Object.entries(priorityCounts).forEach(([priority, count]) => {
        const row = document.createElement("div");
        row.className = "priority-row";

        const heading = document.createElement("div");
        heading.className = "priority-row-heading";

        const label = document.createElement("span");
        label.textContent = `${priority} priority`;

        const number = document.createElement("strong");
        number.textContent = count;

        heading.append(label, number);

        const bar = document.createElement("div");
        bar.className = "priority-bar";

        const fill = document.createElement("div");
        fill.className = `priority-bar-fill ${priority.toLowerCase()}`;

        const percentageOfPending = pending === 0
            ? 0
            : (count / pending) * 100;

        fill.style.width = `${percentageOfPending}%`;

        bar.appendChild(fill);
        row.append(heading, bar);
        fragment.appendChild(row);
    });

    priorityContainer.appendChild(fragment);
}

// -------------------- GREETING AND PAGE --------------------

function renderGreeting() {
    const hour = new Date().getHours();

    let greeting = "YOUR PRODUCTIVITY SPACE";
    let title = "Good evening.";

    if (hour < 12) {
        title = "Good morning.";
        greeting = "START YOUR DAY RIGHT";
    } else if (hour < 18) {
        title = "Good afternoon.";
        greeting = "KEEP UP THE MOMENTUM";
    }

    $("#greeting").textContent = greeting;
    $("#welcomeTitle").textContent = title;

    $("#headerDate").textContent = new Date().toLocaleDateString("en-US", {
        weekday: "short",
        month: "short",
        day: "numeric"
    });

    $("#footerYear").textContent = `© ${new Date().getFullYear()}`;
}

function renderApp() {
    renderTaskList();
    renderStatistics();
}

// -------------------- DARK MODE --------------------

function applyTheme(theme) {
    const isDark = theme === "dark";

    document.body.classList.toggle("dark-mode", isDark);

    $("#themeIcon").textContent = isDark ? "☀" : "☾";
    $("#themeText").textContent = isDark ? "Light mode" : "Dark mode";

    $("#themeToggle").setAttribute(
        "aria-label",
        isDark ? "Switch to light mode" : "Switch to dark mode"
    );

    $("#themeToggle").setAttribute("aria-pressed", String(isDark));

    try {
        localStorage.setItem(THEME_KEY, theme);
    } catch (error) {
        console.warn("Could not save theme preference:", error);
    }
}

function initializeTheme() {
    let savedTheme = null;

    try {
        savedTheme = localStorage.getItem(THEME_KEY);
    } catch (error) {
        console.warn("Could not load theme preference:", error);
    }

    if (savedTheme !== "light" && savedTheme !== "dark") {
        savedTheme = window.matchMedia &&
            window.matchMedia("(prefers-color-scheme: dark)").matches
            ? "dark"
            : "light";
    }

    applyTheme(savedTheme);
}

// -------------------- NOTIFICATIONS --------------------

function showToast(message) {
    clearTimeout(toastTimer);

    elements.toast.textContent = message;
    elements.toast.classList.add("show");

    toastTimer = setTimeout(() => {
        elements.toast.classList.remove("show");
    }, 2800);
}

// -------------------- EVENT LISTENERS --------------------

elements.taskForm.addEventListener("submit", handleTaskSubmit);

$("#openAddModal").addEventListener("click", () => openTaskModal());

$("#closeModal").addEventListener("click", closeTaskModal);

$("#cancelModal").addEventListener("click", closeTaskModal);

elements.taskModal.addEventListener("click", event => {
    if (event.target === elements.taskModal) {
        closeTaskModal();
    }
});

document.addEventListener("keydown", event => {
    if (event.key === "Escape" && !elements.taskModal.hidden) {
        closeTaskModal();
    }
});

document.querySelectorAll(".nav-item[data-filter]").forEach(button => {
    button.addEventListener("click", () => {
        setFilter(button.dataset.filter);
    });
});

document.querySelectorAll(".category-filter").forEach(button => {
    button.addEventListener("click", () => {
        setFilter("all", button.dataset.category);
    });
});

elements.searchInput.addEventListener("input", renderTaskList);

elements.clearSearch.addEventListener("click", () => {
    elements.searchInput.value = "";
    renderTaskList();
    elements.searchInput.focus();
});

elements.priorityFilter.addEventListener("change", renderTaskList);

elements.sortTasks.addEventListener("change", renderTaskList);

$("#clearCompleted").addEventListener("click", clearCompletedTasks);

$("#themeToggle").addEventListener("click", () => {
    const isDark = document.body.classList.contains("dark-mode");
    applyTheme(isDark ? "light" : "dark");
});

// -------------------- INITIALIZE APPLICATION --------------------

initializeTheme();
renderGreeting();
renderApp();
