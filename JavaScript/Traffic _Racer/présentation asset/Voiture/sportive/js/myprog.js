let cnv = document.getElementById('myCanvas');
let ctx = cnv.getContext('2d');
ctx.imageSmoothingEnabled= false;

let img_names = ["car1","car2",
"car3", "car4", "car5", "car6", "car7", "car8", "car9", "car10", "car11", "car12"];
let all_img = [];

for(let i = 0; i < 12; i += 1)
{
    let img = new Image();
    img.src = "./assets/"+img_names[i]+".png";
    all_img.push(img);
}

let decale_droite = 10
let decale_bas = 10

function update()
{
    for(let k = 0; k < 6; k += 1)
    {
        ctx.drawImage(all_img[k], decale_droite, decale_bas, 150, 300);
        decale_droite += 160 
    }

    decale_droite = 10
    decale_bas = 320

    for(let j = 6; j < 12; j += 1)
    {
        ctx.drawImage(all_img[j], decale_droite, decale_bas, 150, 300);
        decale_droite += 160 
    }
}
setInterval(update, 200);