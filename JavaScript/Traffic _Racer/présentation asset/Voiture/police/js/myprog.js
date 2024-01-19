let cnv = document.getElementById('myCanvas');
let ctx = cnv.getContext('2d');
ctx.imageSmoothingEnabled= false;

let imgPolice = new Image();
imgPolice.src = "./assets/police.png";

function update()
{

    ctx.beginPath();
    ctx.drawImage(imgPolice, 10, 10, 300, 600);
    ctx.closePath();

}
setInterval(update, 200);
