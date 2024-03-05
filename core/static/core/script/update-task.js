
function updateTaskCount () {
    const taskCount = document.querySelector('.js-task-count');

    console.log(taskCount);

    const newTaskCount = Number(taskCount.innerHTML) - 1;
    taskCount.innerHTML = newTaskCount;

}


