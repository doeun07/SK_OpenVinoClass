const webcamTestElem = document.querySelector(`#webcamTest`);

function updatePoseImg() {
    const img = new Image();
    const randomValue = Math.random();

    img.onload = function () {
        webcamTestElem.style.backgroundImage = `url('${img.src}')`;
    };
    
    img.src = `/getPoseImg?${randomValue}`;
}

function whereISMyBone() {
    alert("재시작은 에러의 90%를 해결해줍니다.\n확인을 눌러 에러를 해결해보세요.");
    $.get("/killChrome")
}

function startGame() {
    location.href = "/ingame";
}

function createProblem() {
    $.get("/createProblem").done((result) => {
        document.querySelector("#problem h1").innerText = `${result.first_num} ${result.selected_num} ${result.second_num} = ?`
    })
}

let timer = 3;
function saveImage() {
    if (timer <= 1) {
        $.get("/saveImage").done((result) => {
            console.log(result);
        })
        timer = 3;
    } else {
        timer--;
    }

    document.querySelector("#problem h2").innerText = timer;

}